# p31.py
# Laila Bahman
# 7/17/2022
# Python 3.10.5
# Description:
'''
Write a function that has an integer N as parameter and returns true if N is
even.

Hint: A number N is even if N % 2  == 0

Be sure to type the function name and the function calls below, copy/pasting
it will give you errors!
'''
n = int(input('enter integer: '))

def isEven(n):
    if n % 2 == 0:
        return True
    if n % 2 != 0:
        return False

print(n, ' is even: ', isEven(n))

'''
================== RESTART: /Users/lailabahman/Desktop/p31.py ==================
enter integer: 3
3  is even:  False

================== RESTART: /Users/lailabahman/Desktop/p31.py ==================
enter integer: 6
6  is even:  True
'''
