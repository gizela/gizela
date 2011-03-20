class A(object):
	__slots__=["a"]

class B(object):
	__slots__=["b"]
	#__slots__=["a"]
	pass

class C(A,B): pass

c = C()
print c
print dir(c)
