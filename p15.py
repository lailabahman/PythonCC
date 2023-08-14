# p15.py
# Laila Bahman
# 7/8/2022
# Python 3.10.5
# Description:
'''
Write a program that asks the user to enter 4 numbers (positive or negative).

The program shows:

the sum of all numbers (sumAll)
the sum of positive numbers (sumPos),
the sum of negative numbers (sumNeg)
The Algorithm for this problem:

sumNeg is going to hold the total of all negative numbers, it starts at zero (0)
sumPos is going to hold the total of all positive numbers, it starts at zero (0)
if a number is negative you ADD it to sumNeg
if a number is positive you ADD it to sumPos
'''
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))
sumAll = 0
sumAll = a+b+c+d
print('The sum of all numbers is ', sumAll)
sumNeg = 0
if a < 0:
    sumNeg = sumNeg + a
if b < 0:
    sumNeg = sumNeg + b
if c < 0:
    sumNeg = sumNeg + c
if d < 0:
    sumNeg = sumNeg + d
print('The sum of the negative numbers is', sumNeg)
sumPos = 0
if a > 0:
    sumPos = sumPos + a
if b > 0:
    sumPos = sumPos + b
if c > 0:
    sumPos = sumPos + c
if d > 0:
    sumPos = sumPos + d
print('The sum of the positive numbers is', sumPos)

'''
>>>
================== RESTART: /Users/lailabahman/Desktop/p15.py ==================
Enter first number:-45
Enter second number:92
Enter third number:77
Enter fourth number:-81
The sum of all numbers is  43
The sum of the negative numbers is -126
The sum of the positive numbers is 169
>>>
'''
