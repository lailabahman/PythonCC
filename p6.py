# p6.py
# Laila Bahman
# 7/1/22
# Python 3.10.5
# Description:
'''
Write a program to compute a person's height.

INPUT: User will enter two whole numbers: feet and inches.
OUTPUT: Values input & total in inches.
INPUT VALIDATION: Make sure that feet and inches are positive values
Your program must run as shown below:

Please enter the number of feet:  4
Please enter the number of inches:  10
4 feet 10 inch(es) = 58 inches
'''
print('Enter your height')
feet = float(input('feet:'))
inches = float(input('inches:'))

totalInches = feet*12 + inches
print ('%.0f feet %.0f inch(es) = %.0f inches'
       %(feet,    inches,         totalInches)
      )

'''
>>>
=================== RESTART: /Users/lailabahman/Desktop/p6.py ==================
Enter your height
feet:5
inches:4
5 feet 4 inch(es) = 64 inches
>>>
'''
