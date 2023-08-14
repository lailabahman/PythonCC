# p32.py
# Laila Bahman
# 7/17/2022
# Python 3.10.5
# Description:
'''
Write a function multAdd(a,b,c)  that Returns a*b+c.

Write a main() function which calls the multAdd(a,b,c) function.

Pass the three arguments such as 1, 2, 3 from the call in the main()
'''

a = int(input('integer a: '))
b = int(input('integer b: '))
c = int(input('integer c: '))

def multAdd(a, b, c):
    print('solution: ', a * b + c)

def main():
    print(multAdd(a, b, c))

main()

'''
================== RESTART: /Users/lailabahman/Desktop/p32.py ==================
integer a: 3
integer b: 1
integer c: 7
solution:  10
None
'''
