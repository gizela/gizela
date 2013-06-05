# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>
#

from gizela.data.PointLocal import PointLocal
#from gizela.data.CovMat     import CovMat
from gizela.util.Error import Error
#from gizela.tran.Tran2D import Tran2D
#from gizela.tran.Tran3D import Tran3D
import numpy


class PointLocalCovMatError(Error):
    pass


class PointLocalCovMat(PointLocal):
    """
    class for geodetic coordinates x, y, z
    and its covariance matrix

    covariance matrix is numpy array
        upper triangular part is used only
    """

    def __init__(self, id, x=None, y=None, z=None, covmat=None, index=None):
        """x, y, z ... coordinates
        covmat ... covariance matrix
        index  ... (xi, yi, zi) indexes of rows in covariance matrix
        """

        super().__init__(id, x, y, z)

        self.covmat = covmat

        # indexes of rows/columns in covariance matrix
        if index is None:
            self.xi, self.yi, self.zi = None, None, None
        else:
            try:
                self.xi, self.yi, self.zi = index[0], index[1], index[2]
            except IndexError:
                raise PointLocalCovMatError("expected len(index) == 3")

    def _get_index(self):
        return [self.xi, self.yi, self.zi]

    def _set_index(self, index):
        if len(index) == 3:
            self.xi = index[0]; self.yi = index[1];
            self.zi = index[2]
        elif len(index) == 2:
            self.xi = index[0]; self.yi = index[1];
        elif len(index) == 1:
            self.zi = index[0]
        else:
            raise PointCartCovMatError,\
                    "Index (xi, yi, zi) or (xi, yi) or (zi,) expected"

    # covariance matrix index of rows/columns
    index = property(_get_index, _set_index)

    # setting of variance and covariance throught managed attributes
    #def _set_var_x(self, vx):
    #    if self.xi == None:
    #        raise PointCartCovMatError, "Variance index of x coordinate not defined"
    #    self.covmat[self.xi, vx)
    #def _set_var_y(self, vy):
    #    if self.yi == None:
    #        raise PointCartCovMatError, "Variance index of y coordinate not defined"
    #    self.covmat.set_var(self.yi, vy)
    #def _set_var_z(self, vz):
    #    if self.zi == None:
    #        raise PointCartCovMatError, "Variance index of z coordinate not defined"
    #    self.covmat.set_var(self.zi, vz)
    #def _set_cov_xy(self, cxy):
    #    if self.xi == None or self.yi == None:
    #        raise PointCartCovMatError, "Covariance index of coordinate x and y not defined"
    #    self.covmat.set_cov(self.xi, self.yi, cxy)
    #def _set_cov_xz(self, cxz):
    #    if self.xi == None or self.zi == None:
    #        raise PointCartCovMatError, "Covariance index of coordinate x and z not defined"
    #    self.covmat.set_cov(self.xi, self.zi, cxz)
    #def _set_cov_yz(self, cyz):
    #    if self.yi == None or self.zi == None:
    #        raise PointCartCovMatError, "Covariance index of coordinate y and z not defined"
    #    self.covmat.set_cov(self.yi, self.zi, cyz)

    #def _get_var_x(self):
    #    if self.xi == None:
    #        #raise PointCartCovMatError, "Variance of x coordinate not defined"
    #        return None
    #    return self.covmat.get_var(self.xi)

    #def _get_var_y(self):
    #    if self.yi == None:
    #        #raise PointCartCovMatError, "Variance of y coordinate not defined"
    #        return None
    #    return self.covmat.get_var(self.yi)

    #def _get_var_z(self):
    #    if self.zi == None:
    #        #raise PointCartCovMatError, "Variance of z coordinate not defined"
    #        return None
    #    return self.covmat.get_var(self.zi)

    #def _get_cov_xy(self):
    #    if self.xi == None or self.yi == None:
    #        return None
    #        #raise PointCartCovMatError, "Covariance of coordinate x and y not defined"
    #    return self.covmat.get_cov(self.xi, self.yi)

    #def _get_cov_xz(self):
    #    if self.xi == None or self.zi == None:
    #        return None
    #        #raise PointCartCovMatError, "Covariance of coordinate x and z not defined"
    #    return self.covmat.get_cov(self.xi, self.zi)

    #def _get_cov_yz(self):
    #    if self.yi == None or self.zi == None:
    #        return None
    #        #raise PointCartCovMatError, "Covariance of coordinate y and z not defined"
    #    return self.covmat.get_cov(self.yi, self.zi)

    #def _set_var(self, var):
    #    """
    #    sets all variances in covariance matrix

    #    var = (varx, vary, varz)
    #    or
    #    var = (varx, vary)
    #    """

    #    for i, v in zip((self.xi, self.yi, self.zi), var):
    #        if i == None:
    #            raise PointCartCovMatError, "Index for var %e not set" % v
    #        else:
    #            self.covmat.set_var(i, v)

    #def _set_cov(self, cov):
    #    """sets all covariances in covariance matrix
    #    cov = (cov_xy, cov_xz, cov_yz)
    #    """

    #    if type(cov) != tuple and type(cov) != list:
    #        cov = (cov,)

    #    for i, j, c in zip((self.xi, self.xi, self.yi),
    #            (self.yi, self.zi, self.zi), cov):
    #        if i == None or j == None:
    #            raise PointCartCovMatError, "Index for cov %e not set" % c
    #        else:
    #            self.covmat.set_cov(i, j, c)

    #def _get_var(self):
    #    """returns list with all variances var_x, var_y, var_z"""
    #    var = []
    #    for i in (self.xi, self.yi, self.zi):
    #        if i == None:
    #            #raise PointCartCovMatError, "variance not set"
    #            var.append(None)
    #        else:
    #            var.append(self.covmat.get_var(i))
    #    return var

    #def _get_stdev(self):
    #    """returns list with all standard deviations  - sqrt(var)"""
    #    from math import sqrt
    #    return [(var==None and [None] or [sqrt(var)])[0] for var in self._get_var()]

    #def _get_stdev_x(self):
    #    var = self._get_var_x()
    #    if var == None:
    #        return None
    #    else:
    #        from math import sqrt
    #        return sqrt(var)


    #def _get_stdev_y(self):
    #    var = self._get_var_y()
    #    if var == None:
    #        return None
    #    else:
    #        from math import sqrt
    #        return sqrt(var)


    #def _get_stdev_z(self):
    #    var = self._get_var_z()
    #    if var == None:
    #        return None
    #    else:
    #        from math import sqrt
    #        return sqrt(var)


    #def _get_cov(self):
    #    cov = []
    #    for i,j in ((self.xi, self.yi),\
    #            (self.xi, self.zi),\
    #            (self.yi, self.zi)):
    #        if i == None or j == None:
    #            #raise PointCartCovMatError, "covariance not set"
    #            cov.append(None)
    #        else:
    #            #print "i:%i j:%i" %(i,j)
    #            #yield self.covmat.get_cov(i,j)
    #            cov.append(self.covmat.get_cov(i,j))
    #    return cov

    #var    = property(_get_var,    _set_var)
    #cov    = property(_get_cov,    _set_cov)
    #stdev  = property(_get_stdev)
    #varx  = property(_get_var_x,  _set_var_x)
    #vary  = property(_get_var_y,  _set_var_y)
    #varz  = property(_get_var_z,  _set_var_z)
    #covxy = property(_get_cov_xy, _set_cov_xy)
    #covxz = property(_get_cov_xz, _set_cov_xz)
    #covyz = property(_get_cov_yz, _set_cov_yz)
    #stdevx = property(_get_stdev_x)
    #stdevy = property(_get_stdev_y)
    #stdevz = property(_get_stdev_z)

    def _get_err_ell(self):
        """
        returns parameters of standard error ellipse
        (a, b, omega)
        omega ... clockwise from x axis in radians in interval -pi:pi
        """
        if self.x == None or self.y == None:
            raise PointCartCovMatError, "Point id=%s: No x, y coordinates set"\
                   % self.id

        vx = self.varx
        vy = self.vary
        cxy = self.covxy
        if vx == None:
            raise PointCartCovMatError, "Point id=%s: No varx set" % self.id
        if vy == None:
            raise PointCartCovMatError, "Point id=%s: No vary set" % self.id
        if cxy == None:
            raise PointCartCovMatError, "Point id=%s: No covariance xy set" \
                    % self.id

        # test of positive definity
        det = vx*vy - cxy*cxy
        if det < -1e-4:
            raise PointCartCovMatError, "Covariance matrix is not positive definite: det = %e" % det

        import math
        c = math.sqrt((vx - vy)**2 + 4.0*cxy*cxy)
        a = math.sqrt((vx + vy + c)/2.0)
        if vx + vy - c < 0.0:
            b = 0.0
        else:
            b = math.sqrt((vx + vy - c)/2.0)
        omega = math.atan2(2.0*cxy, vx - vy)/2.0

        return [a, b, omega]

    errEll = property(_get_err_ell)


    def get_point_cov_mat(self, dim=3):
        '''
        returns covariance matrix
        selection of covariance matrix of point from large covariance matrix

        dim: dimension of covariance matrix to be returned
        '''

        if dim > 3 or dim < 1:
            raise PointCartCovMatError, "Wrong dimension of covariance matrix."

        if self.covmat.dim == dim:
            return self.covmat

        lcm = self.covmat.empty_copy()
        lcm.dim = dim
        lcm.band = dim - 1 < self.covmat.band and dim - 1 or self.covmat.band

        var = self.var; cov = self.cov

        for i,v in enumerate(var[:dim]):
            if v != None: lcm.set_var(i,v)

        if dim > 1:
            if cov[0] != None: lcm.set_cov(0,1,cov[0])
        if dim > 2:
            if cov[1] != None: lcm.set_cov(0,2,cov[1])
            if cov[2] != None: lcm.set_cov(1,2,cov[2])

        #import sys
        #print >>sys.stderr, "get_point_cov_mat:", self.covmat, lcm

        return lcm

    def set_point_cov_mat(self, covmat):
        """
        sets covariance matrix of point

        covmat: CovMat instance with proper dimension
        """
        dim = self.get_dim()
        if dim != covmat.dim:
            raise PointCartCovMatError,\
                    "Wrong dimension of covariance matrix (%i != %i)" \
                        % (dim, covmat.dim)

        i = 0
        if self.x == None: self.xi = None
        else: self.xi = i; i += 1
        if self.y == None: self.yi = None
        else: self.yi = i; i += 1
        if self.z == None: self.zi = None
        else: self.zi = i

        self.covmat = covmat

    def __add__(self, other):
        '''addition of two points with covariance matrix'''

        if not isinstance(other, PointCartCovMat):
            raise PointCartCovMatError, \
                "Addition of two PointCartCovMat instances supported"

        x, y, z = None, None, None
        if self.x != None and other.x != None: x = self.x + other.x
        if self.y != None and other.y != None: y = self.y + other.y
        if self.z != None and other.z != None: z = self.z + other.z

        #id = " ".join([self.id, "+", other.id])
        #co = PointCartCovMat(id=self.id, x=x, y=y, z=z, textTable=self.textTable)

        # covariance matrix
        if self.covmat.dim == 3:
            lcm = self.covmat
        else:
            lcm = self.get_point_cov_mat()

        if other.covmat.dim == 3:
            ocm = other.covmat
        else:
            ocm = other.get_point_cov_mat()

        import copy
        p = copy.deepcopy(self)
        p.x = x; p.y = y; p.z = z; p.covmat = lcm + ocm
        if x == None: p.xi = None
        else: p.xi = 0
        if y == None: p.yi = None
        else: p.yi = 1
        if z == None: p.zi = None
        else: p.zi = 2
        return p

    def __sub__(self, other):
        '''subtraction of two points with covariance matrix'''

        if not isinstance(other, PointCartCovMat):
            raise PointCartCovMatError, \
                "Subtraction of two PointCartCovMat instances supported"

        x, y, z = None, None, None
        if self.x != None and other.x != None: x = self.x - other.x
        if self.y != None and other.y != None: y = self.y - other.y
        if self.z != None and other.z != None: z = self.z - other.z

        # covariance matrix
        if self.covmat.dim == 3:
            lcm = self.covmat
        else:
            lcm = self.get_point_cov_mat()

        if other.covmat.dim == 3:
            ocm = other.covmat
        else:
            ocm = other.get_point_cov_mat()

        import copy
        p = copy.deepcopy(self)
        p.x = x; p.y = y; p.z = z; p.covmat = lcm + ocm
        if x == None: p.xi = None
        else: p.xi = 0
        if y == None: p.yi = None
        else: p.yi = 1
        if z == None: p.zi = None
        else: p.zi = 2
        return p

    def __mul__(self, scalar):
        """
        returns multiplication of point coordinates with scalar
        """

        return super(PointCartCovMat, self).__mul__(scalar)

        # multiplication of variances and covariances
        var = self.var
        cov = self.cov
        for i in xrange(3):
            if var[i] is not None:
                var[i] *= scalar*scalar
            if cov[i] is not None:
                cov[i] *= scalar*scalar
        self.var = var
        self.cov = cov


