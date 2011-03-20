class d(object):
    def delete(self):
        self.__del__()

    def __init__(self, a=1):
        self.a = a

    def init(self):
        self.__init__()

    def replace(self, a=10):
        new = d(a=a)
        print new.a
        # nefunguje self = new

a=d()
b=d(10)
print a
print b
del a
#print a

print b.a
b.init()
print b.a

#replace
c=d()
c.replace()
print c.a
