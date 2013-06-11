# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>

from gizela.adj.local.PointBase import PointBase
#from gizela.util.Converter import Converter


class PointGeodetic(PointBase):
    """
    Class for geodetic coordinates:
        latitude,
        longitude,
        height ellipsoidal,
        elevation (orthometric height)
        """

    def __init__(self, id, lat=None, lon=None, height=None, elevation=None):
        self.lat, self.lon = lat, lon
        self.height, self.elevation = height, elevation
        super().__init__(id)

    #def get_point_cart(self, ellipsoid):
    #    from gizela.data.PointLocal import PointLocal

    #    x, y, z = ellipsoid.llh2xyz_(self.lat, self.lon, self.height)
    #    return PointLocal(id=self.id, x=x, y=y, z=z)

    def __str__(self):
        str = '<point id="{self.id}"'.format(self=self)
        if self.lat is not None:
            str += ' latitude="{self.lat}"'.format(self=self)
        if self.lon is not None:
            str += ' longitude="{self.lon}"'.format(self=self)
        if self.height is not None:
            str += ' height="{self.height}"'.format(self=self)
        if self.elevation is not None:
            str += ' elevation="{self.elevation}"'.format(self=self)
        str += ">"
        return str


if __name__ == "__main__":

    c1 = PointGeodetic(id="A", lat=1, lon=2)
    c2 = PointGeodetic(id="A2", lat=1, lon=2, height=3, elevation=4)

    print(c1)
    print(c2)
