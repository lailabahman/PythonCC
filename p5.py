# p5.py
# Laila Bahman
# 6/27/22
# Python 3.10.5
# Description:
'''
Write a program which computes the sum and product of two numbers entered by
the user.

Algorithm:
Ask the user to enter two numbers.
store those two numbers in 2 variables, num1, num2.
make two new variables sum = num1+ num2, and product = num1*num2
Then, output the sum and product of to the user.
'''

# enter values:
num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))

# calculate:
sum = num1 + num2
product = num1*num2

# results:
print(num1, '+', num2, '=', sum)
print(num1, 'x', num2, '=', product)

'''
>>>
=================== RESTART: /Users/lailabahman/Desktop/p5.py ==================
enter first number: 5
enter second number: 9
5 + 9 = 14
5 x 9 = 45
>>>
'''
