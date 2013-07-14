# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>


from gizela.util.Error import Error


class ParserBaseError(Error):
    pass


class ParserBase(object):
    """abstract class for input parsers
    """

    def __init__(self):
        """constructor
        """
        pass
    
    def parser_data(self,NetworkAdj,parserConf):
        """parsers data and full fill NetworkAdj object
        @type NetworkAjd: 
        @type parserConf: 
        """
        pass
        

if __name__ == "__main__":

    print ("This is ParserBase class")