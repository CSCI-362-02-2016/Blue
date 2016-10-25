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

    def runTests( self ):
        totalResult = ""
        totalDetail = ""
        argList = [
            True,
            False
            ]
        for args in argList:
            test = self.runTest(args)
            totalResult += test[0]
            totalDetail += test[1]
            self.setID(self.getID() + 1)
        return [totalResult, totalDetail]
