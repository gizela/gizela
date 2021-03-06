# gizela 
# 
# Copyright (C) 2010 Michal Seidl, Tomas Kubin 
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz> 
# URL: <http://slon.fsv.cvut.cz/gizela> 
# 
# $Id: GamaDataObs.py 37 2010-05-25 08:09:13Z michal $

"""
The sample of Gizela class module.
==================================
	- The module file name is exatly same as the name of the class.
	- The file carry only the class definition and its Error class.
"""

#__docformat__ = 'epytext en'
#"""Docformat of this file"""

#from gizela.util.Error import Error

#class ClassAError(Error):
#	"""
#	Error class of A class.
#	"""
#	pass

class ClassA(object):
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
	
		#Class Atributes
	
	PUBLIC_CONSTANT 	= 'public constant'	#: public constant
	_PRIVATE_CONSTANT 	= 'private constant'	#: private constatnt
	publicAtribute 		= 'public atribute'	#: public atribute
	_privateAtribute 	= 'private atribute'	#: private atribute
	_x = None
	
	#__slots__ = ['writableAtribute','readonlyAtribute','CONSTANT']
	#__slots__=['writableAtribute','_x']
	# Pouziti slotu zpusobi ze vsechmy class atributy jsou jen read-only krome tech co
	# jsou pristupny jako property
	# Instance atributy musi byt uvedeny ve slotu jinak chyba a nelze ho pouzivat.
	# Dalsi veci je ze slot ma nejaky vliv na to co se dedi. Napriklad pri pouziti slotu
	# ma trida ClassC atribut writableAtribut z tridy ClassA prostoze nebyl zavolan konstruktor
	#"""Disable adding or changing arguments not mentioned here"""

	def __init__(self,b=None,c=3):
		"""Class inicialization function"""
		#Data or instance atributes
		self.writableAtribute = 'w'
		
		#self.PUBLIC_CONSTANT = 3
		#self.readonlyAtribute = 'r'
		#self.CONSTANT = 'constant'
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
		print self.PUBLIC_CONSTANT
		print self._PRIVATE_CONSTANT
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

class ClassC(ClassA):
	#def __init__(self):
	pass
	
if __name__ == "__main__":
	instanceA = ClassA()
	print instanceA.sum(1,2)
	print instanceA.x
	instanceA.x = 10
	print instanceA.x
	instanceA.writableAtribute = 3
	#instanceA.publicAtribute = 3
	
	#instanceA.PUBLIC_CONSTANT = 3
	print instanceA.PUBLIC_CONSTANT,instanceA._PRIVATE_CONSTANT,instanceA.publicAtribute,instanceA._privateAtribute
	print instanceA.writableAtribute
	#print insta
	#print instanceA._PRIVATE_CONSTANT,
	
	instanceB = ClassA()
	print instanceB.PUBLIC_CONSTANT
	print instanceB.writableAtribute
	
	instanceC = ClassC()
	print instanceC.PUBLIC_CONSTANT
	print dir(instanceC)
	instanceC.x = 20
	instanceC._x = 20
	#print instanceC.writableAtribute
	print instanceC.sum(0,10)
	#print instanceC.writableAtribute
