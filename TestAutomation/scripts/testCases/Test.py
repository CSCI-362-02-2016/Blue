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
        files = os.listdir(os.path.realpath("..") + "/TestAutomation/testCases/")
        for fn in files:
            if fn[-4:] == ".txt" and fn.split(" ")[1][:-4] == self.name:
                file = open(os.path.realpath("..") + "/TestAutomation/testCases/" + fn)
                break
        fileStr = file.read()
        file.close()
        fileArray = fileStr.split("\n")
        self.component = fileArray[10].strip()
        self.function = fileArray[11].strip()

    def getParamList( self ):
        self.paramList = []
        self.expectedList = []
        self.requirements = []
        self.ids = []
        files = os.listdir(os.path.realpath("..") + "/TestAutomation/testCases")
        for fn in files:
            if fn[-4:] == ".txt" and fn.split(" ")[1][:-4] == self.name:
                file = open(os.path.realpath("..") + "/TestAutomation/testCases/" + fn)
                fileStr = file.read()
                file.close()
                if fileStr[-1] == '\n':
                    fileStr = fileStr[:-1]
                fileArray = fileStr.split("\n")
                self.ids += [fileArray[8]]
                self.requirements += [fileArray[9]]
                self.expectedList += [fileArray[13]]
                self.paramList += [fileArray[12].split(",")]                    

    def runTest( self, id, args, expected, requirement ):
        
        passFail = self.func( args, expected )
        self.requirement = requirement
        self.details[self.PASS_FAIL_INDEX] = ('PASS' if passFail else 'FAIL')
        self.details[self.EXPECTED_INDEX] = str( expected )
        self.details[self.ARGUMENTS_INDEX] = ", ".join(args)
        self.details[self.FUNCTION_INDEX] = self.function
        self.details[self.COMPONENT_INDEX] = self.component
        self.details[self.REQUIREMENT_INDEX] = self.requirement
        self.details[self.ID_INDEX] = str( id )
        htmlFormat = ""
        for i in range(0, len(self.details), 4):
            htmlFormat += " ".join(self.details[i:i+4])
        return [('.' if passFail else 'F'), htmlFormat]

    def runTests( self ):
        totalResult = ""
        totalDetail = ""
        for i in range(len(self.paramList)):
            test = self.runTest(self.ids[i], self.paramList[i], self.expectedList[i], self.requirements[i])
            totalResult += test[0]
            totalDetail += test[1]
        return [totalResult, totalDetail]

    def func( self, args, expected ):
        pass

    def report( self ):
        return self.report

