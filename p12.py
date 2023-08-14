# p12.py
# Laila Bahman
# 7/8/2022
# Python 3.10.5
# Description:
'''
Write a program to determine if the user can vote. The program will ask the
user a series of questions - age, citizenship and registration. The user will
receive a message as to whether or not s/he may vote -- yes, no (with a reason
- too young, not a citizen, hasn't registered to vote).
'''

age = int(input('How old are you?'))
citizen = input('Are you a U.S. citizen? (y or n)')
registered = input('Are you registered to vote? (y or n)')
if age >= 18 and citizen == 'y' and registered == 'y':
          print('Congratulations, you can vote!')
else:
    if age < 18:
        print('You must be at least 18 to vote.')
    if citizen != 'y':
        print('You must be a U.S. citizen to vote.')
    if registered != 'y':
        print('You must be registered to vote.')

'''
>>>
================== RESTART: /Users/lailabahman/Desktop/p12.py ==================
How old are you?18
Are you a U.S. citizen? (y or n)y
Are you registered to vote? (y or n)y
Congratulations, you can vote!

================== RESTART: /Users/lailabahman/Desktop/p12.py ==================
How old are you?17
Are you a U.S. citizen? (y or n)y
Are you registered to vote? (y or n)y
You must be at least 18 to vote.

================== RESTART: /Users/lailabahman/Desktop/p12.py ==================
How old are you?17
Are you a U.S. citizen? (y or n)n
Are you registered to vote? (y or n)y
You must be at least 18 to vote.
You must be a U.S. citizen to vote.

================== RESTART: /Users/lailabahman/Desktop/p12.py ==================
How old are you?17
Are you a U.S. citizen? (y or n)n
Are you registered to vote? (y or n)n
You must be at least 18 to vote.
You must be a U.S. citizen to vote.
You must be registered to vote.
>>>
'''
