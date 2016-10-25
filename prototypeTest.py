from Test import Test



class prototypeTest(Test):

    def __init__( self ):
        Test.__init__( self )
        self.requirement = "Functionality of Driver"
        self.component = "prototypeTest"
        self.function = "runTest"
        self.expected = "True"
        
    def func( self, args ):
        return args

    def getArgList( self ):
        argList = [
            True,
            False
            ]
        return argList
