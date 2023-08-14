# p30.py
# Laila Bahman
# 7/17/2022
# Python 3.10.5
# Description:
'''
Write a function which has two parameters, N and M.

The function returns True if N is evenly divisible by M, and False otherwise.

Be sure to type the function name and the function calls below, copy/pasting it
will give you errors!
'''

N = int (input ('Enter integer N:') )
M = int (input ('Enter integer M:') )

print('is integer N divisible by integer M...')

def isDivisible(N, M):
    if N % M == 0:
        return True
    if N % M != 0:
        return False

print(isDivisible(N, M))

'''
================== RESTART: /Users/lailabahman/Desktop/p30.py ==================
Enter integer N:66
Enter integer M:5
is integer N divisible by integer M...
False

================== RESTART: /Users/lailabahman/Desktop/p30.py ==================
Enter integer N:4
Enter integer M:2
is integer N divisible by integer M...
True
'''
