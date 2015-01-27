#!/bin/bash

# move old output (this only will save you once!)
mv generated_output.txt generated_output.txt.old

python numberFileGenerator.py $1 $2
./a.out < generated_input.txt > generated_output.txt
python analyzer.py
