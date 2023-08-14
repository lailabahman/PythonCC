# p13.py
# Laila Bahman
# 7/8/2022
# Python 3.10.5
# Description:
'''
Write a program to convert any given number of total cents (under 100) into
the correct number of: quarters, dimes, nickels, pennies.
'''

totalCents = int(input('Enter total cents:'))
quarters = int(totalCents/25)
if quarters > 0:
        print('You have', quarters, 'quarters.')
        totalCents = totalCents - quarters*25 #total number of cents remaining
dimes = int(totalCents/10)
if dimes > 0:
        print('You have', dimes, 'dimes.')
        totalCents = totalCents - dimes*10 #total number of cents remaining
nickels = int(totalCents/5)
if nickels > 0:
        print('You have', nickels, 'nickels.')
        totalCents = totalCents - nickels*5 #total number of cents remaining
pennies = int(totalCents)
if pennies > 0:
        print('You have', pennies, 'pennies.')
        totalCents = totalCents - pennies
'''
>>>
================== RESTART: /Users/lailabahman/Desktop/p13.py ==================
Enter total cents:66
You have 2 quarters.
You have 1 dimes.
You have 1 nickels.
You have 1 pennies.
>>>
'''