if __name__ == "__main__":

    # empty point
    p = PointCartCovMat(None)
    print p
    print p.var
    print p.cov
    print p.stdev

    # regular point
    c1 = PointCartCovMat("P", x=10, y=20, z=30)
    c1.varx  =  0.1
    c1.vary  =  0.2
    c1.varz  =  0.3
    c1.covxy = -0.04
    c1.covxz = -0.05
    c1.covyz = -0.06

    print c1
    print c1.var
    print c1.stdev

    c1.textTable = TextTable([("id","%12s"), ("x","%11.3f"), ("y","%11.3f")], type="plain")
    print c1

    # output tables
    from gizela.data.point_text_table import *
    c1.textTable = coor_table()
    print c1

    c1.textTable = coor_stdev_table()
    print c1

    c1.textTable = coor_var_table()
    print c1

    c1.textTable = coor_cov_table()
    print c1

    print c1.make_gama_xml()

    # error ellipse
    print c1.errEll
    print c1.stdevz

    # graph
    from gizela.pyplot.FigureLayoutErrEll import FigureLayoutErrEll
    fig = FigureLayoutErrEll()
    c1.plot_(fig)
    c1.plot_error_ellipse(fig)
    c1.plot_error_z(fig)
    fig.set_aspect_equal()
    #fig.show_()

    # addition and subtraction of points
    c2 = PointCartCovMat("Q", x=10, y=20, z=30)
    c2.var = (1, 1, 1)
    c2.cov = (-1, -1, -1)

    add = c1 + c2
    sub = c1 - c2

    add.textTable = coor_cov_table()
    sub.textTable = coor_cov_table()

    print add
    print sub

    # multiplication with scalar
    print "multiplication"
    print c2 * 2.0

    # xy and z points
    c3 = PointCartCovMat("XY", x=10, y=20)
    c3.var = (1, 2)
    c3.cov = (0.5)
    print c3
    print c3.make_gama_xml()

    c4 = PointCartCovMat("Z", z=30)
    c4.varz = 1
    print c4
    print c4.make_gama_xml()

    # transforms
    print "Transformation"
    from gizela.tran.Tran2D import Tran2D
    tr = Tran2D()

    import math
    om = 30 * math.pi / 180
    tr.rotation_(om)
    c4 = PointCartCovMat("C4", x=2, y=0)
    c4.var = (0.2,0.1)
    print c4
    print c4.covmat.data
    ellipse = c4.errEll
    print "a=", ellipse[0], "b=", ellipse[1], "om=", ellipse[2]*180/math.pi

    fig = FigureLayoutErrEll(figScale=0.05)
    c4.plot_(fig)
    c4.plot_error_ellipse(fig)
    fig.set_aspect_equal()

    c4.tran_(tr)
    c4.id = c4.id + " tran"

    print c4
    print c4.covmat.data
    ellipse = c4.errEll
    print "a=", ellipse[0], "b=", ellipse[1], "om=", ellipse[2]*180/math.pi

    c4.plot_(fig)
    c4.plot_error_ellipse(fig)

    fig.show_()
