# p23.py
# Laila Bahman
# 7/17/2022
# Python 3.10.5
# Description:
'''
Write a program to let a child practice arithmetic skills.

The program should first ask for what kind of practice is wanted: addition(1),
subtraction(2), or multiplicatio(3)... (no division).

Then, the program will have a loop for each of the the desired operations that
lets the user repeat the practice as many times as desired,

Two random numbers will be generated (0 - 9), and the child will have to add,
subtract or multiply them.

If the child answers the question correctly, congratulate them, and give them
two different numbers to try.

If the child answers incorrectly, the problem should be repeated (with the two
same numbers).

Note: You are not allowed to use the eval() or sum() functions!

'''

from random import randint

while True:
    n1 = randint(0,9)
    n2 = randint(0,9)

    operation = input('would you like to add(+), subtract(-), or multiply(x): ')

    #ADDITION
    if operation == '+':
        answer = int(input('what is %i + %i = ' %(n1,n2)))
        #if user is wrong, ask question again
        while answer != n1 + n2:
            answer = int(input('incorrect, what is %i + %i = ' %(n1,n2)))
        if answer == n1 + n2:
            print('correct')

    #SUBTRACTION
    if operation == '-':
        answer = int(input('what is %i - %i = ' %(n1,n2)))
        while answer != n1 - n2:
            answer = int(input('incorrect, what is %i - %i = ' %(n1,n2)))
        if answer == n1 - n2:
            print('correct')

    #MULTIPLICATION
    if operation == 'x':
        answer = int(input('what is %i x %i = ' %(n1,n2)))
        while answer != n1 * n2:
            answer = int(input('incorrect, what is %i x %i = ' %(n1,n2)))
        if answer == n1 * n2:
            print('correct')

    repeat = input('would you like to try again (y/n): ')
    if repeat != 'y':
        print('thanks for playing')
        break

'''
================== RESTART: /Users/lailabahman/Desktop/p23.py ==================
would you like to add(+), subtract(-), or multiply(x): +
what is 6 + 1 = 4
incorrect, what is 6 + 1 = 7
correct
would you like to try again (y/n): y
would you like to add(+), subtract(-), or multiply(x): -
what is 5 - 4 = 2
incorrect, what is 5 - 4 = 1
correct
would you like to try again (y/n): y
would you like to add(+), subtract(-), or multiply(x): x
what is 0 x 8 = 4
incorrect, what is 0 x 8 = 0
correct
would you like to try again (y/n): n
thanks for playing
'''
    
        

