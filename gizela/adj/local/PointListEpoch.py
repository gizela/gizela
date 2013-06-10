# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>

'''
class for list of point lists with dictionary for searching by point id

PointListEpoch.list = [ PointList instance:
                                list = [<Point id="A", x, y, z>,
                                        <Point id="B", x, y, z>,<-o
                                        <Point id="C", x, y, z>,  |
                                        ...                       |
                                       ]                          |
                         PointList instance:                      |
                                list = [<Point id="B", x, y, z>,<-|--o
                                        <Point id="C", x, y, z>,  |  |
                                        ...                       |  |
                                       ]                          |  |
                             ...               o------------------o  |
                      ]                        |  o------------------o
                                               |  |
                                               v  v
PointListEpoch.index = { "A": [0, None], "B": [1, 0], "C": [2, 1], ...}
'''


from gizela.util.Error import Error
from gizela.adj.local.PointList import PointList


class PointListEpochError(Error):
    pass


class PointListEpoch(object):
    """
    List of PointList instances with
    index - dictionary of ids for searching
    """

    def __init__(self):

        self.index = {}        # dictionary id: list index
        self.list = []        # list of pointList instances

        #self.sortOutput = sortOutput  # sort points by id in text output?

    def addEpoch(self, epoch):
        '''adds PointList instance into list of epoch'''
        if not isinstance(epoch, PointList):
            raise PointListEpochError("Requires PointList instance")

        # add pointList to list
        self.list.append(epoch)

        # add None to all point in index
        for id in self.index:
            self.index[id].append(None)

        # add indexes to points
        for id in epoch.index:
            if id in self.index:
                self.index[id][-1] = epoch.index[id]
            else:
                self.index[id] = [None for i in range(len(self.list))]
                self.index[id][-1] = epoch.index[id]

    #def add_multiple_epoch(self, mepoch, reString, epochIndex, pointIndex):
    #    """
    #    add pointList (mepoch)  with more than one epoch and create index
    #    for all epoch inclusded by point id and regular expression

    #    use: for separating joined adjustment of multiple epochs

    #    mepoch: PointList object with multiple epochs
    #    reString: regular expression with two groups - point id,
    #                                                 - epoch index from 0
    #    epochIndex: index of epoch number (0 or 1) in regular expression groups
    #    pointIndex: index of point id (0 or 1) in regular expression groups
    #    """
    #    import re

    #    try:
    #        patt = re.compile(reString)
    #    except:
    #        raise EpochPointListError, "Error compiling regular expression"

    #    for point in epoch.pointListFix:
    #        grp = patt.search(point.id)
    #        if grp is not None:
    #            if len(grp) == 2:
    #                id = grp[pointIndex]
    #                ei = grp[epochIndex]

    def getEpoch(self, index):
        '''returns PointList instance'''
        try:
            return self.list[index]
        except IndexError:
            raise PointListEpochError("Unknown epoch {0}".format(index))

    def iterPoint(self, id):
        "returns point instance generator through epochs"
        if id in self.index:
            for i in range(len(self.list)):
                ind = self.index[id][i]
                if ind is None:
                    #yield self.list[i].list[0].__class__(None)
                    yield None
                else:
                    yield self.list[i].list[ind]

        else:
            raise PointListEpochError("Unknown point id='{0}'".format(id))

    def iterEpoch(self):
        "iterator for epoch - return PointList instances"
        for e in self.list:
            yield e

    def __iter__(self):
        """
        iterator through points
        returns generator of generators of points in epoch
        """

        #return iter(self.index)
        for id in self.index:
            yield self.iterPoint(id)

    def iterPointId(self):
        """
        returns key-iterator of ids of points
        """
        return iter(self.index)

    def getNumPoint(self):
        "returns the number of points"
        return len(self.index)

    def getNumEpoch(self):
        "returns the number of epochs"
        return len(self.list)

    def __str__(self):
        return "\n".join(["Epoch index = {0}\n".format(i) + self.list[i].__str__() for i in range(self.getNumEpoch())])


if __name__ == "__main__":

    from gizela.adj.local.PointLocalCovMat import PointLocalCovMat
    from gizela.adj.local.POINT_LOCAL_STATUS import POINT_LOCAL_STATUS
    from gizela.adj.local.PointListCovMat import PointListCovMat
    import numpy
    c1 = PointLocalCovMat("C1", x=10, y=20, z=30, status=POINT_LOCAL_STATUS.adj)
    c2 = PointLocalCovMat("C2", x=100, y=200, status=POINT_LOCAL_STATUS.adj)
    c3 = PointLocalCovMat("C3", z=3000, status=POINT_LOCAL_STATUS.adj)
    pl1 = PointListCovMat()
    pl1.addPoint(c1)
    pl1.addPoint(c2)
    pl1.addPoint(c3)
    cm = numpy.array([[1, 0.1, 0.1, 0.1, 0.1, 0.1],
                      [0, 2,   0.2, 0.2, 0.2, 0.2],
                      [0, 0,   3,   0.3, 0.3, 0.3],
                      [0, 0,   0,   4,   0.4, 0.4],
                      [0, 0,   0,   0,   5,   0.5],
                      [0, 0,   0,   0,   0,   6]])
    pl1.setCovMat(cm)

    pl2 = PointListCovMat()
    pl2.addPoint(c1)
    pl2.addPoint(c3)
    pl2.setCovMat(cm)

    ple = PointListEpoch()
    ple.addEpoch(pl1)
    ple.addEpoch(pl2)
    print(ple)

    print("Number of points: {0}".format(ple.getNumPoint()))
    print("Number of epochs: {0}".format(ple.getNumEpoch()))

    print("Iter Point within epochs")
    for point in ple.iterPoint('C2'):
        print(point)
