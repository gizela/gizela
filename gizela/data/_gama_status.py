# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>
#


class DUPLICATE_ID(object):
def point_local_status_string(int):
    """returns string representation of coordinate status"""
    gama_coord_status_string={
    GamaCoordStatus.unused    : 'unused',
    GamaCoordStatus.fix_x      : 'fix_x',
    GamaCoordStatus.adj_x      : 'adj_x',
    GamaCoordStatus.con_x      : 'adj_X',
    GamaCoordStatus.fix_y      : 'fix_y',
    GamaCoordStatus.adj_y      : 'adj_y',
    GamaCoordStatus.adj_Y      : 'adj_Y',
    GamaCoordStatus.fix_z      : 'fix_z',
    GamaCoordStatus.adj_z      : 'adj_z',
    GamaCoordStatus.adj_Z      : 'adj_Z',
    GamaCoordStatus.fix_xy     : 'fix_xy',
    GamaCoordStatus.adj_xy     : 'adj_xy',
    GamaCoordStatus.adj_XY     : 'adj_XY',
    GamaCoordStatus.fix_xyz    : 'fix_xyz',
    GamaCoordStatus.adj_xyz    : 'adj_xyz',
    GamaCoordStatus.adj_XYz    : 'adj_XYz',
    GamaCoordStatus.adj_xyZ    : 'adj_xyZ',
    GamaCoordStatus.adj_XYZ    : 'adj_XYZ',
    }
    try:
        return PointLocalStatus[int]
    except KeyError:
        raise PointLocalStatusError("Unknown code of coordinate status: %i" % int)

#def point_local_status_xml_attr(int):
#    """returns attribute for gama xml tag <point/>"""
#    tag={
#    GamaCoordStatus.unused     : '',
#    GamaCoordStatus.fix_z      : 'fix="z"',
#    GamaCoordStatus.adj_z      : 'adj="z"',
#    GamaCoordStatus.adj_Z      : 'adj="Z"',
#    GamaCoordStatus.fix_xy     : 'fix="xy"',
#    GamaCoordStatus.adj_xy     : 'adj="xy"',
#    GamaCoordStatus.adj_XY     : 'adj="XY"',
#    GamaCoordStatus.fix_xyz    : 'fix="xyz"',
#    GamaCoordStatus.adj_xyz    : 'adj="xyz"',
#    GamaCoordStatus.adj_XYz    : 'adj="XYz"',
#    GamaCoordStatus.adj_xyZ    : 'adj="xyZ"',
#    GamaCoordStatus.adj_XYZ    : 'adj="XYZ"',
#    }
#    try:
#        return tag[int]
#    except KeyError:
#        raise GamaCoordStatusError("Unknown code of gama coord status xml tag: %i" % int)
#
#def gama_coord_status_attr_fix(val):
#    "returns GamaCoordStatus for attribute fix"
#    status={
#        'z'  : GamaCoordStatus.fix_z,
#        'xy' : GamaCoordStatus.fix_xy,
#        'xyz': GamaCoordStatus.fix_xyz
#        }
#
#    try:
#        return status[val.lower()]
#    except KeyError:
#        raise GamaCoordStatusError, "Unknown value for attribute fix"
#
#def gama_coord_status_attr_adj(val):
#    "returns GamaCoordStatus for attribute adj"
#    status={
#        'z'  : GamaCoordStatus.adj_z,
#        'xy' : GamaCoordStatus.adj_xy,
#        'xyz': GamaCoordStatus.adj_xyz,
#        'Z'  : GamaCoordStatus.adj_Z,
#        'XY' : GamaCoordStatus.adj_XY,
#        'XYZ': GamaCoordStatus.adj_XYZ,
#        'xyZ': GamaCoordStatus.adj_xyZ,
#        'XYz': GamaCoordStatus.adj_XYz
#        }
#
#    try:
#        return status[val]
#    except KeyError:
#        raise GamaCoordStatusError, "Unknown value for attribute fix"


def point_local_status(val):
    "returns PointLocalStatus for attribute"
    att = val.split("_")
    if len(att) != 2:
        raise GamaCoordStatusError, "Unknown attribute %s" % val
    if att[0] == "adj":
        return gama_coord_status_attr_adj(att[1])
    elif att[0] == "fix":
        return gama_coord_status_attr_fix(att[1])
    elif att[0] == "con":
        return gama_coord_status_attr_adj(att[1].upper())
    else:
        raise GamaCoordStatusError, "Unknown attribute %s" % val


def gama_coord_status_dim(status):
    "returns the number of coordinates"
    gama_coord_status_dim={
    GamaCoordStatus.unused  : 0,
    GamaCoordStatus.fix_x   : 1,
    GamaCoordStatus.adj_x   : 1,
    GamaCoordStatus.con_x   : 1,
    GamaCoordStatus.fix_y   : 1,
    GamaCoordStatus.adj_y   : 1,
    GamaCoordStatus.adj_Y   : 1,
    GamaCoordStatus.fix_z   : 1,
    GamaCoordStatus.adj_z   : 1,
    GamaCoordStatus.adj_Z   : 1,
    GamaCoordStatus.fix_xy  : 2,
    GamaCoordStatus.adj_xy  : 2,
    GamaCoordStatus.adj_XY  : 2,
    GamaCoordStatus.fix_xyz : 3,
    GamaCoordStatus.adj_xyz : 3,
    GamaCoordStatus.adj_XYz : 3,
    GamaCoordStatus.adj_xyZ : 3,
    GamaCoordStatus.adj_XYZ : 3,
    }

    try:
        return gama_coord_status_dim[status]
    except KeyError:
        raise GamaCoordStatusError, "Unknown status %s" % status


if __name__ == "__main__":
    cst = GamaCoordStatus.adj_XYz + GamaCoordStatus.ori
    print gama_coord_status_string(cst)

    try:
        cst = GamaCoordStatus.fix_x
        print gama_coord_status_string(cst)

    #except CoordStatusError, e:
    #    print "Error occured!"
    #    print e

    except Error, e:
        print "Error occured!"
        print e

    print gama_coord_status_xml_attr(GamaCoordStatus.fix_xyz)

    print gama_coord_status_attr_fix("XY")
    print gama_coord_status_attr_adj("XY")

    cst = GamaCoordStatus.fix_xyz
    print bool(cst & GamaCoordStatus.fix_xy)
    print bool(cst & GamaCoordStatus.con_xy)

    cst = GamaCoordStatus.adj_XY
    print bool(cst & GamaCoordStatus.adj_XYz)
    print bool(cst & GamaCoordStatus.adj_XYZ)
    print bool(cst & GamaCoordStatus.adj_xyZ)
    """enumeration class for handlig points with same id
    """

    error = 0      # raise exception for duplicate point id
    hold = 1       # hold old point
    overwrite = 2  # owerwrite old point with the new one
    compare = 3    # raise exception when coordinates are different
