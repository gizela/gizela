# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>

from gizela.util.Error import Error
from gizela.adj.local.PointList import PointList
from gizela.adj.local.PointLocalCovMat import PointLocalCovMat
from gizela.adj.local.DUPLICATE_ID import DUPLICATE_ID


class PointListCovMatError(Error):
    pass


class PointListCovMat(PointList):
    """
    List of geodetic points with covariance matrix
    """

    def __init__(self, covmat=None, duplicateId=DUPLICATE_ID.error, sort=False):
        '''
        covmat: covariance matrix numpy.array
                upper triangular part is used
        duplicateId: what to do with duplicit point
        sort: sort output by id?
        '''
        super().__init__(duplicateId=duplicateId, sort=sort)
        self._covmat = covmat  # covariance matrix
        self._numCoord = 0     # covmat row index of last coordinate + 1

    def addPoint(self, point):
        '''
        Adds PointLocalCovMat into list
        Sets covariance matrix of point as covariance of point list
        Sets point index to covariance matrix of point list
        '''
        if not isinstance(point, PointLocalCovMat):
            raise PointListCovMatError("PointLocalCovMat instance expected")
        dim = point.dim()
        point.setCovMat(self._covmat)
        index = tuple(i for i in range(self._numCoord, self._numCoord + dim))
        point.setCovMatIndex(index)
        self._numCoord += dim
        super().addPoint(point)

    def getNumOfCoordinates(self):
        "returns the number of coordinates in point list"
        return self._numCoord

    #def update_covmat(self):
    #    """updating covariance matrix in each point - sharing does not work"""
    #    for point in self._list: point.covmat = self._covmat

    #def is_cov_mat_dim_ok(self):
    #    maxind = 0
    #    for point in self._list:
    #        maxind_ = max(point.index)
    #        if maxind_ > maxind: maxind = maxind_

    #    return maxind + 1 == self._covmat.dim

    def setCovMat(self, covmat):
        'set covariance matrix for all points in list'
        shape = covmat.shape
        if shape[0] != shape[1]:
            raise PointListCovMatError("Covariance matrix is not square")
        if shape[0] < self._numCoord:
            raise PointListCovMatError("Covariance matrix (dim={0}) is smaller than number of coordinates ({1})".
                                       format(shape[0], self._numCoord))
        self._covmat = covmat
        for point in self:
            point.setCovMat(covmat)

    def getCovMat(self):
        return self._covmat

    def __add__(self, other):
        "addition of two point lists"
        raise NotImplementedError("__add__ not implemented")


if __name__ == "__main__":

    from gizela.adj.local.POINT_LOCAL_STATUS import POINT_LOCAL_STATUS
    import numpy
    c1 = PointLocalCovMat("C1", x=10, y=20, z=30, status=POINT_LOCAL_STATUS.adj)
    c2 = PointLocalCovMat("C2", x=100, y=200, status=POINT_LOCAL_STATUS.adj)
    c3 = PointLocalCovMat("C3", z=3000, status=POINT_LOCAL_STATUS.adj)
    pl = PointListCovMat()
    pl.addPoint(c1)
    pl.addPoint(c2)
    pl.addPoint(c3)
    cm = numpy.array([[1, 0.1, 0.1, 0.1, 0.1, 0.1],
                      [0, 2,   0.2, 0.2, 0.2, 0.2],
                      [0, 0,   3,   0.3, 0.3, 0.3],
                      [0, 0,   0,   4,   0.4, 0.4],
                      [0, 0,   0,   0,   5,   0.5],
                      [0, 0,   0,   0,   0,   6]])
    pl.setCovMat(cm)
    print(pl)

    print('getPointCovMat')
    print(c2.getPointCovMat())

    print('setPointCovMat')
    cm = numpy.array([[10, 1], [0, 20]])
    c2.setPointCovmat(cm)
    print(pl.getCovMat())
