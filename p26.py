# p26.py
# Laila Bahman
# 7/17/2022
# Python 3.10.5
# Description:
'''
Write a program that generates a random list of numbers.

(start with an empty list and use append() )

The length of the list X can be a random number between 15 to 20.

Each of the random numbers on the list can be between 2 to 5.

Count how many times the number 3 appears.

You are not allowed to use python built-in function "count()" or you'll get a
Zero!
'''

from random import randint
x = randint(15,20)
print('Generating a list of ', x, ' numbers...')
aList = [] # make an empty list
for i in range(0,x,1):
    number = randint(2,5)
    print(number, end=',')
    aList.append(number) # add random numbers to the list
# count how many times 3 is in the list
count3 = 0
for i in range(0,x,1):
    if aList[i] == 3: # if you find a 3
        count3 += 1 # add 1 to count3
print('\n',3, "was found", count3, "times")

'''
================== RESTART: /Users/lailabahman/Desktop/p26.py ==================
Generating a list of  15  numbers...
2,2,2,5,2,4,5,4,4,3,2,3,4,3,2,
 3 was found 3 times
'''
