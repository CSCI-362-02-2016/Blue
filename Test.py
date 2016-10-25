class Test:

    details = [
    "###", "Test ID:", "", "###\n",
    "###", "Requirement Tested:", "Functionality of driver", "###\n",
    "###", "Component Tested:", "prototypeTest", "###\n",
    "###", "Function Tested:", "runTest", "###\n",
    "###", "Arguments:", "", "###\n",
    "###", "Expected Result:", "True", "###\n",
    "###", "Pass/Fail:", "", "###\n"
    ]

    
    PASS_FAIL_INDEX = 26
    EXPECTED_INDEX = 22
    ARGUMENTS_INDEX = 18
    FUNCTION_INDEX = 14
    COMPONENT_INDEX = 10
    REQUIREMENT_INDEX = 6
    ID_INDEX = 2

    def __init__( self ):
        self.report = ""
        
    def getDetails( self ):
        return self.details

    def getArgList( self ):
        pass

    def runTest( self, args ):
        
        passFail = self.func( args )
        self.details
        self.details[self.PASS_FAIL_INDEX] = ('PASS' if passFail else 'FAIL')
        self.details[self.EXPECTED_INDEX] = self.expected
        self.details[self.ARGUMENTS_INDEX] = str( args )
        self.details[self.FUNCTION_INDEX] = self.function
        self.details[self.COMPONENT_INDEX] = self.component
        self.details[self.REQUIREMENT_INDEX] = self.requirement
        self.details[self.ID_INDEX] = str( self.getID() )
        htmlFormat = "<div>===================================\n\n</div>"
        for i in range(0, len(self.details), 4):
            htmlFormat +="<div>" + " ".join(self.details[i:i+4]) + "</div>"
        htmlFormat += "<div>===================================\n\n</div>"
        return [('.' if passFail else 'F'), htmlFormat]

    def runTests( self ):
        totalResult = ""
        totalDetail = ""
        argList = self.getArgList()
        for args in argList:
            test = self.runTest(args)
            totalResult += test[0]
            totalDetail += test[1]
            self.setID(self.getID() + 1)
        return [totalResult, totalDetail]

    def func( args ):
        pass

    def setID( self, id ):
        self.id = id

    def getID( self ):
        return self.id

    def report( self ):
        return self.report

