from Test import Test
import sys

from unisubs.deploy.deploy import *

class prototypeTest(Test):

    def __init__( self ):
        self.name = "prototypeTest"
        Test.__init__( self )
        
    def func( self, args, expected ):
        return True
        #print( log(args[0], args[1], args[2]) == "* My friend Sam")

