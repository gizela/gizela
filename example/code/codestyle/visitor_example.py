class Corrections(object):
	"""visitor class for making correnctions"""
	
	def visit_distance(self, distance):
		"""visitor method for correction of distance"""
		distance.val += 1
		#return distance

	def visit_direction(self, direction):
		"""visitor method for correction of direction"""
		direction.val += 10
		#return direction


class Direction(object):
	"""class for direction"""

	def __init__(self, to, val):
		self.to=to
		self.val=val

	def accept_visitor(self, visitor):
		#return visitor.visit_direction(self)
		visitor.visit_direction(self)

	def __str__(self):
		return '<direction to="%s" val="%s">' % (self.to, self.val)


class Distance(object):
	"""class for distance"""

	def __init__(self, to, val):
		self.to=to
		self.val=val

	def accept_visitor(self, visitor):
		#return visitor.visit_distance(self)
		visitor.visit_distance(self)
	
	def __str__(self):
		return '<distance to="%s" val="%s">' % (self.to, self.val)

if __name__ == "__main__":

	obsList = [Direction("A", 0), Distance("B", 0)]
	corr = Corrections()
	obsList[0].accept_visitor(corr)
	for obs in obsList: obs.accept_visitor(corr)
	for obs in obsList: print obs
