#numberFileGenerator.py
```
python numberFileGenerator.py <number of points> <max size of point>
```
Generates "generated_input.txt" with a list of points.
By default, 1000 points with values from 0 to 1000
It overwrites the current generated_input.txt, so just know if you run it again, you'll have different input.


#analyzer.py
```
./a.out < generated_input.txt > generated_output.txt; python analyzer.py
```
Graphically shows how your algorithm traverses.
First you'll need to have python and the module "graphics.py" in wherever your python modules are stored.
Run your main cpp file with this. The name of the .txt files are important.

#analyze.sh
```
analyze.sh <number of points> <max size of point>
```
Automates the process of using this tool

#graphics.py
the module that analyzer.py requires to run
Put this in your python folder where your modules typically go. You can look this up on Google, since it
varies from OS to OS.
