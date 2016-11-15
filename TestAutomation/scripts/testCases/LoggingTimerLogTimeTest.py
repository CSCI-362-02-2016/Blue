from Test import Test
from unisubs.deploy.deploy import *

class LoggingTimerLogTimeTest(Test):

    def __init__( self ):
        self.name = "LoggingTimerLogTimeTest"
        Test.__init__( self )

    def func( self, args, expected ):
        x = LoggingTimer()
        time.sleep(eval(args[0]))
        return x.log_time("Time is", "") == expected
