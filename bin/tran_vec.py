#!/usr/bin/python

'''
Script for transformation of vectors to local system 
'''

# $Id: tran_vec.py 76 2010-10-22 21:19:21Z tomaskubin $

import sys
#from gizela.stat.CompareObs import CompareObs

# nacteni vstupnich parametru
from optparse import OptionParser
usage = "usage: %prog [options] < file1"
version = "%prog $Revision: 76 $"
parser = OptionParser(usage=usage, version=version)
parser.add_option("", "--cpoint", action="store", type="string", 
            dest="central_point", 
            help="Set central point latitude and longitude in degrees --cpoint=50.01,14.2")

(options, args) = parser.parse_args();

# read data
from gizela.data.GamaLocalDataObs import GamaLocalDataObs
obs1 = GamaLocalDataObs()
obs1.parse_file(sys.stdin)
#print >>sys.stderr, obs1.stdev

# set central point
if options.central_point is None:
    print >>sys.stderr, "No central point set."
    sys.exit(1)

cpoint = options.central_point.split(",")

if len(cpoint) != 2:
    print >>sys.stderr, "Cannot read central point: %s" % options.central_point
    sys.exit(1)

print >>sys.stderr, "Local system: Central point: lat=%s, lon=%s deg" %\
                            (cpoint[0], cpoint[1])


from gizela.util.Converter import Converter
lat = Converter.deg2rad_(float(cpoint[0]))
lon = Converter.deg2rad_(float(cpoint[1]))

obs1.centralPointGeo.lat=lat 
obs1.centralPointGeo.lon=lon 

#print >>sys.stderr, obs1.coordSystemLocal

# transform vector to local system
obs1.tran_vec_local_ne()
obs1.set_axes_ori("ne")

# write gama xml to stdout
print >>sys.stdout, obs1.make_gama_xml()

