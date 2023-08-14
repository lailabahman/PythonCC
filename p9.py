# p9.py
# Laila Bahman
# 7/1/2022
# Python 3.10.5
# Description:
'''
Write a program to compute a person's height and print out a message.

The user will input their height in feet and inches.

The program will convert the feet and inches into total_inches, and then print
a message.

If the total inches is greater than 72, the message should be something like,
"You're tall."
If the total inches is between 5' and 6', a different message should appear,
like "You are average"
If the total inches is less than 60, another message should appear, like "You
are vertically challenged"
'''
print('Please enter your height.')
feet = float(input('Feet:'))
inches = float(input('Inches:'))
totalInches = feet*12 + inches
print('%.0f feet %.0f inch(es) = %.0f inches'
      %(feet,    inches,         totalInches)
      )
if totalInches > 72:
    print("You're tall.")
if totalInches < 72 and totalInches > 60:
          print("You're average.")
if totalInches < 60:
          print("You're vertically challenged")

'''
>>>
=================== RESTART: /Users/lailabahman/Desktop/p9.py ==================
Please enter your height.
Feet:8
Inches:1
8 feet 1 inch(es) = 97 inches
You're tall.
>>>
=================== RESTART: /Users/lailabahman/Desktop/p9.py ==================
Please enter your height.
Feet:5
Inches:6
5 feet 6 inch(es) = 66 inches
You're average.
>>>
=================== RESTART: /Users/lailabahman/Desktop/p9.py ==================
Please enter your height.
Feet:3
Inches:3
3 feet 3 inch(es) = 39 inches
You're vertically challenged
>>>
'''
