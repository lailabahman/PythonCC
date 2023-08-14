# p27.py
# Laila Bahman
# 7/17/2022
# Python 3.10.5
# Description:
'''
Write a program that generates a random list of letters.

# start with an
empty_list = [ ]
# and use
empty_list.append(Letter) # to add letters to the list

The length of the list of letters changes every time you run the program.

There can be a random number of X  letters on the list, where X is a random
number between 50 to 75.

Each of the letters on the list is a random letter between A to F (uppercase).

Use a loop to generate the list and then Show the generated list of letters to
the user.

Count and then show to the user how many times the letter B appears.

In order to receive credit, you may not use python built-in function "count()" !
'''

from random import randint

x= randint(50,75)
emptyList = [ ]
countB = 0

for i in range(0, x, 1):
    asciiNum = randint(65,70)
    emptyList.append(chr(asciiNum)) 
    if asciiNum == 66: # 66 --> B
        countB += 1

print('generating a list of ',x, ' letters...')
print(emptyList)
print('the letter "B" appears ', countB, ' times.')

'''
================== RESTART: /Users/lailabahman/Desktop/p27.py ==================
generating a list of  51  letters...
['A', 'D', 'D', 'B', 'F', 'F', 'D', 'C', 'B', 'A', 'D', 'F', 'F', 'C', 'D', 'A', 'F', 'D', 'C', 'F', 'F', 'F', 'B', 'F', 'E', 'D', 'F', 'E', 'E', 'F', 'D', 'A', 'B', 'B', 'D', 'E', 'F', 'E', 'E', 'A', 'F', 'D', 'D', 'D', 'A', 'C', 'D', 'E', 'F', 'C', 'B']
the letter "B" appears  6  times.
'''
