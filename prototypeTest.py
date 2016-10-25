from Test import Test

details = "Prototype Test"

class prototypeTest(Test):

    def __init__( self ):
        Test.__init__( self, details)
        
    def func( self, args ):
        return True

    def runTests( self ):
        return self.runTest( [] )
