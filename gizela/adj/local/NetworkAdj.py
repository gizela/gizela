# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>

from gizela.util.Error import Error
from gizela.adj.local.PointList import PointList
from gizela.adj.local.PointListCovMat import PointListCovMat
import configparser
#from gizela.adj.local.PointLocal import PointLocal
#from gizela.adj.geodetic.PointGeodetic import PointGeodetic
#import datetime


class NetworkAdjError(Error):
    pass


class NetworkAdj(object):
    """
    base class for local geodetic network
    adjusted values
    """

    def __init__(self):
        # coordinate system

        self.config = configparser.ConfigParser()  # configuration parameters of network
        #self._setDateTime()
        #self._setCentralPoint()

        # point list of FIXED POINTS
        self.pointListFix = PointList()

        # point list of ADJUSTED POINTS
        self.pointListAdj = PointListCovMat()

    def parseConfigFile(self, file):
        """
        parses configuration from file with ConfigParser
        file: file like object
        """
        self.config = configparser.ConfigParser()
        try:
            self.config.read_file(file)
        except Exception as e:
            raise NetworkAdjError("Error: configparser: {0}".format(e.message))

    def parseConfigString(self, string):
        "parses string with configuration"
        self.config = configparser.ConfigParser()
        try:
            self.config.read_string(string)
        except Exception as e:
            raise NetworkAdjError("Error: configparser: {0}".format(e.message))

    def __str__(self):
        str = ["Adjusted Local Network",
               "----------------------"]
        str.append("Epoch:")
        str.append("  date: {0}".format(self.config.get('epoch', 'date', fallback="")))
        str.append("  time: {0}".format(self.config.get('epoch', 'time', fallback="")))
        str.append("  description: {0}".format(self.config.get('epoch', 'description', fallback="")))
        str.append("Local Coordinate System:")
        str.append("  name: {0}".format(self.config.get('local-coordinate-sytem', 'name', fallback="")))
        str.append("  description: {0}".format(self.config.get('local-coordinate-sytem', 'description', fallback="")))
        str.append("  ellipsoid code: {0}".format(self.config.get('local-coordinate-sytem', 'ellipsoid-code', fallback="")))
        str.append("  axes orientation: {0}".format(self.config.get('local-coordinate-sytem', 'axes-ori', fallback="")))
        str.append("  bearing orientation: {0}".format(self.config.get('local-coordinate-sytem', 'bearing-ori', fallback="")))
        str.append("  Central Point:")
        str.append("    x        : {0}".format(self.config.get('local-coordinate-sytem', 'central-point-x', fallback="")))
        str.append("    y        : {0}".format(self.config.get('local-coordinate-sytem', 'central-point-y', fallback="")))
        str.append("    z        : {0}".format(self.config.get('local-coordinate-sytem', 'central-point-z', fallback="")))
        str.append("    latitude : {0}".format(self.config.get('local-coordinate-sytem', 'central-point-lat', fallback="")))
        str.append("    longitude: {0}".format(self.config.get('local-coordinate-sytem', 'central-point-lon', fallback="")))
        str.append("    height   : {0}".format(self.config.get('local-coordinate-sytem', 'central-point-height', fallback="")))
        str.append("    elevation: {0}".format(self.config.get('local-coordinate-sytem', 'central-point-elevation', fallback="")))
        str.append("Statistic:")
        str.append("  confidence probability : {0}".format(self.config.get('statistic', 'confidence-probability', fallback="")))
        str.append("  standard deviation used: {0}".format(self.config.get('statistic', 'stdev-use', fallback="")))

        def idStr(pointList):
            pointIdStrList = []
            strTmp = ""
            for point in pointList:
                idString = "'{}'({})".format(point.id, point.getType())
                if len(strTmp) + len(idString) > 80:
                    if len(strTmp) > 0:
                        pointIdStrList.append(strTmp)
                        strTmp = ""
                if len(strTmp) != 0:
                    strTmp += ', '
                strTmp += idString
            pointIdStrList.append(strTmp)
            return "\n".join(pointIdStrList)

        str.append("Points Fixed:")
        str.append(idStr(self.pointListFix))
        str.append("Points Adjusted:")
        str.append(idStr(self.pointListAdj))
        return "\n".join(str)

    #def set_date_time_string(self, dateStr, timeStr=None):
    #    """
    #    sets date and time according to dateStr ant timeStr
    #    dateStr: yyyy.mm.dd
    #    timeStr: hh.mm.ss
    #    """
    #    to rewrite
    #    for date in dateTimeStr.split(" "):
    #        date = date.split(".")
    #        try:
    #            # one date in the form yyyy.mm.dd.hh.mm.ss.microseconds
    #            date = [int(i) for i in date]
    #        except:
    #            raise NetworkError, "Wrong date: %s" % date

    #        if len(date) == 1:
    #            self.dateTimeList.append(datetime.datetime(year=date[0]))
    #        elif len(date) == 2:
    #            self.dateTimeList.append(datetime.datetime(year=date[0],
    #                                               month=date[1]))
    #        elif len(date) == 3:
    #            self.dateTimeList.append(datetime.datetime(year=date[0],
    #                                               month=date[1],
    #                                               day=date[2]))
    #        elif len(date) == 4:
    #            self.dateTimeList.append(datetime.datetime(year=date[0],
    #                                               month=date[1],
    #                                               day=date[2],
    #                                               hour=date[3]))
    #        elif len(date) == 5:
    #            self.dateTimeList.append(datetime.datetime(year=date[0],
    #                                               month=date[1],
    #                                               day=date[2],
    #                                               hour=date[3],
    #                                               minute=date[4]))
    #        elif len(date) == 6:
    #            self.dateTimeList.append(datetime.datetime(year=date[0],
    #                                               month=date[1],
    #                                               day=date[2],
    #                                               hour=date[3],
    #                                               minute=date[4],
    #                                               second=date[5]))
    #        elif len(date) == 7:
    #            self.dateTimeList.append(datetime.datetime(year=date[0],
    #                                               month=date[1],
    #                                               day=date[2],
    #                                               hour=date[3],
    #                                               minute=date[4],
    #                                               second=date[5],
    #                                               microsecond=date[6]))
    #        else:
    #            raise NetworkError, "Wrong date: %s" % date

