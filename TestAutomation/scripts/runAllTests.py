#!/usr/bin/env python3

import sys, os
from testCases import *

def driver( args ):
    
    testObjects = [
        LoggingTimerLogTimeTest(),
        GetDockerHostsTest(),
        CdToProjectRootTest(),
        LogTest(),
        MultiArgLogTest(),
        LogNoStarTest(),
        MultiArgLogNoStarTest()
        ]
    
    file = open("../testCases/testNames.txt", "r")
    fileStr = file.read()
    if fileStr[-1] == "\n":
        fileStr = fileStr[:-1]
    fileArray = fileStr.split("\n")
    file.close()
    
    file = open("../temp/testOutput.html", "w")
    id = 0
    tests = {}

    for i in range(len(fileArray)):
        tests[fileArray[i]] = testObjects[i]

    results = "<head>Simplified Results:<div>"
    details = "<body>Detailed Results:"
    
    if len( args ) == 0:
        for name, test in tests.items():
            test.setID( id )
            tempResults = test.runTests()
            id = test.getID()
            results += tempResults[0]
            details += tempResults[1]
    else:
        tests[args[0]].setID(0)
        tempResults = tests[args[0]].runTest(args[1:])
        results += tempResults[0]
        details += tempResults[1]

    results += "\n</div></head>"
    details += "</body>"
    file.write(results + "\n")
    file.write("<br>\n</br>")
    file.write(details + "\n")
    file.close()

if __name__ == '__main__':
    driver( sys.argv ) if sys.argv[0] != "runAllTests.py" else driver(sys.argv[1:])
