# gizela 
# 
# Copyright (C) 2010 Michal Seidl, Tomas Kubin 
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz> 
# URL: <http://slon.fsv.cvut.cz/gizela> 
# 
# $Id: GamaDataObs.py 37 2010-05-25 08:09:13Z michal $

"""
The sample of Gizela class module.

# The module file name is exatly same as the name of the class.
# The file carry only the class definition and its Error class.

(http://www.seznam.cz)
"""

class ClassC(object):
	"""
	Class A documentation
		- new style Python code
			- class as a object
			- 
			- I{__slots__}
			- I{super()} function
			- I{property()}
		- code indenting with I{\\t}
	"""	
	
	PUBLIC_CONSTANT 	= 'public constant'	#: public constant
	_PRIVATE_CONSTANT 	= 'private constant'	#: private constatnt
	publicAtribute 		= 'public atribute'	#: public atribute
	_privateAtribute 	= 'private atribute'	#: private atribute
	_x = None
	

	def __init__(self,b=None,c=3):
		"""Class inicialization function"""
		self.writableAtribute = 'w' #:tohle je atribut#		
		pass
	
	def sum(self,a,b):
		"""
		Sum of a and b.

		@param	a: first argument
		@type	a: number
		@param	b: second argument
		@type	b: number
		@return: Returns M{a+b}
		@rtype	: number	
		
		"""
		print (self.PUBLIC_CONSTANT)
		print (self._PRIVATE_CONSTANT)
#	publicAtribute 		= 'public atribute'
#	_privateAtribute 	= 'private atribute'
		return a-b

	def _getx(self): return self._x
	def _setx(self, value): self._x = value
	def _delx(self): del self._x

	x = property(_getx, _setx, _delx, "I'm the 'x' property.")
	"""
	Properties are sometimes called managed atributes.
	It is easier way then using pure Python descriptors.
	U{http://users.rcn.com/python/download/Descriptor.htm}
	"""