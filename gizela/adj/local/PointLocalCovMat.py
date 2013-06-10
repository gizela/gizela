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

        self.covmat = covmat
        if index is not None:
            self.setCovMatIndex(index)
        else:
            self._index = None

    def getCovMatIndex(self):
        'returns covariance matrix index'
        if self._index is None:
            raise PointLocalCovMatError("Index is not set")
        if self.dim() != len(self._index):
            raise PointLocalCovMatError("Dimension of point {0} is different than lenght of index {1}".
                                        format(self.dim(), len(self._index)), self)
        return self._index

    def setCovMatIndex(self, index):
        if self.covmat is None:
            raise PointLocalCovMatError("No covariance matrix set", self)
        if self.dim() != len(index):
            raise PointLocalCovMatError("Dimension of point {0} is different than lenght of index {1}".
                                        format(self.dim(), len(index)), self)
        shape = self.covmat.shape
        if max(index) > shape[0]:
            raise PointLocalCovMatError("Index exceeds covariance matrix dimension", self)
        self._index = index

    def getPointCovMatList(self):
        '''
        return covariances and variances of point in list
        format: upper triangular part by rows
        '''
        if self.covmat is None:
            raise PointLocalCovMatError("Covariance matrix is not defined", self)

        index = self.getCovMatIndex()
        cmDim = len(index)
        cmList = []
        if  cmDim == 1:
            zi = index[0]
            cmList.append(self.covmat[zi, zi])
        elif cmDim == 2:
            xi, yi = index[0], index[1]
            cmList.append(self.covmat[xi, xi])
            cmList.append(self.covmat[xi, yi])
            cmList.append(self.covmat[yi, yi])
        elif cmDim == 3:
            xi, yi, zi = index[0], index[1], index[2]
            cmList.append(self.covmat[xi, xi])
            cmList.append(self.covmat[xi, yi])
            cmList.append(self.covmat[xi, zi])
            cmList.append(self.covmat[yi, yi])
            cmList.append(self.covmat[yi, zi])
            cmList.append(self.covmat[zi, zi])
        return cmList

    def getPointCovMat(self):
        '''
        returns a copy of covariance matrix
        selection of covariance matrix from large covariance matrix is supported
        '''
        if self.covmat is None:
            raise PointLocalCovMatError("Covariance matrix is not defined", self)

        index = self.getCovMatIndex()
        cmDim = len(index)
        cm = numpy.zeros((cmDim, cmDim))
        if  cmDim == 1:
            zi = index[0]
            cm[0, 0] = self.covmat[zi, zi]
        elif cmDim == 2:
            xi, yi = index[0], index[1]
            cm[0, 0] = self.covmat[xi, xi]
            cm[0, 1] = self.covmat[xi, yi]
            cm[1, 1] = self.covmat[yi, yi]
        elif cmDim == 3:
            xi, yi, zi = index[0], index[1], index[2]
            cm[0, 0] = self.covmat[xi, xi]
            cm[1, 1] = self.covmat[yi, yi]
            cm[2, 2] = self.covmat[zi, zi]
            cm[0, 1] = self.covmat[xi, yi]
            cm[0, 2] = self.covmat[xi, zi]
            cm[1, 2] = self.covmat[yi, zi]
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
            self.covmat[zi, zi] = covmat[0, 0]
        elif dim == 2:
            xi, yi = index[0], index[1]
            self.covmat[xi, xi] = covmat[0, 0]
            self.covmat[yi, yi] = covmat[1, 1]
            self.covmat[xi, yi] = covmat[0, 1]
        elif dim == 3:
            xi, yi, zi = index[0], index[1], index[2]
            self.covmat[xi, xi] = covmat[0, 0]
            self.covmat[yi, yi] = covmat[1, 1]
            self.covmat[zi, zi] = covmat[2, 2]
            self.covmat[xi, yi] = covmat[0, 1]
            self.covmat[xi, zi] = covmat[0, 2]
            self.covmat[yi, zi] = covmat[1, 2]

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
        vx = self.covmat[xi, xi]
        vy = self.covmat[yi, yi]
        cxy = self.covmat[xi, yi]

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
        if self.covmat is None and other.covmat is None:
            co.covmat = None
        else:
            if self.covmat is None:
                raise PointLocalCovMatError("Covariance matrix is not set", self)
            if other.covmat is None:
                raise PointLocalCovMatError("Covariance matrix is not set", other)

        cm1 = self.getPointCovMat()
        cm2 = self.getPointCovMat()
        if cm1.size != cm2.size:
            raise PointLocalCovMatError("Dimensions of covariance matrices are not same {0}!={1}".
                                        format(cm1.shape[0], cm2.shape[0]), self)
        co.covmat = cm1 + cm2
        co.index = tuple(i for i in range(self.dim()))
        return co

    def __add__(self, other):
        return self.__add__sub__(other, True)

    def __sub__(self, other):
        return self.__add__sub__(other, False)

    def __str__(self):
        if self.covmat is None:
            cmStr = "CovMat(None)"
        else:
            cmStr = "CovMat({shape[0]}, {shape[1]})".format(shape=self.covmat.shape)
        if self._index is None:
            ixStr = "Index(None)"
            valStr = ""
        else:
            ixStr = "Index(" + ", ".join(["{0}".format(i) for i in self._index]) + ")"
            valStr = "\nValues(" + ", ".join(["{0}".format(i) for i in self.getPointCovMatList()]) + ")"
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
    c1.covmat = cm
    c1.setCovMatIndex((0, 1, 2))
    print(c1)

    print('getPointCovmat')
    cm = numpy.array([[1, 0, 0.1, 0.5], [0, 2, 0.2, 0.6], [0, 0, 2.5, 0.1], [0, 0, 0, 1]])
    c2 = PointLocalCovMat("P2", x=100, y=200)
    try:
        print(c1.getPointCovMat())
    except Exception as e:
        print(e.message)
    c2.covmat = cm
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
    c3.covmat = cm
    c3.setCovMatIndex((0, 1, 2))

    add = c1 + c3
    sub = c1 - c3
    add.id = "add"
    print(add)
    print(sub)
    print(c1)
    print(c3)
    #sub = c1 - c2

    #add.textTable = coor_cov_table()
    #sub.textTable = coor_cov_table()

    #print add
    #print sub

    ## multiplication with scalar
    #print "multiplication"
    #print c2 * 2.0

    ## xy and z points
    #c3 = PointCartCovMat("XY", x=10, y=20)
    #c3.var = (1, 2)
    #c3.cov = (0.5)
    #print c3
    #print c3.make_gama_xml()

    #c4 = PointCartCovMat("Z", z=30)
    #c4.varz = 1
    #print c4
    #print c4.make_gama_xml()

    ## transforms
    #print "Transformation"
    #from gizela.tran.Tran2D import Tran2D
    #tr = Tran2D()

    #import math
    #om = 30 * math.pi / 180
    #tr.rotation_(om)
    #c4 = PointCartCovMat("C4", x=2, y=0)
    #c4.var = (0.2,0.1)
    #print c4
    #print c4.covmat.data
    #ellipse = c4.errEll
    #print "a=", ellipse[0], "b=", ellipse[1], "om=", ellipse[2]*180/math.pi

    #fig = FigureLayoutErrEll(figScale=0.05)
    #c4.plot_(fig)
    #c4.plot_error_ellipse(fig)
    #fig.set_aspect_equal()

    #c4.tran_(tr)
    #c4.id = c4.id + " tran"

    #print c4
    #print c4.covmat.data
    #ellipse = c4.errEll
    #print "a=", ellipse[0], "b=", ellipse[1], "om=", ellipse[2]*180/math.pi

    #c4.plot_(fig)
    #c4.plot_error_ellipse(fig)

    #fig.show_()
