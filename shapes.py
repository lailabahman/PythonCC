# shapes.py
# Laila Bahman
# 7/21/2022
# Python 3.10.5
# Description:
'''
A quadrilateral is a shape with 4 sides and 4 angles.

Write a program that lets the user enter 4 sides and 4 angles into LISTS.
The program checks if the type of quadrilateral is either: 
- Rhombus
- Square
- Rectangle
'''
while True:
    print('Make a quadrilateral')

    side1 = float(input('side 1: '))
    if side1 <= 0:
        side1 = float(input('value must be positive. side 1: '))

    side2 = float(input('side 2: '))
    if side2 <= 0:
        side2 = float(input('value must be positive. side 2: '))

    side3 = float(input('side 3: '))
    if side3 <= 0:
        side3 = float(input('value must be positive. side 3: '))

    side4 = float(input('side 4: '))
    if side4 <= 0:
        side4 = float(input('value must be positive. side 4: '))

    angle1 = float(input('angle 1: '))
    if angle1 <= 0:
        angle1 = float(input('value must be positive. angle 1: '))
    if angle1 >= 180:
        angle1 = float(input('value must be less than 180. angle 1:'))

    angle2 = float(input('angle 2: '))
    if angle2 <= 0:
        angle2 = float(input('value must be positive. angle 2: '))
    if angle2 >= 180:
        angle2 = float(input('value must be less than 180. angle 2:'))

    angle3 = float(input('angle 3: '))
    if angle3 <= 0:
        angle3 = float(input('value must be positive. angle 3: '))
    if angle3 >= 180:
        angle3 = float(input('value must be less than 180. angle 3:'))

    angle4 = float(input('angle 4: '))
    if angle4 <= 0:
        angle4 = float(input('value must be positive. angle 4: '))
    if angle4 >= 180:
        angle4 = float(input('value must be less than 180. angle 4:'))

    if side1 == side2 == side3 == side4 and angle1 == angle2 == angle3 == angle4 == 90:
        print('You made a square')
    if side1 == side2 == side3 == side4 and angle1 == angle3 and angle2 == angle4 and angle1 != angle2:
        print('You made a rhombus')
    if side1 == side3 and side2 == side4 and angle1 == angle2 == angle3 == angle4 == 90 and side1 != side2:
        print('You made a rectangle')

    while True:
        answer = str(input('Would you like to repeat this? (y/n): '))
        if answer in 'Yy':
            break
        
        if answer in 'Nn':
            print('Goodbye.')
            break
        
    if answer in 'Yy':
        continue
 
    break

'''
================= RESTART: /Users/lailabahman/Desktop/shapes.py ================
Make a quadrilateral
side 1: -4
value must be positive. side 1: 4
side 2: 4
side 3: 4
side 4: 4
angle 1: -90
value must be positive. angle 1: 90
angle 2: 180
value must be less than 180. angle 2:90
angle 3: 90
angle 4: 90
You made a square
Would you like to repeat this? (y/n): y
Make a quadrilateral
side 1: 4
side 2: 4
side 3: 4
side 4: 4
angle 1: 70
angle 2: 20
angle 3: 70
angle 4: 20
You made a rhombus
Would you like to repeat this? (y/n): y
Make a quadrilateral
side 1: 5
side 2: 3
side 3: 5
side 4: 3
angle 1: 90
angle 2: 90
angle 3: 90
angle 4: 90
You made a rectangle
Would you like to repeat this? (y/n): n
Goodbye.
'''
