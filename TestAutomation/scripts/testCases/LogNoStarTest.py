from Test import Test
from sys import *
from io import *
from unisubs.deploy.deploy import *

class LogNoStarTest(Test):

    def __init__( self ):
        self.name = "LogNoStarTest"
        Test.__init__( self )
        
    def func( self, args, expected ):
        backup = sys.stdout
        sys.stdout = BytesIO()
        log_nostar(args[0], args[1], args[2])
        value = sys.stdout
        sys.stdout = backup
        return value.getvalue()[:-1] == expected
