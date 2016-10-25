class Test:

    def __init__( self, details ):
        self.details = details
        self.report = ""
        
    def details( self ):
        return self.details

    def runTest( self, args ):
        self.report += str( self.getID() ) + "\n" + self.details
        return [('.' if self.func( args ) else 'F'), self.report]

    def runTests( self ):
        pass

    def func( args ):
        pass

    def setID( self, id ):
        self.id = id

    def getID( self ):
        return self.id

    def report( self ):
        return self.report

