# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>
#

from gizela.adj.local.PointLocal import PointLocal
from gizela.util.Error import Error
import numpy


class PointLocalCovMatError(Error):
    def __init__(self, message, point=None):
        if point is not None:
            message = "Error: " + point.__str__() + "\n" + "Error: " + message
        else:
            message = "Error: " + message
        super().__init__(message)


class PointLocalCovMat(PointLocal):
    """
    class for geodetic coordinates x, y, z
    and its covariance matrix

    covariance matrix is numpy array
        upper triangular part is used only
    """

    def __init__(self, id, x=None, y=None, z=None, status=None, covmat=None, index=None):
        """x, y, z ... coordinates
        covmat ... covariance matrix
        index  ... indexes of rows in covariance matrix
                   (zi,)
                   (xi, yi)
                   (xi, yi, zi)
        """

        super().__init__(id=id, x=x, y=y, z=z, status=status)

        self._covmat = covmat
        if index is not None:
            self.setCovMatIndex(index)
        else:
            self._index = None

    def setCovMat(self, covmat):
        "sets covariance matrix"
        self._covmat = covmat

    def getCovMat(self):
        "gets covariance matrix"
        return self._covmat

    def getCovMatIndex(self):
        'returns covariance matrix index'
        if self._index is None:
            raise PointLocalCovMatError("Index is not set")
        if self.dim() != len(self._index):
            raise PointLocalCovMatError("Dimension of point {0} is different than lenght of index {1}".
                                        format(self.dim(), len(self._index)), self)
        return self._index

    def setCovMatIndex(self, index):
        if self.dim() != len(index):
            raise PointLocalCovMatError("Dimension of point {0} is different than lenght of index {1}".
                                        format(self.dim(), len(index)), self)
        self._index = index

    def getPointCovMatList(self):
        '''
        return covariances and variances of point in list
        format: upper triangular part by rows
        '''
        if self._covmat is None:
            raise PointLocalCovMatError("Covariance matrix is not defined", self)

        index = self.getCovMatIndex()
        cmDim = len(index)
        cmList = []
        if  cmDim == 1:
            zi = index[0]
            cmList.append(self._covmat[zi, zi])
        elif cmDim == 2:
            xi, yi = index[0], index[1]
            cmList.append(self._covmat[xi, xi])
            cmList.append(self._covmat[xi, yi])
            cmList.append(self._covmat[yi, yi])
        elif cmDim == 3:
            xi, yi, zi = index[0], index[1], index[2]
            cmList.append(self._covmat[xi, xi])
            cmList.append(self._covmat[xi, yi])
            cmList.append(self._covmat[xi, zi])
            cmList.append(self._covmat[yi, yi])
            cmList.append(self._covmat[yi, zi])
            cmList.append(self._covmat[zi, zi])
        return cmList

    def getPointCovMatListWithNones(self):
        '''
        return covariances and variances of point in list
        format: upper triangular part by rows
        the length of list returned is also 6
        '''
        if self._covmat is None:
            raise PointLocalCovMatError("Covariance matrix is not defined", self)

        index = self.getCovMatIndex()
        cmDim = len(index)
        cmList = [None for i in range(6)]
        if  cmDim == 1:
            zi = index[0]
            cmList[5] = self._covmat[zi, zi]
        elif cmDim == 2:
            xi, yi = index[0], index[1]
            cmList[0] = self._covmat[xi, xi]
            cmList[1] = self._covmat[xi, yi]
            cmList[2] = self._covmat[yi, yi]
        elif cmDim == 3:
            xi, yi, zi = index[0], index[1], index[2]
            cmList[0] = self._covmat[xi, xi]
            cmList[1] = self._covmat[xi, yi]
            cmList[2] = self._covmat[xi, zi]
            cmList[3] = self._covmat[yi, yi]
            cmList[4] = self._covmat[yi, zi]
            cmList[5] = self._covmat[zi, zi]
        return cmList

    def getPointCovMat(self):
        '''
        returns a copy of covariance matrix
        selection of covariance matrix from large covariance matrix is supported
        '''
        if self._covmat is None:
            raise PointLocalCovMatError("Covariance matrix is not defined", self)

        index = self.getCovMatIndex()
        cmDim = len(index)
        cm = numpy.zeros((cmDim, cmDim))
        if  cmDim == 1:
            zi = index[0]
            cm[0, 0] = self._covmat[zi, zi]
        elif cmDim == 2:
            xi, yi = index[0], index[1]
            cm[0, 0] = self._covmat[xi, xi]
            cm[0, 1] = self._covmat[xi, yi]
            cm[1, 0] = self._covmat[xi, yi]
            cm[1, 1] = self._covmat[yi, yi]
        elif cmDim == 3:
            xi, yi, zi = index[0], index[1], index[2]
            cm[0, 0] = self._covmat[xi, xi]
            cm[1, 1] = self._covmat[yi, yi]
            cm[2, 2] = self._covmat[zi, zi]
            cm[0, 1] = self._covmat[xi, yi]
            cm[1, 0] = self._covmat[xi, yi]
            cm[0, 2] = self._covmat[xi, zi]
            cm[2, 0] = self._covmat[xi, zi]
            cm[1, 2] = self._covmat[yi, zi]
            cm[2, 1] = self._covmat[yi, zi]
        return cm

    def setPointCovmat(self, covmat):
        """
        sets covariances and variances of point

        covmat: numpy array with proper dimension
            upper triangular part of the matrix is used
        """
        index = self.getCovMatIndex()
        dim = self.dim()

        shape = covmat.shape
        if shape[0] != shape[1]:
            raise PointLocalCovMatError("Covariance matrix is not square", self)
        if dim != shape[0]:
            raise PointLocalCovMatError("Dimension of covariance matrix ({0}) is not equal to dimension of point ({1})".
                                        format(dim, shape[0]), self)

        # set variances and covariances
        if dim == 1:
            zi = index[0]
            self._covmat[zi, zi] = covmat[0, 0]
        elif dim == 2:
            xi, yi = index[0], index[1]
            self._covmat[xi, xi] = covmat[0, 0]
            self._covmat[yi, yi] = covmat[1, 1]
            self._covmat[xi, yi] = covmat[0, 1]
        elif dim == 3:
            xi, yi, zi = index[0], index[1], index[2]
            self._covmat[xi, xi] = covmat[0, 0]
            self._covmat[yi, yi] = covmat[1, 1]
            self._covmat[zi, zi] = covmat[2, 2]
            self._covmat[xi, yi] = covmat[0, 1]
            self._covmat[xi, zi] = covmat[0, 2]
            self._covmat[yi, zi] = covmat[1, 2]

    def getErrorEllipseParam(self):
        """
        returns parameters of standard error ellipse
        (a, b, omega)
        omega ... clockwise from x axis in radians in interval -pi:pi
        """
        if self.x is None or self.y is None:
            raise PointLocalCovMatError("No x or y coordinates set", self)
        index = self.getCovMatIndex()
        xi, yi = index[0], index[1]
        vx = self._covmat[xi, xi]
        vy = self._covmat[yi, yi]
        cxy = self._covmat[xi, yi]

        # test of positive definity
        det = vx * vy - cxy * cxy
        if det < -1e-6:
            raise PointLocalCovMatError("Covariance matrix is not positive definite: det = {0:e}".format(det), self)

        import math
        c = math.sqrt((vx - vy) ** 2 + 4.0 * cxy * cxy)
        a = math.sqrt((vx + vy + c) / 2.0)
        if vx + vy - c < 0.0:
            b = 0.0
        else:
            b = math.sqrt((vx + vy - c) / 2.0)
        omega = math.atan2(2.0 * cxy, vx - vy) / 2.0

        return [a, b, omega]

    def __add__sub__(self, other, add):
        '''
        addition or subtraction of two points with covariance matrix

        add: True of False

        returns a new point with his own covariance matrix
        id and status is from self instance
        '''

        if not isinstance(other, PointLocalCovMat):
            raise PointLocalCovMatError("Addition of two PointLocalCovMat instances supported", self)

        if add:
            co = super().__add__(other)
        else:
            co = super().__sub__(other)

        # covariance matrix
        if self._covmat is None and other.getCovMat() is None:
            co.setCovMat(None)
        else:
            if self._covmat is None:
                raise PointLocalCovMatError("Covariance matrix is not set", self)
            if other.getCovMat() is None:
                raise PointLocalCovMatError("Covariance matrix is not set", other)

        cm1 = self.getPointCovMat()
        cm2 = self.getPointCovMat()
        if cm1.size != cm2.size:
            raise PointLocalCovMatError("Dimensions of covariance matrices are not same {0}!={1}".
                                        format(cm1.shape[0], cm2.shape[0]), self)
        co._covmat = cm1 + cm2
        co._index = tuple(i for i in range(self.dim()))
        return co

    def __add__(self, other):
        return self.__add__sub__(other, True)

    def __sub__(self, other):
        return self.__add__sub__(other, False)

    def __str__(self):
        if self._covmat is None:
            cmStr = "CovMat(None)"
        else:
            cmStr = "CovMat({shape[0]}, {shape[1]})".format(shape=self._covmat.shape)
        if self._index is None:
            ixStr = "Index(None)"
            valStr = ""
        else:
            ixStr = "Index(" + ", ".join(["{0}".format(i) for i in self._index]) + ")"
            if self._covmat is not None:
                valStr = "Values(" + ", ".join(["{0}".format(i) for i in self.getPointCovMatList()]) + ")"
            else:
                valStr = ""
        return "  ".join([super().__str__(),
                          cmStr,
                          ixStr,
                          valStr])


