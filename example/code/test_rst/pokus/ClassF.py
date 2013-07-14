"""
Created on Jul 11, 2013

"""

from test_rst.ClassC import ClassC

class ClassF(ClassC):
    """
    Trida dedi z tridy ClassC
    """

    def __init__(self, foo, bar='baz'):
        """A really simple class.
        


        Args:
           foo (str): We all know what foo does.

        Kwargs:
           bar (str): Really, same as foo.

        """
        self._foo = foo
        self._bar = bar

    def pokus(self,c,d):
        """ Cha cha"""
        return(c+d)
    
    def test(self):
        """ co je tohle
        .. highlightlang:: python
                amdkks = ljaslj + 4
        """
        pass
            