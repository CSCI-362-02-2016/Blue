from Test import Test

from unisubs.deploy.deploy import *

class LogTest(Test):

    def __init__( self ):
        self.name = "LogTest"
        Test.__init__( self )
        
    def func( self, args, expected ):
        return log(args[0], args[1], args[2]) == expected