if __name__ == "__main__":

    print('empty point')
    p = PointLocalCovMat(None)
    print(p)

    print('regular point with covariance matrix')
    from gizela.adj.local.POINT_LOCAL_STATUS import POINT_LOCAL_STATUS
    c1 = PointLocalCovMat("P1", x=10, y=20, z=30, status=POINT_LOCAL_STATUS.adj)
    cm = numpy.array([[1, 0, 0.1], [0, 2, 0.2], [0, 0, 2.5]])
    c1.setCovMat(cm)
    c1.setCovMatIndex((0, 1, 2))
    print(c1)

    print('getPointCovmat')
    cm = numpy.array([[1, 0, 0.1, 0.5], [0, 2, 0.2, 0.6], [0, 0, 2.5, 0.1], [0, 0, 0, 1]])
    c2 = PointLocalCovMat("P2", x=100, y=200)
    try:
        print(c1.getPointCovMat())
    except Exception as e:
        print(e.message)
    c2.setCovMat(cm)
    c2.setCovMatIndex((1, 2))
    print(c2)
    pcm = c2.getPointCovMat()
    print(pcm)

    print('setPointCovmat')
    c2.setPointCovmat(pcm)
    print(c2)

    print('error ellipse')
    print(c2.getErrorEllipseParam())

    print('addition and subtraction of points')
    c3 = PointLocalCovMat("P3", x=10, y=20, z=30, status=POINT_LOCAL_STATUS.adj)
    cm = numpy.array([[1, 0, 0.1], [0, 2, 0.2], [0, 0, 2.5]])
    c3.setCovMat(cm)
    c3.setCovMatIndex((0, 1, 2))
    print(c3)

    add = c1 + c3
    sub = c1 - c3
    add.id = "add"
    print(add)
    print(sub)
    print(c1)
