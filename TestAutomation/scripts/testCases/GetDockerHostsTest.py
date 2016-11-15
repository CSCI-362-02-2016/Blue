from Test import Test
from unisubs.deploy.deploy import *

class GetDockerHostsTest(Test):

    def __init__( self ):
        self.name = "GetDockerHostsTest"
        Test.__init__( self )
        
    def func( self, args, expected ):
        cleanup = Cleanup()
        return cleanup.get_docker_hosts() == expected
