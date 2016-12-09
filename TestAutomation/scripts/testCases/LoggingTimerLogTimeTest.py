from Test import Test
from sys import *
from io import *
from unisubs.deploy.deploy import *



class LoggingTimerLogTimeTest(Test):
    def __init__( self ):
        self.name = "LoggingTimerLogTimeTest"
        Test.__init__( self )

    def func( self, args, expected ):
        backup = sys.stdout
        sys.stdout = BytesIO()
        x = LoggingTimer()
        time.sleep(eval(args[0]))
        x.log_time("Time is", "")
        value = sys.stdout
        sys.stdout = backup
        actual = value.getvalue()[:-1] 
        return actual == expected, actual
