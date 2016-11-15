from testCases import *

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
        self.setDetails()
        self.getParamList()
        
    def getDetails( self ):
        return self.details

    def setDetails( self ):
        file = open("../testCases/" + self.name + ".txt")
        fileStr = file.read()
        file.close()
        fileArray = fileStr.split("\n")
        self.requirement = fileArray[1].split(":")[1].strip()
        self.component = fileArray[3].split(":")[1].strip()
        self.function = fileArray[5].split(":")[1].strip()

    def getParamList( self ):
        file = open("../testCases/" + self.name + ".txt")
        fileStr = file.read()
        file.close()
        fileArray = fileStr.split("\n")
        self.paramList = []
        self.expectedList = []
        for i in range(len(fileArray) - 1):
            if fileArray[i][0] != "=":
                splt = fileArray[i].split("|")                    
                self.paramList += [splt[1:-1]]
                self.expectedList += [splt[-1]]

    def runTest( self, args, expected ):
        
        passFail = self.func( args, expected )
        self.details
        self.details[self.PASS_FAIL_INDEX] = ('PASS' if passFail else 'FAIL')
        self.details[self.EXPECTED_INDEX] = str( expected )
        self.details[self.ARGUMENTS_INDEX] = ", ".join(args)
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
        for i in range(len(self.paramList)):
            test = self.runTest(self.paramList[i], self.expectedList[i])
            totalResult += test[0]
            totalDetail += test[1]
            self.setID(self.getID() + 1)
        return [totalResult, totalDetail]

    def func( self, args, expected ):
        pass

    def setID( self, id ):
        self.id = id

    def getID( self ):
        return self.id

    def report( self ):
        return self.report

