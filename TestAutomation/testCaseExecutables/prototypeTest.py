from Test import Test



class prototypeTest(Test):

    def __init__( self ):
        Test.__init__( self )
        self.requirement = "Functionality of Driver"
        self.component = "prototypeTest"
        self.function = "runTest"
        self.expected = 1
        
    def func( self, args ):
        return eval(args[0]) == self.expected

    def getArgList( self ):
        argList = [
            '1',
            '2',
            '3',
            '4',
            '5'
            ]
        return argList
