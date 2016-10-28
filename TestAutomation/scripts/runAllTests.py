#!/usr/bin/env python3

import sys
from prototypeTest import prototypeTest

def driver( args ):
    
    testObjects = [
        prototypeTest(),
        ]
    
    file = open("testNames.txt", "r")
    fileStr = file.read()
    if fileStr[-1] == "\n":
        fileStr = fileStr[:-1]
    fileArray = fileStr.split("\n")
    file.close()

    file = open("testOutput.html", "w")
    id = 0

    tests = {}

    for i in range(len(fileArray)):
        tests[fileArray[i]] = testObjects[i]
    
    results = "<head>Simplified Results:<div>"
    details = "<body>Detailed Results:"
    
    if len( args ) == 0:
        for key, value in tests.items():
            value.setID( id )
            tempResults = value.runTests()
            id = value.getID()
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
    driver( sys.argv ) if sys.argv[0] != "pSpec.py" else driver(sys.argv[1:])
