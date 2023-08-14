# p7.py
# Laila Bahman
# 7/1/22
# Python 3.10.5
# Description:
'''
Circumference & Area of a Circle
Write a program to compute the circumference and area of a circle.
The user will input the radius of a circle.
Validate Input: Make sure that the radius is positive, or give an error message.
The program will show the circumference and area of a circle with that radius.
The answers should be rounded to the nearest tenth.
Program should run as shown:
What is the radius (in inches) of the circle you want to draw?  12
A circle with radius 12 inches has
circumference:   75.4 inches
area:   452.4 sq. inches
Algorithm
Use 3.1415 as the value of PI.
Enter radius
Circumference of a Circle = 2 * PI * R
Area of a Circle = PI * R*R
'''

PI = 3.14159265
radius = float(input('Enter radius:'))
if radius<0:
    print('ERROR: Radius cannot be negative.')

else:
    area = PI*radius*radius
    print('A circle with radius %.1f inches has' %radius)
    print('Area: %.1f square inches' %area)

'''
>>>
=================== RESTART: /Users/lailabahman/Desktop/p7.py ==================
Enter radius:9
A circle with radius 9.0 inches has
Area: 254.5 square inches
>>>
'''
