# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>
#

from gizela.util.Error import Error
import datetime


class NetworkAdjError(Error):
    pass


class NetworkAdj(object):
    """
    base class for local geodetic network
    adjusted values
    """

    def __init__(self):
        self.coordSystem = {"ellipsoid": "wgs84",
                            "axesOri": "en",
                            "bearingOri": "right-handed",
                            "name": "default",
                            "description": "default coordinate system"}

        # date and time of measurement
        self.dateTime = datetime.datetime(1900, 1, 1)

        #import ConfigParser
        #self.configParser = ConfigParser.SafeConfigParser()
        #self.configParser.optionxform = str
            # to make options case sensitive

        self.stdev = {"apriori": None,
                      "aposteriori": None,
                      "used": "apriori",
                      "probability": 0.95}

        # point list of FIXED POINTS
        #self.pointListFix = PointList()
        self.pointListFix = None

        # point list of ADJUSTED POINTS
        # point list of adjusted/constrained points with covariance matrix
        #self.pointListAdjCovMat =\
        #        PointListCovMat(covmat=CovMatApri(useApriori=self._useApriori),
        #                        textTable=gama_coor_stdev_table())
        self.pointListAdj = None



            # try to parse description string
            #import StringIO
            #try:
            #    # handle character % in description
            #    data.description = data.description.replace("%","%%")
            #    #import sys
            #    #print >>sys.stderr, "Description:", data.description
            #    self.configParser.readfp(StringIO.StringIO(data.description))
            #except Exception, e:
            #    import sys
            #    print >>sys.stderr, "Warning: Description not parsed"
            #    print >>sys.stderr, "Description: %s" % data.description
            #    print >>sys.stderr, "Error: %s" % e

            #    # create section epoch
            #    self.configParser.add_section("epoch")
            #    # set option description
            #    self.configParser.set("epoch", "description", data.description)

            #else:
            #    self.set_date_time_list()
            #        # sets date and time according to configParser

            # set stdev

            # check axes and bearing orientation
            #if self.coordSystemLocal.axesOri != data.param["axes-xy"]:
            #    import sys
            #    print >>sys.stderr, "Axes orientation is different (%s, %s)"\
            #        % (self.coordSystemLocal.axesOri, data.param["axes-xy"])

            #if self.coordSystemLocal.bearingOri != data.param["angles"]:
            #    import sys
            #    print >>sys.stderr, "Bearing orientation is different (%s, %s)"\
            #        % (self.coordSystemLocal.bearingOri, data.param["angles"])

            #ax = AxesOrientation(axesOri=data.param["axes-xy"],
            #                     bearingOri=data.param["angles"])
            #if not ax.is_consistent():
            #    raise NetworkError, \
            #            "Coordinate system of data is not consistent"



    #def set_date_time_string(self, dateTimeStr):
    #    """
    #    sets dateTimeList according to dateTimeStr

    #    dateTimeStr: string: string with date and time in format
    #                         yyyy.mm.dd.hh.mm.ss.microseconds
    #    """

    #    import datetime

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
    pass
