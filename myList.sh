#!/bin/bash

location=$(pwd)
fileNames=$(ls)
displayedFiles=""
for test in $fileNames; do
	displayedFiles="$displayedFiles $test"
done

echo -e $displayedFiles > output.html

firefox output.html
rm output.html
