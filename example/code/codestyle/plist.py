"""porovnani rychlosti slovniku a listu s indexy ve slovniku

vysledek: pro 1e6 polozek je rozdil v casech mensi nez 1s
"""

import sys


if len(sys.argv) == 2:
	if sys.argv[1] == "list":
		list = True
	elif sys.argv[1] == "dict":
		list = False
else:
	sys.exit(1)

pl=range(1000000)
ind={}
pd={}
for i in pl:
	ind[2*i]=i
	pd[2*i]=i

if list:
	for key in ind:
		x = pl[ind[key]]

	print x


else:
	for key in pd:
		x = pd[key]

	print x
