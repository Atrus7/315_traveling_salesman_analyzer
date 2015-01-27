import random
#change these parameters to change output
number_of_points = list(xrange(1000))
max_point_value = list(xrange(1000))
########################################

f = open('generated_input.txt', 'w')
while countlist:
  countlist.pop()
  f.write(str(random.choice(mylist)))
  f.write('  ')
  f.write(str(random.choice(mylist)))
  f.write('\n')
f.close()
