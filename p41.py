# p41.py
# Laila Bahman
# 7/20/2022
# Python 3.10.5
# Description:
'''
Write a function which outputs as many crosses
as the parameter 'numCrosses' indicates.

def stars(numCrosses):
For example, when parameter 'numCrosses' equals 5,
the function displays the following:

+ 
+ + 
+ + + 
+ + + + 
+ + + + +
You are not allowed to use string "concatenation" or multiplication.
Also the use of a list and appending to a list is not permitted.
You must solve the problem using 2 loops (one 'for' loop nested in the other).
'''
row = int(input('enter number of rows of crosses: '))

def stars(row):
    for row in range(0, row, 1):
        print('+', end= ' ')
        for j in range (0, row, 1):
            print('+', end= ' ')
        print()
    
print(stars(row))

'''
================== RESTART: /Users/lailabahman/Desktop/p41.py ==================
enter number of rows of crosses: 9
+ 
+ + 
+ + + 
+ + + + 
+ + + + + 
+ + + + + + 
+ + + + + + + 
+ + + + + + + + 
+ + + + + + + + + 
None
'''
