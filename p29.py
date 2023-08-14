# p29.py
# Laila Bahman
# 7/17/2022
# Python 3.10.5
# Description:
'''
The absolute value of 1 is 1, and the absolute value of -1 is also 1.

Write a function that calculates the absolute value and returns the absolute
value of a number.

Do not just use the built-in python function abs()! You must write the
definition yourself!

Be sure to type the function name and the function calls below, copy/pasting
it will give you errors!
'''

a = float (input ('Enter a positive or negative value:') )
    
def absolute(a):
    if a >= 0:
        print ('absolute value is:', a)
    if a < 0:
        print ('absolute value of', a, 'is:', a*(-1))

print(absolute(a))

'''
================== RESTART: /Users/lailabahman/Desktop/p29.py ==================
Enter a positive or negative value:-3
absolute value of -3.0 is: 3.0
None

================== RESTART: /Users/lailabahman/Desktop/p29.py ==================
Enter a positive or negative value:20
absolute value is: 20.0
None
'''
