#!/usr/bin/python

'''
Script for testing displacement vectors 
Type of tests:  apriori (chi square distribution), 
		aposteriori (f distribution)


'''

# $Id: displacement_test.py 10 2010-04-20 12:23:33Z kubin $

import sys
from gizela.stat.Displacement import *

# nacteni vstupnich parametru
from optparse import OptionParser
parser = OptionParser()
parser.add_option("", "--dim", dest="dim",
		help="Maximal dimension of test: 1, 2, 3, 4, max")
parser.add_option("", "--type", dest="type",
		help="Type of tests: x, y, z, ori, xy, xyz, xyori, xyzori")
'''parser.add_option("", "--adj", action="store_true", dest="adj",
		help="vypis souradnic urcovanych a opernych bodu z tagu <adjusted>")
parser.add_option("", "--apriori", action="store_true", dest="apriori",
		help="vypis smerodatnych odchylek apriornich")
parser.add_option("", "--aposteriori", action="store_true", dest="aposteriori",
		help="vypis smerodatnych odchylek aposteriornich")
parser.add_option("", "--coord", action="store_true", dest="coord",
		help="pouze vypis souradnic bez presnosti")'''
(options, args) = parser.parse_args();

if len(args) != 2:
	print "usage: displacement_test.py epoch1.xml epoch2.xml"
	sys.exit(1)

try:
	file1 = open(args[0])
	file2 = open(args[1])
except:
	sys.exit(1)

test = Displacement()
test.parse_epochs(file1, file2)
test.make_test()
print test.results
#print test.results.id
#print test.results.diff_xyz

