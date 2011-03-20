"""example of class with managed attributes and slots"""

class attrib(object):

	__slots__ = ["atr1", "_atr2"]

	def __init__(self):
		self.atr1 = 1
		self._atr2 = 1

	def _get_atr2(self):
		print "Method _get_atr2"
		return self._atr2
	
	def _set_atr2(self, atr2):
		print "Method _set_atr2"
		self._atr2 = atr2
	
	atr2 = property(_get_atr2, _set_atr2) # managed attribute

if __name__ == "__main__":

	a = attrib()
	print a.atr1
	print a.atr2
	a.atr1 = 2
	a.atr2 = 2
	print a.atr1
	print a.atr2
