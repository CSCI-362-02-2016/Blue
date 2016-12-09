#!/usr/bin/env python3

import sys, os, webbrowser
from testCases import *

def driver( args ):
    
    testObjects = []
    fileArray = []
    files = sorted(os.listdir(os.path.realpath("..") + "/TestAutomation/testCases"), key=getTestNum)
    for fn in files:
        if fn[-4:] == ".txt":
            if not fn.split(' ')[1][:-4] + "()" in fileArray:
                fileArray += [fn.split(' ')[1][:-4] +"()"]
    
    file = open(os.path.realpath("..") + "/TestAutomation/temp/testOutput.html", "wb")
    for i in range(len(fileArray)):
        testObjects += [eval(fileArray[i])]
    style = '<style type = "text/css"> table {width: 75%; border: 1px solid black; padding: 1px;} td {text-align: left; border: 1px solid black; padding: 10px;} th {text-align: left; padding: 10px;}</style>'
    results = "Simplified Results:<div>"
    details = '<body>Detailed Results: <table style = "border-collapse: collapse; width: 100%;">'
    for test in testObjects:
        tempResults = test.runTests()
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

def getTestNum( filename ):
    
    return int(eval( filename.split(" ")[0] )) if filename[-4:] == ".txt" else 10000
                   
if __name__ == '__main__':
    driver( sys.argv ) if sys.argv[0] != "runAllTests.py" else driver(sys.argv[1:])
