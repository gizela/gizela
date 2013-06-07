# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>
#

from gizela.util.Error import Error
from gizela.adj.local.PointBase import PointBase
from gizela.adj.local.POINT_LOCAL_STATUS import xmlAttribute


class PointLocalError(Error):
    pass


class PointLocal(PointBase):
    '''
    class for geodetic point with cartesian coordinates x, y, z
    '''

    def __init__(self, id, x=None, y=None, z=None, status=None):
        """
        id, coordinates x, y, z
        status ... status of point adjusted use POINT_LOCAL_STATUS class
        """

        super().__init__(id=id)
        self.x = x
        self.y = y
        self.z = z
        self.status = status

    def isSetXYZ(self):
        return self.x is not None and self.y is not None and self.z is not None

    def isSetXY(self):
        return self.x is not None and self.y is not None

    def isSetZ(self):
        return self.z is not None

    def isSetStatus(self):
        return self.status is not None

    def dim(self):
        return sum([1 for i in (self.x, self.y, self.z) if i is not None])

    def __str__(self):
        str = ['<point id="{self.id}"'.format(self=self)]
        if self.x is not None:
            str.append('x="{self.x:.4f}"'.format(self=self))
        if self.y is not None:
            str.append('y="{self.y:.4f}"'.format(self=self))
        if self.z is not None:
            str.append('z="{self.z:.4f}"'.format(self=self))
        if self.status is not None:
            str.append(xmlAttribute(self))
        str.append('/>')
        return " ".join(str)

    def __add__(self, other):
        "returns self + other"
        if not isinstance(other, PointLocal):
            raise PointLocalError("addition of two points is not supported")
        if self.dim() != other.dim():
            raise PointLocalError("Dimension of points are not equal {0}!={1}".
                                  format(self.dim(), other.dim()))

        x, y, z = None, None, None
        if self.x is not None and other.x is not None:
            x = self.x + other.x
        if self.y is not None and other.y is not None:
            y = self.y + other.y
        if self.z is not None and other.z is not None:
            z = self.z + other.z
        if self.status != other.status:
            raise PointLocalError("status of point is not the same ({0},{1})".
                                  format(self.status, other.status))

        import copy
        p = copy.deepcopy(self)
        p.x = x
        p.y = y
        p.z = z
        return p

    def __sub__(self, other):
        "returns self - other"
        if not isinstance(other, PointLocal):
            raise PointLocalError("subtraction of two points supported")

        x, y, z = None, None, None
        if self.x is not None and other.x is not None:
            x = self.x - other.x
        if self.y is not None and other.y is not None:
            y = self.y - other.y
        if self.z is not None and other.z is not None:
            z = self.z - other.z
        if self.status != other.status:
            raise PointLocalError("status of point is not the same ({0},{1})".
                                  format(self.status, other.status))

        import copy
        p = copy.deepcopy(self)
        p.x = x
        p.y = y
        p.z = z
        return p

    def __mul__(self, other):
        "returns multiplication of point coordinates with scalar"
        if type(other) != float and type(other) != int:
            raise PointLocalError("only multiplication with scalar supported")

        x, y, z = None, None, None
        if self.x is not None:
            x = self.x * other
        if self.y is not None:
            y = self.y * other
        if self.z is not None:
            z = self.z * other

        import copy
        p = copy.deepcopy(self)
        p.x = x
        p.y = y
        p.z = z
        return p

    def __eq__(self, other):
        "are points equal?"
        if other is None:
            # Point with all Nones
            return self.id is None and self.x is None and\
                self.y is None and self.z is None

        elif isinstance(other, PointLocal):
            # compare all coordinates and status
            return self.id == other.id and self.x == other.x and\
                self.y == other.y and self.z == other.z and\
                self.status == other.status

        elif type(other) is str or type(other) is unicode:
            # compare id
            return self.id == other

        else:
            raise PointLocalError("PointCart instance expected")

    def __ne__(self, other):
        return not self.__eq__(other)

    def update(self, other):
        """
        updates parameters of self from other
        """

        if not isinstance(other, PointLocal):
            raise PointLocalError("PointLocal instance expected")

        self.id = other.id
        self.x = other.x
        self.y = other.y
        self.z = other.z
        self.status = other.status


if __name__ == "__main__":
    from gizela.adj.local.POINT_LOCAL_STATUS import POINT_LOCAL_STATUS
    c1 = PointLocal(id="A", x=10, y=20, status=POINT_LOCAL_STATUS.fix)
    c2 = PointLocal(id="B", x=30, y=40, z=50, status=POINT_LOCAL_STATUS.con_xy)
    c2.z = 100
    print(c1)
    print(c2)

    # isSet
    print(c1.isSetXY())
    print(c1.isSetZ())
    print(c2.isSetXYZ())
    print(c2.isSetStatus())

    # udpate
    c3 = PointLocal(id="C")
    c3.update(c2)
    print(c3)

    # addition subtraction multiplying
    print(c2 * 2)
    print(c2 + c3)
    print(c2 - c3)
    try:
        c1 - c2
    except Exception as e:
        print(e)

    # comparison
    print(c1 == c2)
    print(c1 != c2)
    print(c1 == "A")
    print(c1 != "A")
    print("A" == c1)
