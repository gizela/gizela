#!/usr/bin/python

'''
Script for comparison of observations 
    comparison of vectors

'''

# $Id: compare_obs.py 76 2010-10-22 21:19:21Z tomaskubin $

import sys
from gizela.stat.CompareObs import CompareObs

# nacteni vstupnich parametru
from optparse import OptionParser
usage = "usage: %prog [options] file1 file2"
version = "%prog $Rev: 76 $"
parser = OptionParser(usage=usage, version=version)
parser.add_option("", "--vec", action="store_true", dest="vec", 
            default=False,
            help="Compare vectors")

parser.add_option("", "--vecl", action="store_true", dest="vecl",
            default=False,
            help="Compare vectors transformed to local system using --cpoint")

#parser.add_option("", "--all", action="store_true", dest="all",
#        help="Compare all type of observations")

parser.add_option("", "--cpoint", action="store", type="string", 
            dest="central_point",
            help="Set central point latitude and longitude in degrees --cpoint=50.01,14.2")

parser.add_option("", "--mean", action="store_true", dest="mean",
            default=False,
            help="Compute mean value of repeated observations before comparison")


(options, args) = parser.parse_args();

if len(args) != 2:
    print >>sys.stderr, usage
    sys.exit(1)

# open files
try:
    file1 = open(args[0])
except Exception, e:
    print >>sys.stderr, e
    sys.exit(1)

try:
    file2 = open(args[1])
except Exception, e:
    print >>sys.stderr, e
    sys.exit(1)

# read data
from gizela.data.GamaLocalDataObs import GamaLocalDataObs
obs1 = GamaLocalDataObs()
obs2 = GamaLocalDataObs()
obs1.parse_file(file1)
obs2.parse_file(file2)

# set central point
if options.central_point is not None:
    cpoint = options.central_point.split(",")

    if len(cpoint) is not 2:
        print >>sys.stderr, "Cannot read central point: %s" % \
                options.central_point
        sys.exit(1)

    print >>sys.stderr, "Local system: Central point: lat=%s, lon=%s deg" %\
                                (cpoint[0], cpoint[1])

    from gizela.util.Converter import Converter
    lat = Converter.deg2rad_(float(cpoint[0]))
    lon = Converter.deg2rad_(float(cpoint[1]))

    obs1.centralPointGeo.lat=lat 
    obs1.centralPointGeo.lon=lon 
    obs2.centralPointGeo.lat=lat 
    obs2.centralPointGeo.lon=lon 

# transform vector to local system
if options.vecl and options.central_point:
    obs1.tran_vec_local_ne()
    obs1.set_axes_ori("ne")
    #print obs1.make_gama_xml()
    
    obs2.tran_vec_local_ne()
    obs2.set_axes_ori("ne")
    #print obs2.make_gama_xml()
    print >>sys.stderr, "Transformation of vectors done."

# compare observations
from gizela.stat.CompareObs import CompareObs
cmp = CompareObs(obs1, obs2)
if options.vec or options.vecl:
    # compare vectors
    cmp.compare_vector(mean=options.mean)

# print results
print cmp.str_summary()
print cmp.str_compared()
print cmp.str_uncompared()
if options.mean:
    print cmp.str_mean()
