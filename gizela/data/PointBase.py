# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>


from gizela.util.Error import Error


class PointBaseError(Error):
    pass


class PointBase(object):
    '''base class for geodetic points
    '''

    def __init__(self, id):
        """id - string - point identification
        """
        self.id = id

    def __str__(self):
        return 'PointBase id="{0}"'.format(self.id)

    def __eq__(self, other):
        if isinstance(other, PointBase):
            return self.id == other.id
        else:
            return self.id == other

    def formatGamaXML(self):
        return '<point id="{self.id}" />'.format(self=self)

if __name__ == "__main__":

    p = PointBase("A")
    p2 = PointBase("B")
    print(p)
    print(p.formatGamaXML())

    print(p == p)
    print(p == "A")
    print(p == p2)
    print(p == "B")
