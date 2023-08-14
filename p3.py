# Program name: p3.py
# Your Name: Laila Bahman
# Python Version: 3.10.5
# Date Started - Date Finished: 6/27/22 
# Description:
'''
1. Type up the Example input.py program below, including the comments, and get
it working.

2. When the program runs, copy/paste the Output (in BLUE) at the bottom of your
program as a multi-line comment '''     ''', then save the file.

3. Submit input.py
'''
name = input('Please enter your name: ') # this is a string
weightlbs = float(input('Please enter your weight in lbs: ')) # a float
age = int(input("Please enter your age (whole number): ")) # an integer
weightKg = weightlbs*0.453592
title = "Human"

print('Hello', title, name, 'your weight is')
print(weightlbs, 'lbs')
print('which equals = %.2f' %weightKg, end=' ') # end=' ' prevents new line
print('kilograms')

'''
>>>
=================== RESTART: /Users/lailabahman/Desktop/p3.py ==================
Please enter your name: Laila
Please enter your weight in lbs: 148
Please enter your age (whole number): 18
Hello Human Laila your weight is
148.0 lbs
which equals = 67.13 kilograms
>>>
'''
