# **********************Author Info**************************
# *@author    Christopher Findeisen                         *
# *@contact    <cfindeisen7@gmail.com>                      *
# *@date     Mon Jan 26 18:13:38 2015                       *
# ***********************************************************
from graphics import *
import time
f = open('generated_input.txt', 'r')


win = GraphWin('Coordinate Plane', 1000, 1000) # give title and dimensions
given_point_order = []
for line in f:
    print line
    numbers = line.split();
    x = int(numbers[0])
    y = int(numbers[1])
    pt = Point( x, y )
    pt.draw(win)
    given_point_order += [x,y]

f.close()
f = open('martin_output.txt', 'r')
prev_x = -1
prev_y = -1
for line in f:
    numbers = line.split();
    pt_no = int(numbers[0]) * 2
    x = given_point_order[pt_no]
    y = given_point_order[pt_no+1]
    if prev_x >= 0:
        connection = Line(Point(prev_x,prev_y), Point(x, y))
        connection.draw(win)
        #if you want to see the graph traverse more slowly, uncomment this!
        # time.sleep(1)
    prev_x = x
    prev_y = y

win.getMouse() # Pause to view result
win.close()
