numberFileGenerator.py --For generating input.. Default params - 1000 points from 0 - 1000
You can change the parameters to make a better spread or change the number of points.
It overwrites the current generated_input.txt, so just know if you run it again, you'll have different input.
python numberFileGenerator.py


analyzer.py -- Graphically shows how your algorithm traverses.
First you'll need to have python and the module "graphics.py" in wherever your python modules are stored.
Run your main cpp file with this. The name of the .txt files are important.
./a.out < generated_input.txt | cat > generated_output.txt
python analyzer.py


graphics.py-- the module that analyzer.py requires to run

