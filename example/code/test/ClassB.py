# gizela 
# 
# Copyright (C) 2010 Michal Seidl, Tomas Kubin 
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz> 
# URL: <http://slon.fsv.cvut.cz/gizela> 
# 
# $Id: GamaDataObs.py 37 2010-05-25 08:09:13Z michal $

"""
The sample of Gizela Class B.
"""

from gizela.util.Error import Error
from ClassA import ClassA

class ClassBError(Error):
	"""
	Error Class of B Class
	"""
	pass

a = ClassA()
print(dir(a))
#a.PUBLIC_CONSTANT = 23
a.writableAtribute = 5
print(a.writableAtribute)
print(a.PUBLIC_CONSTANT)