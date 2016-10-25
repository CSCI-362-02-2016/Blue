from Test import Test

details = [
    "###", "Test ID:\t", "", "###\n",
    "###", "Requirement Tested:\t", "Functionality of driver", "###\n",
    "###", "Component Tested:\t", "prototypeTest", "###\n",
    "###", "Function Tested:\t", "runTest", "###\n",
    "###", "Arguments:\t", "", "###\n",
    "###", "Expected Result:\t", "True", "###\n",
    "###", "Pass/Fail:\t", "", "###\n"
    ]

class prototypeTest(Test):

    def __init__( self ):
        Test.__init__( self, details)
        
    def func( self, args ):
        return args

    def getArgList( self ):
        argList = [
            True,
            False
            ]
        return argList
