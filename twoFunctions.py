# twoFunctions.py
# Laila Bahman
# 7/21/2022
# Python 3.10.5
# Description:
'''
FUNCTION 1

Write the following two function definitions, and call each function
appropriately in order to test and show how each function works.

Write and test both functions in the same twoFunctions.py file.

For full credit please submit your working program test runs, as usual. You are
not allowed to use built-in functions to sort of find median.


FUNCTION 2

Write a function named "middle" which has 3 PARAMETERS: num1, num2, num3.

The function RETURNS the middle/median value of the 3 arguments. Assume 3
different values as parameters.

You are not permitted to use built-in python functions sort(), sorted(),
median()

Note: Median is not the same as Average! Show the value that the function
returns after it was called.
'''
print('FUNCTION 1')

distance = float(input('distance traveled (miles): '))
time = float(input('time traveled (hours): '))

def speed(distance, time):
    speed = distance/time
    print('speed=', round(speed,2),'miles per hour')

speed(distance, time)

print('\nFUNCTION 2')

num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
num3 = int(input('enter third number: '))

def middle(num1, num2, num3):
    if num1 < num2 < num3 or num3 < num2 < num1:
        median = num2
    if num2 < num1 < num3 or num3 < num1 < num2:
        median = num1
    if num1 < num3 < num2 or num2 < num3 < num1:
        median = num3
    return median

print('median=', middle(num1, num2, num3))

'''
============== RESTART: /Users/lailabahman/Desktop/twoFunctions.py =============
FUNCTION 1
distance traveled (miles): 738.949
time traveled (hours): 9.826
speed= 75.2 miles per hour

FUNCTION 2
enter first number: 9
enter second number: 23
enter third number: 1
median= 9
'''
