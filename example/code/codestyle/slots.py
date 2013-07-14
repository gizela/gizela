class A(object):
        __slots__ = ["a","b","c"]
        
        def __init__(self):
                self.a="x"
                self.b="xx"
                self.c="xxx"
    
        def __str__(self):
                "list all slot attributes"
                return "\n".join(["%s: %s" % 
                                  (self.__slots__[i], 
                                   self.__getattribute__(self.__slots__[i]))
                                  for i in xrange(len(self.__slots__))])

if __name__ == "__main__":

        a = A()
        print a

