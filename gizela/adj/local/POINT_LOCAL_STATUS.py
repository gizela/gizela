# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>
#


class POINT_LOCAL_STATUS:
    ''' enumeration type for coordinates status '''
    #unused = 0
    fix = 0     # fixed all coordinates
    adj = 1     # adjusted all coodinates
    con = 2     # constrained all coordinates
    con_xy = 3  # constrained only x and y coordinates (z is adjusted)
    con_z = 4   # constrained only z coordinates (x and y are adjusted)

#def isConstrained(status):
#    return status == POINT_LOCAL_STATUS.con or status == POINT_LOCAL_STATUS.con_xy\
#            or status == POINT_LOCAL_STATUS.con_z


def xmlAttribute(point):
    strType = ['fix',
               'adj',
               'adj',
               'adj',
               'adj']
    if point.status is None:
        return ''
    attr = strType[point.status] + '="'
    if point.x is not None:
        if point.status == POINT_LOCAL_STATUS.con or point.status == POINT_LOCAL_STATUS.con_xy:
            attr += 'X'
        else:
            attr += 'x'
    if point.y is not None:
        if point.status == POINT_LOCAL_STATUS.con or point.status == POINT_LOCAL_STATUS.con_xy:
            attr += 'Y'
        else:
            attr += 'y'
    if point.z is not None:
        if point.status == POINT_LOCAL_STATUS.con or point.status == POINT_LOCAL_STATUS.con_z:
            attr += 'Z'
        else:
            attr += 'z'
    attr += '"'
    return attr

if __name__ == "__main__":
    from gizela.adj.local.PointLocal import PointLocal
    p1 = PointLocal(id="A", x=5000, y=1000, status=POINT_LOCAL_STATUS.fix)
    p2 = PointLocal(id="B", x=5000, y=1000, z=100, status=POINT_LOCAL_STATUS.con_z)
    p3 = PointLocal(id="C", x=5000, y=1000, z=100, status=POINT_LOCAL_STATUS.con_xy)
    print(xmlAttribute(p1))
    print(xmlAttribute(p2))
    print(xmlAttribute(p3))
