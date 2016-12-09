from Test import Test
from sys import *
from io import *
from unisubs.deploy.deploy import *

class CdToProjectRootTest(Test):

    def __init__( self ):
        self.name = "CdToProjectRootTest"
        Test.__init__( self )
        
    def func( self, args, expected ):
        backup = sys.stdout
        sys.stdout = BytesIO()
        deploy = Deploy()
        deploy.cd_to_project_root()
        value = sys.stdout
        sys.stdout = backup
        return value.getvalue()[:8] + ".." + value.getvalue()[-27:-1] == expected
