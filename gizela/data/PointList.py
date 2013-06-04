# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>

'''
class for list of points with dictionary for searching by point id

PointList.list = [<Point id="A", x, y, z>,
                  <Point id="B", x, y, z>,
                  <Point id="C", x, y, z>, <--o
                  ...]       |_______     ____|
                                     |   |
PointList.index = { "A": 0, "B": 1, "C": 2, ...}
'''


from gizela.util.Error import Error
from gizela.data.PointBase import PointBase
from gizela.data.DUPLICATE_ID import DUPLICATE_ID


class PointListError(Error):
    pass


class PointList(object):
    """List of geodetic points CoordBase"""

    def __init__(self, duplicateId=DUPLICATE_ID.error, sort=False):
        '''
        duplicateId ... what to do with duplicit id of point
        sort   ... sort output by id?
        '''

        self.index = {}         # dictionary id: list index
        self.list = []          # list of points
        self.duplicateId = duplicateId
        self.sortOutput = sort  # sort output?

    def setSort(self):
        self.sortOutput = True

    def unsetSort(self):
        self.sortOutput = False

    def addPoint(self, point):
        '''
        adds PointBase instance into list
        '''
        if not isinstance(point, PointBase):
            raise PointListError("Requires PointBase or its inheritance")

        # handle duplicateId
        id = point.id
        if id in self.index:
            if self.duplicateId == DUPLICATE_ID.hold:
                "hold old point"
                pass
            elif self.duplicateId == DUPLICATE_ID.overwrite:
                "owerwrite old poitn with the new one"
                self.list[self.index[id]] = point
            elif self.duplicateId == DUPLICATE_ID.error:
                "raise exception"
                raise PointListError("Duplicit point id '{0}'".format(id))

            elif self.duplicateId == DUPLICATE_ID.compare:
                "compare coordinates: raise error when differs"
                p = self.list[self.index[id]]
                if p != point:
                    raise PointListError("Point '{0}' differs with point allready in list".format(id))
            else:
                raise PointListError("Unsupported DUPLICATE_ID value '{0}'".format(self.duplicateId))

        else:
            index = len(self.list)
            self.index[id] = index
            point.lindex = index
            self.list.append(point)

    def replacePoint(self, point):
        """
        replace existing point with new point
        """
        if point.id not in self.index:
            raise PointListError("Error replacing point id='{0}'".format(point.id))
        ind = self.index[point.id]
        self.list[ind] = point

    def getPoint(self, id):
        '''returns PointBase instance'''
        try:
            return self.list[self.index[id]]
        except KeyError:
            raise PointListError("Unknown point id='{0}'".format(id))

    def del_point(self, id):
        """deltes point from poitList"""

        # delete: 1. remove key from self.index dictionary
        #         2. replace point in self.list list with None

        try:
            ind = self.index.pop(id)
            #self.list[ind] = self.list[ind].__class__(id=None)
            self.list[ind] = None
        except KeyError:
            raise PointListError("Point id='{0}' does not exist".format(id))

    def __len__(self):
        '''number of points in dictionary'''
        return sum([1 for i in self.list if i is not None])

    def __iter__(self):
        """point generator"""
        for p in self.list:
            if p is not None:
                yield p

    def iterId(self):
        """iterator throught id"""
        return iter(self.index)

    def extend(self, other):
        """
        extends with other PointList
        """
        if not isinstance(other, PointList):
            raise PointListError("PointList instance expected")

        for point in other:
            self.addPoint(point)

    def __str__(self):
        return "\n".join(["{0}".format(point) for point in self])

    def updatePoint(self, point):
        """
        update point if point exists
        otherwise add new point
        """
        if point.id in self.iterId():
            p = self.getPoint(point.id)
            p.update(point)
        else:
            self.addPoint(point)


if __name__ == "__main__":

    from gizela.data.PointLocal import PointLocal

    c1 = PointLocal(id="C", x=1, y=2, z=3)
    c2 = PointLocal(id="B", x=4, y=5, z=6)

    pd = PointList()

    print(pd)

    pd.addPoint(c1)
    pd.addPoint(c2)
    pd.addPoint(PointLocal(id="A", x=7, y=8, z=9))
    pd.addPoint(PointLocal(id="AA", x=7, y=8, z=9))

    print(pd)
    print(pd.getPoint("A"))
    print("C" in pd)
    print("c" in pd)
    for point in pd:
        print(point)

    #delete
    print("delete point A")
    pd.del_point("A")
    print(pd)
    for id in pd.iterId():
        print(id)
    for p in pd:
        print(p)

    # sort
    print("sort")
    pd.setSort()
    print(pd)
    pd.unsetSort()

    # duplicateId
    pd.duplicateId = DUPLICATE_ID.overwrite
    pd.addPoint(PointLocal(id="C", x=10, y=20, z=30))
    pd.duplicateId = DUPLICATE_ID.hold
    pd.addPoint(PointLocal(id="AA", x=70, y=80, z=90))
    print(pd)

    # adding
    print("adding")
    pd2 = PointList()
    pd2.addPoint(PointLocal(id="AB", x=0, y=5, z=30))
    pd2.addPoint(PointLocal(id="BB", x=10, y=10, z=30))
    pd2.extend(pd)
    print(pd)
    print(pd2)

    # test of coordinates update
    from gizela.data.POINT_LOCAL_STATUS import POINT_LOCAL_STATUS
    point1 = PointLocal(id="A", x=1, y=2, status=POINT_LOCAL_STATUS.fix)
    point2 = PointLocal(id="B", x=100, y=200, status=POINT_LOCAL_STATUS.adj)
    point3 = PointLocal(id="A", x=10, y=20, status=POINT_LOCAL_STATUS.adj)
    pl = PointList()
    pl.addPoint(point1)
    p = pl.getPoint(id="A")
    p.x = 10
    print(pl)

    pl.updatePoint(point2)
    print(pl)
    pl.updatePoint(point3)
    print(pl)
