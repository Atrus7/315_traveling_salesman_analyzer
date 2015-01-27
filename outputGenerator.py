import random
countlist = list(xrange(1000))
mylist = list(xrange(1000))
f = open('generated_output.txt', 'w')
for i in countlist:
  f.write(str(i))
  f.write('\n')
f.close()
