import random
# for CLI arguments
import sys

# defaults
number_of_points = 1000
max_point_value = 1000

# if we have cli arguments
if len(sys.argv) == 3:
  number_of_points = int(sys.argv[1])
  max_point_value = int(sys.argv[2])

# List of all possible x's and y's
xs = list(xrange(max_point_value))
ys = list(xrange(max_point_value))

# randomize points
random.shuffle(xs)
random.shuffle(ys)

# open file
f = open('generated_input.txt', 'w')

# write points to file
for i in range(number_of_points):
  f.write(str(xs[i]))
  f.write('\t')
  f.write(str(ys[i]))
  f.write('\n')
f.close()
