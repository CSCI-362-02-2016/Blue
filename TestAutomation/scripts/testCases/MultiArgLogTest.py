from Test import Test

from unisubs.deploy.deploy import *

class MultiArgLogTest(Test):

    def __init__( self ):
        self.name = "MultiArgLogTest"
        Test.__init__( self )
        
    def func( self, args, expected ):
        x = args[1].split(",")
        tuple_args = tuple(x)
        result = self.applylast(log, args[0], tuple_args, args[2])
        return result == expected

            
    def applylast(self, func, arg1, arglist, *literalargs):
        return func(*((arg1,) + arglist + literalargs))

