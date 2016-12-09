from Test import Test
from io import *
from sys import *
from unisubs.deploy.deploy import *

class MultiArgLogTest(Test):

    def __init__( self ):
        self.name = "MultiArgLogTest"
        Test.__init__( self )
        
    def func( self, args, expected ):
        backup = sys.stdout
        sys.stdout = BytesIO()
        x = args[1].split("|")
        tuple_args = tuple(x)
        self.applylast(log, args[0], tuple_args, args[2])
        value = sys.stdout
        sys.stdout = backup
        actual = value.getvalue()[:-1] 
        return actual == expected, actual

            
    def applylast(self, func, arg1, arglist, *literalargs):
        return func(*((arg1,) + arglist + literalargs))

