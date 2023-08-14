# p22.py
# Laila Bahman
# 7/17/2022
# Python 3.10.5
# Description:
'''
Write a Dice Game program that generates two random dice values between 1 and 6
for you, and 2 for the computer.

You get to roll as many times as you like (if you don't like your 2 dice), while
the computer only rolls once, after you have decided that you like your two dice. 

Determine who wins, you or the computer.
'''

from random import randint

while True: # loop continues forever...
    d1 = randint(1,6)
    d2 = randint(1,6)

    keep = input('you rolled %i and %i for a total of %i, keep? (y/n):' %(d1,d2,d1+d2))
    if keep == 'y':
        break #...until the user enters a letter 'y'
pc1 = randint(1,6)
pc2 = randint(1,6)

print('the computer rolled %i and %i for a total of %i.' %(pc1,pc2,pc1+pc2))

# check winner
if pc1 + pc2 > d1 + d2:
    print('computer wins')
elif pc1 + pc2 < d1 + d2:
    print('player wins')
else:
    print('tie')

'''
================== RESTART: /Users/lailabahman/Desktop/p22.py ==================
you rolled 4 and 5 for a total of 9, keep? (y/n):n
you rolled 4 and 6 for a total of 10, keep? (y/n):y
the computer rolled 6 and 4 for a total of 10.
tie

================== RESTART: /Users/lailabahman/Desktop/p22.py ==================
you rolled 1 and 6 for a total of 7, keep? (y/n):n
you rolled 1 and 1 for a total of 2, keep? (y/n):y
the computer rolled 1 and 6 for a total of 7.
computer wins

================== RESTART: /Users/lailabahman/Desktop/p22.py ==================
you rolled 4 and 5 for a total of 9, keep? (y/n):n
you rolled 2 and 1 for a total of 3, keep? (y/n):n
you rolled 6 and 5 for a total of 11, keep? (y/n):y
the computer rolled 4 and 2 for a total of 6.
player wins
'''
