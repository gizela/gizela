class A:
    "class and instance variables"

    i = 1 # class variable
    def __init__(self, j=2):
        self.j = j # instance variable

    def increase(self):
        self.j += 1 
        self.i += 1 # instance variable - initial value is taken from class
                    # variable 'i'

a1 = A()
a2 = A()
a2.increase()
print a1.i, a1.j
print a2.i, a2.j
print A.i, a1.i

print a1.i, A.i
A.i = 5
print a1.i, A.i

print a1.i, A.i
a1.i = 10
print a1.i, A.i
