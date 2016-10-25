class Test:

    PASS_FAIL_INDEX = 26
    ARGUMENTS_INDEX = 18
    ID_INDEX = 2

    def __init__( self, details ):
        self.details = details
        self.report = ""
        
    def getDetails( self ):
        return self.details

    def runTest( self, args ):
        
        passFail = self.func( args )
        
        self.details[self.PASS_FAIL_INDEX] = ('PASS' if passFail else 'FAIL')
        self.details[self.ARGUMENTS_INDEX] = str( args )
        self.details[self.ID_INDEX] = str( self.getID() )
        htmlFormat = "<div>===================================\n\n</div>"
        for i in range(0, len(self.details), 4):
            htmlFormat +="<div>" + " ".join(self.details[i:i+4]) + "</div>"
        htmlFormat += "<div>===================================\n\n</div>"
        return [('.' if passFail else 'F'), htmlFormat]

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

