from Test import Test

from unisubs.deploy.deploy import *

class CdToProjectRootTest(Test):

    def __init__( self ):
        self.name = "CdToProjectRootTest"
        Test.__init__( self )
        
    def func( self, args, expected ):
        deploy = Deploy()
        return deploy.cd_to_project_root() == eval(expected)
