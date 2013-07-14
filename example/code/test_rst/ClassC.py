# gizela 
# 
# Copyright (C) 2010 Michal Seidl, Tomas Kubin 
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz> 
# URL: <http://slon.fsv.cvut.cz/gizela> 
# 
# $Id: GamaDataObs.py 37 2010-05-25 08:09:13Z michal $

"""
The sample of Gizela class module.

#. The module file name is exatly same as the name of the class.
#. The file carry only the class definition and its Error class.

"""

class ClassC(object):
	"""
	Class documentation 
		- new style Python code
			- class as a object 
			- I{super()} function
		- code indenting with 4 spaces

	You never call this class before calling :func:`public_fn_with_sphinxy_docstring`.

	.. note::

	   An example of intersphinx is this: you **cannot** use :mod:`pickle` on this class.

		
	Args:
	   name (str):  The name to use.

	Kwargs:
	   state (bool): Current state to be in.

	Returns:
	   int.  The return code::

		  0 -- Success!
		  1 -- No good.
		  2 -- Try again.

	Raises:
	   AttributeError, KeyError

	A really great idea.  A way you might use me is

	>>> print public_fn_with_googley_docstring(name='foo', state=None)
	0

	BTW, this always returns 0.  **NEVER** use with :class:`MyPublicClass`.

	"""	
	
	PUBLIC_CONSTANT 	= 'public constant'	#: public constant
	_PRIVATE_CONSTANT 	= 'private constant'	#: private constatnt
	publicAtribute 		= 'public atribute'	#: public atribute
	_privateAtribute 	= 'private atribute'	#: private atribute
	_x = None
	

	def __init__(self,b=None,c=3):
		"""class constrictor
		
		:param etype: exception type
   		:param value: exception value
		:param tb: traceback object
		:param limit: maximum number of stack frames to show
		:type limit: integer or None
		:returns: formatted list of strings
		:rtype: list
		"""
		self.writableAtribute = b #:tohle je atribute a inline komentar
		pass
	
	
	
	def sum(self,a,b):
		"""
		Public function sum.
		

		:param a: bla bla
		:type a: float
		:param b: exception value
		:type b: float or None
		:returns: formatted list of strings
		:rtype: list
		
		"""
		
		print (self.PUBLIC_CONSTANT)
		print (self._PRIVATE_CONSTANT)
		return a-b

	def sum2(self,a,b):
		"""
		Public function sum

		:Parametres: bla bla
			- a float
   			- b exception value
   		:Returns:
			- list of strings
		
		"""
		
		print (self.PUBLIC_CONSTANT)
		print (self._PRIVATE_CONSTANT)
		return a-b

	
	def add(self,a,b):
		"""
		Private function _add

		Keyword arguments:
		timestamp	 -- the format string (default '')
		priority	  -- priority number (default '')
		priority_name -- priority name (default '')
		message	   -- message to display (default '')
		"""
		
		print (self.PUBLIC_CONSTANT)
		print (self._PRIVATE_CONSTANT)
		return a-b