from Test import Test

from unisubs.deploy.deploy import *

class MultiArgLogNoStarTest(Test):

    def __init__( self ):
        self.name = "MultiArgLogNoStarTest"
        Test.__init__( self )
        
    def func( self, args, expected ):
        x = args[1].split(",")
        tuple_args = tuple(x)
        result = self.applylast(log_nostar, args[0], tuple_args, args[2])
        return result == expected
            
    def applylast(self, func, arg1, arglist, *literalargs):
        return func(*((arg1,) + arglist + literalargs))
