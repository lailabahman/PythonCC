# p10.py
# Laila Bahman
# 7/1/2022
# Python 3.10.5
# Description:
'''
Write a program which asks the user for a student's grade as a percent, and
then returns their letter grade.

Validate the input to make sure that the number is between 0 - 100 . If for
any other number, say "ERROR" and ask for another number)

A is 90% or above
B is between 80% and 90%
C is between 70% and 80%
D is between 60% and 70%
F is under 60%
'''
percent = float(input('Please enter grade as a percent:'))
if percent < 0 or percent > 100:
                print('ERROR: percent must be between 0 to 100.')
                percent = float(input('Enter value between 0 to 100:'))
if percent >= 90 and percent <= 100:
                print('The grade is A')
if percent >= 80 and percent <= 90:
                print('The grade is B')
if percent >= 70 and percent <= 80:
                print('The grade is C')
if percent >= 60 and percent <= 70:
                print('The grade is D')
if percent <= 50:
                print('The grade is F')
'''
>>>
================== RESTART: /Users/lailabahman/Desktop/p10.py ==================
Please enter grade as a percent:89
The grade is B
>>>
'''
