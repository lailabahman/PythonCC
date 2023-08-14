# p28.py
# Laila Bahman
# 7/17/2022
# Python 3.10.5
# Description:
'''
Write a function which given two integer parameters Returns their sum...unless
the two values are the same, then the function Returns their doubled sum.

Be sure to type the function name and the function calls below, copy/pasting
it will give you errors!
'''

# I want to return the sum of two numbers if they are both negative
# otherwise show the sum if they're positive

def sum_double(n1, n2):
    if n1 != n2:
        return n1 + n2
    if n1 == n2:
        return n1 *2 + n2 * 2
        
    total = n1 + n2
    print('total = ', total)

# call the function  so it returns a value
print(sum_double(1,2)) #shows 3
print(sum_double(2,2)) #shows 8

'''
================== RESTART: /Users/lailabahman/Desktop/p28.py ==================
3
8
'''
