from Test import Test
from sys import *
from io import *
from unisubs.deploy.deploy import *

class LogTest(Test):

    def __init__( self ):
        self.name = "LogTest"
        Test.__init__( self )
        
    def func( self, args, expected ):
        backup = sys.stdout
        sys.stdout = BytesIO()
        log(args[0], args[1], args[2])
        value = sys.stdout
        sys.stdout = backup
        print(value.getvalue())
        return value.getvalue()[:-1] == expected