if __name__ == "__main__":
    net = NetworkAdj()
    iniString = """
[epoch]
date=1990.1.1
time=0.0
description=description of epoch

[local-coordinate-sytem]
name=default
description=default local coordinate system
ellipsoid-code=wgs84
axes-ori=en
bearing-ori=right-handed
central-point-x=0.0
central-point-y=0.0
central-point-z=0.0
central-point-lat=0.0
central-point-lon=0.0
central-point-height=0.0
central-point-elevation=0.0

[statistic]
confidence-probability=0.95
stdev-use=apriori
"""
    net.parseConfigString(iniString)

    # point lists
    from gizela.adj.local.PointLocal import PointLocal
    from gizela.adj.local.PointLocalCovMat import PointLocalCovMat
    from gizela.adj.local.POINT_LOCAL_STATUS import POINT_LOCAL_STATUS
    p1 = PointLocal(id="Point 1", z=10, status=POINT_LOCAL_STATUS.fix)
    p2 = PointLocal(id="Point 2", x=10, y=10, status=POINT_LOCAL_STATUS.fix)
    p3 = PointLocal(id="Point 3", x=10, y=10, z=10, status=POINT_LOCAL_STATUS.fix)
    p4 = PointLocalCovMat(id="Point 4", z=10, status=POINT_LOCAL_STATUS.adj)
    p5 = PointLocalCovMat(id="Point 5", x=10, y=10, status=POINT_LOCAL_STATUS.con)
    p6 = PointLocalCovMat(id="Point 6", x=10, y=10, z=10, status=POINT_LOCAL_STATUS.con_z)
    net.pointListFix.addPoint(p1)
    net.pointListFix.addPoint(p2)
    net.pointListFix.addPoint(p3)
    net.pointListAdj.addPoint(p4)
    net.pointListAdj.addPoint(p5)
    net.pointListAdj.addPoint(p6)

    print(net)
