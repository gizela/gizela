"""Example abstract class - implementation with exception"""

class Abstract(object):
    """Abstract class
    abstract methods:
    	aMethod
    """
    
    def aMethod( self ):
        raise NotImplementedError( "Should have implemented this" )

