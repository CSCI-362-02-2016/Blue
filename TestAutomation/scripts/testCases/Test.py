from testCases import *
import sys, os
class Test:

    details = [
    '<tr><td>', "Test ID:", "", "</td><tr>",
    "<tr><td>", "Requirement Tested:", "Functionality of driver", "</td>",
    "<td>", "Arguments:", "", "</td></tr>",
    "<tr><td>", "Component Tested:", "prototypeTest", "</td>",
    "<td>", "Expected Result:", "True", "</td></tr>",
    "<tr><td>", "Function Tested:", "runTest", "</td>",
    "<td>", "Pass/Fail:", "", "</td></tr>"
    ]

    
    PASS_FAIL_INDEX = 26
    EXPECTED_INDEX = 18
    ARGUMENTS_INDEX = 10
    FUNCTION_INDEX = 22
    COMPONENT_INDEX = 14
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
        self.component = fileArray[3].split(":")[1].strip()
        self.function = fileArray[5].split(":")[1].strip()

    def getParamList( self ):
        self.paramList = []
        self.expectedList = []
        self.requirements = []
        files = os.listdir("../testCases")
        for fn in files:
            if fn[:len(self.name)] == self.name:
                file = open("../testCases/" + fn)
                fileStr = file.read()
                file.close()
                if fileStr[-1] == '\n':
                    fileStr = fileStr[:-1]
                fileArray = fileStr.split("\n")
                for i in range(len(fileArray)):
                    if fileArray[i][0] != "=" :
                        splt = fileArray[i].split("|")
                        self.paramList += [splt[1:-1]]
                        self.expectedList += [splt[-1]]
                    elif i == 1:
                        self.requirements += [fileArray[i][15:]]


    def runTest( self, args, expected, requirement ):
        
        passFail = self.func( args, expected )
        self.requirement = requirement
        self.details[self.PASS_FAIL_INDEX] = ('PASS' if passFail else 'FAIL')
        self.details[self.EXPECTED_INDEX] = str( expected )
        self.details[self.ARGUMENTS_INDEX] = ", ".join(args)
        self.details[self.FUNCTION_INDEX] = self.function
        self.details[self.COMPONENT_INDEX] = self.component
        self.details[self.REQUIREMENT_INDEX] = self.requirement
        self.details[self.ID_INDEX] = str( self.getID() )
        htmlFormat = ""
        for i in range(0, len(self.details), 4):
            htmlFormat += " ".join(self.details[i:i+4])
        return [('.' if passFail else 'F'), htmlFormat]

    def runTests( self ):
        totalResult = ""
        totalDetail = ""
        for i in range(len(self.paramList)):
            test = self.runTest(self.paramList[i], self.expectedList[i], self.requirements[i])
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

