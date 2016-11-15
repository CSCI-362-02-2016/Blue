from Test import Test

from unisubs.deploy.deploy import *

class LogNoStarTest(Test):

    def __init__( self ):
        self.name = "LogNoStarTest"
        Test.__init__( self )
        
    def func( self, args, expected ):
        return log_nostar(args[0], args[1], args[2]) == expected
