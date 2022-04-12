print("Valid Triangle Tester")
print()

pt1_x = float(input("Enter Point #1 - x position: "))
pt1_y = float(input("Enter Point #1 - y position: "))
pt2_x = float(input("Enter Point #2 - x position: "))
pt2_y = float(input("Enter Point #2 - y position: "))
pt3_x = float(input("Enter Point #3 - x position: "))
pt3_y = float(input("Enter Point #3 - y position: "))
print()

print("The length of each side of your test shape is:")
print()

import math
side1_dist = float(format(math.sqrt(math.pow(pt1_x - pt2_x, 2) + math.pow(pt1_y - pt2_y, 2)), ".2f"))
side2_dist = float(format(math.sqrt(math.pow(pt1_x - pt3_x, 2) + math.pow(pt1_y - pt3_y, 2)), ".2f"))
side3_dist = float(format(math.sqrt(math.pow(pt2_x - pt3_x, 2) + math.pow(pt2_y - pt3_y, 2)), ".2f"))

print("Side 1: ", side1_dist)
print("Side 2: ", side2_dist)
print("Side 3: ", side3_dist)
print()

if side1_dist + side2_dist > side3_dist and side1_dist + side3_dist > side2_dist and side2_dist + side3_dist > side1_dist:
    print("This is a valid triangle!")
    if side1_dist == side2_dist == side3_dist:
        print("This is an equilateral triangle")
    elif side1_dist == side2_dist and side3_dist != side1_dist and side3_dist != side2_dist:
        print("This is an isosceles triangle")
    elif side1_dist == side3_dist and side2_dist != side1_dist and side2_dist != side3_dist:
        print("This is an isosceles triangle")
    elif side2_dist == side3_dist and side1_dist != side2_dist and side1_dist != side3_dist:
        print("This is an isosceles triangle")
    elif side1_dist != side2_dist != side3_dist:
        print("This is a scalene triangle")
else:
    print("This is not a valid triangle")
