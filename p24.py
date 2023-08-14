# p24.py
# Laila Bahman
# 7/17/2022
# Python 3.10.5
# Description:
'''
Write a program that generates X random integers Num.

Num is a random number between 20 to 50. 

X is a random number between 10 to 15.

Calculate and show the Smallest, Largest, Sum, and Average of those numbers.

You are not allowed to use Python functions sample(), min(), max(), average(),
sort(), sorted()!!
'''

from random import randint

X = randint(10,15)

print('X = ', X)
sum = 0
for i in range(0, X, 1):

    number = randint(20,50)
    sum += number
    print(number, end=',')

    #first random number is when i=0
    if i == 0: #if it is the first number
        smallest = number

    else: #if it is any number after the first
        if number < smallest: #if any number is smaller
            smallest = number # that is your new smallest

    if i == 0:
        greatest = number

    else:
        if number > greatest:
            greatest = number


print('\nsmallest = ', smallest)
print('greatest = ', greatest)
print('sum = ', sum)
print('avergae = ', sum/X)

'''
================== RESTART: /Users/lailabahman/Desktop/p24.py ==================
X =  10
28,27,36,35,25,31,43,46,40,28,
smallest =  25
greatest =  46
sum =  339
avergae =  33.9
'''
