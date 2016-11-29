#!/usr/bin/env python3

import sys, os, webbrowser
from testCases import *

def driver( args ):
    
    testObjects = []
    
    file = open("../testCases/testNames.txt", "r")
    fileStr = file.read()
    if fileStr[-1] == "\n":
        fileStr = fileStr[:-1]
    fileArray = fileStr.split("\n")
    file.close()
    
    file = open("../temp/testOutput.html", "wb")
    id = 0

    for i in range(len(fileArray)):
        testObjects += [eval(fileArray[i])]
    style = '<style type = "text/css"> table {width: 75%; border: 1px solid black; padding: 1px;} td {text-align: left; border: 1px solid black; padding: 10px;} th {text-align: left; padding: 10px;}</style>'
    results = "Simplified Results:<div>"
    details = '<body>Detailed Results: <table style = "border-collapse: collapse; width: 100%;">'
    for test in testObjects:
        test.setID( id )
        tempResults = test.runTests()
        id = test.getID()
        results += tempResults[0]
        details += tempResults[1]

    results += "\n</div></head>"
    details += "</table></body>"
    file.write(style)
    file.write(results + "\n")
    file.write("<br>\n</br>")
    file.write(details + "</html>")
    file.close()

    webbrowser.open("file://" + os.path.abspath("..")[:-17] + "/temp/testOutput.html")

if __name__ == '__main__':
    driver( sys.argv ) if sys.argv[0] != "runAllTests.py" else driver(sys.argv[1:])
