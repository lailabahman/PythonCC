# p33.py
# Laila Bahman
# 7/17/2022
# Python 3.10.5
# Description:
'''
If you are given three sticks, you may or may not be able to arrange them in a
triangle. For example, if one of the sticks is 12 inches long and the other two
are one inch long, you will not be able to get the short sticks to meet in the
middle.

For any three sticks, there is a simple test to see if it is possible to form a
triangle:

“If any of the three sticks is greater than the sum of the other two, then you
cannot form a triangle. Otherwise, you can.”

Write a function named isTriangle(a,b,c) that has three sides a,b,c  as
parameters.

The function returns either True or False, depending on whether you can form a
triangle from the sides with the given lengths.
'''
a = int(input('enter length a: '))
b = int(input('enter length b: '))
c = int(input('enter length c: '))

def isTriangle(a, b, c):
    if c > a + b:
        return False
    if b > a + c:
        return False
    if a > b + c:
        return False
    else:
        return True

print(isTriangle(a, b, c))

'''
================== RESTART: /Users/lailabahman/Desktop/p33.py ==================
enter length a: 2
enter length b: 5
enter length c: 3
True

================== RESTART: /Users/lailabahman/Desktop/p33.py ==================
enter length a: 6
enter length b: 1
enter length c: 2
False
'''
