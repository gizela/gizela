# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>
#


class POINT_LOCAL_STATUS:
    ''' enumeration type for coordinates status '''
    unused = 0
    fix = 1     # fixed all coordinates
    adj = 2     # adjusted all coodinates
    con = 3     # constrained all coordinates
    con_xy = 4  # constrained only x and y coordinates (z is adjusted)
    con_z = 5   # constrained only z coordinates (x and y are adjusted)
