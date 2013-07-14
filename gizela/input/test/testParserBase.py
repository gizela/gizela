'''
Created on Jul 6, 2013

@author: michal
'''

from gizela.input.ParserBase import ParserBase
from gizela.adj.local.NetworkAdj import NetworkAdj 


def test_parser_data():
    parser = ParserBase()
    networkAdj = NetworkAdj()
    parserConfig = 2
    parser.parser_data(networkAdj,parserConfig)
    assert networkAdj == [2]
