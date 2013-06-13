# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>

from gizela.util.Error import Error
from gizela.adj.local.PointListEpoch import PointListEpoch
from gizela.adj.local.NetworkAdj import NetworkAdj


class NetworkAdjEpochError(Error):
    pass


class NetworkAdjEpoch(object):
    """
    object stores adjusted local networks in epochs
    """

    def __init__(self):
        self.epochList = []  # list of NetowrkAdj instances
        self.epochPointListFix = PointListEpoch()  # list of fixed points for all epochs
        self.epochPointListAdj = PointListEpoch()  # list of coordinates in epochs

    def addEpoch(self, epoch):
        """
        @param epoch: results of local geodetic network adjustment
        @type epoch: L{NetworkAdj}

        adds adjusted network into list
        """

        if not isinstance(epoch, NetworkAdj):
            raise NetworkAdjEpochError("Network instance expected")

        self.epochList.append(epoch)
        self.epochPointListFix.addEpoch(epoch.pointListFix)
        self.epochPointListAdj.addEpoch(epoch.pointListAdj)

    def __str__(self):
        """
        @return: returns information string about epochs
        @rtype: C{str}
        """
        str = []
        for idx, epoch in enumerate(self.epochList):
            str.append("Epoch index: {}".format(idx))
            str.append(epoch.__str__())
        return "\n\n".join(str)


if __name__ == "__main__":

    from gizela.adj.local.PointLocal import PointLocal
    from gizela.adj.local.PointLocalCovMat import PointLocalCovMat
    from gizela.adj.local.POINT_LOCAL_STATUS import POINT_LOCAL_STATUS

    # first epoch
    p1 = PointLocal(id="Point 1", z=10, status=POINT_LOCAL_STATUS.fix)
    p2 = PointLocal(id="Point 2", x=10, y=10, status=POINT_LOCAL_STATUS.fix)
    p3 = PointLocal(id="Point 3", x=10, y=10, z=10, status=POINT_LOCAL_STATUS.fix)
    p4 = PointLocalCovMat(id="Point 4", z=10, status=POINT_LOCAL_STATUS.adj)
    p5 = PointLocalCovMat(id="Point 5", x=10, y=10, status=POINT_LOCAL_STATUS.con)
    p6 = PointLocalCovMat(id="Point 6", x=10, y=10, z=10, status=POINT_LOCAL_STATUS.con_z)
    net1 = NetworkAdj()
    net1.pointListFix.addPoint(p1)
    net1.pointListFix.addPoint(p2)
    net1.pointListFix.addPoint(p3)
    net1.pointListAdj.addPoint(p4)
    net1.pointListAdj.addPoint(p5)
    net1.pointListAdj.addPoint(p6)

    # second epoch
    p1 = PointLocal(id="Point 1", z=10.1, status=POINT_LOCAL_STATUS.fix)
    p2 = PointLocal(id="Point 2", x=10.1, y=10.1, status=POINT_LOCAL_STATUS.fix)
    p3 = PointLocal(id="Point 3", x=10.1, y=10.1, z=10.1, status=POINT_LOCAL_STATUS.fix)
    p4 = PointLocalCovMat(id="Point 4", z=10.1, status=POINT_LOCAL_STATUS.adj)
    p5 = PointLocalCovMat(id="Point 5", x=10.1, y=10.1, status=POINT_LOCAL_STATUS.con)
    p6 = PointLocalCovMat(id="Point 7", x=10.1, y=10.1, z=10.1, status=POINT_LOCAL_STATUS.con_z)
    net2 = NetworkAdj()
    net2.pointListFix.addPoint(p1)
    net2.pointListFix.addPoint(p2)
    net2.pointListFix.addPoint(p3)
    net2.pointListAdj.addPoint(p4)
    net2.pointListAdj.addPoint(p5)
    net2.pointListAdj.addPoint(p6)

    epochs = NetworkAdjEpoch()
    epochs.addEpoch(net1)
    epochs.addEpoch(net2)

    print(epochs)
