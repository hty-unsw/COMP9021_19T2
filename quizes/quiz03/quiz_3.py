# Written by *** and Eric Martin for COMP9021

# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
      )
print()

# INSERT YOUR CODE HERE
num = '0' * nb_of_leading_zeroes + f'{int(code):o}'
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
directions = dict(zip(('0', '1', '2', '3', '4', '5', '6', '7'),
                      [(0, 1), (1, 1), (1, 0), (1, -1),
                      (0, -1), (-1, -1), (-1, 0), (-1, 1)]))


directions = [(0, 1), (1, 1), (1, 0), (1, -1),
                      (0, -1), (-1, -1), (-1, 0), (-1, 1)]



current_x,current_y = (0,0)

points = {(0,0):1}

# 032    230
# num = "032"   [::-1]

# 04        0
for item in reversed(num):

    direction_x,direction_y = directions[int(item)]

    current_x = current_x + direction_x
    current_y =current_y + direction_y

    if (current_x,current_y) not in points:
        points[(current_x,current_y)] = 1
    else:
        del points[(current_x,current_y)]

keys = points.keys()

if points:
    x_list = []
    y_list = []
    for (x,y) in keys:
        x_list.append(x)
        y_list.append(y)


    x_min,x_max = min(x_list),max(x_list)
    y_min,y_max = min(y_list),max(y_list)

    1





    1
    lines = []
    for y in range(y_min, y_max + 1):

        line = []
        for x in range(x_min,x_max + 1):
            if (x,y) in points:
                line.append(on)
            else:
                line.append(off)


# 1,1,2
# 1,2,3

        lines.append(line)


for line in reversed(lines):
    for item in line:
        print(item,end='')
    print()




