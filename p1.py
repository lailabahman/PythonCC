# Program name: p1.py
# Your name: Laila Bahman
# Python Version: 3.10.5
# Date Started - Date Finished: 6/27/22
# Description: Using Python to program and show an output
'''
1.   Type up the Example program output.py program (don't copy/paste), including
the comments, and get it working.

2.   When the program runs, copy/paste how the program ran (in the Shell window)
at the bottom of your program as a multi-line comment '''     ''', then save
the file

3.   Submit output.py
'''

print('hello world') # single quote
print("hello world") # double qoutes (same as single quote in Python only)
print("he\nllo") # \n means insert a new line (same as pressing enter)

myName = "Laila" # declare/initialize string variable myName
Weight = 148.3781 # declare/initialize float variable Weight
Age = 18 # declare/initialize int variable Age
Grades = "[98,95,88]"
nameZ = ["Laila", "Bahman"]

print("Hello", myName)
print("Your weight is", Weight, "pounds. Your age is", Age, "years.")
print("Your weight is %.2f pounds. Your age is %i years." %(Weight, Age))
print("Lists: grades =", Grades, "nameZ=", nameZ)
print("This is how you print", end='')
print("on the same line")

'''
>>>
=================== RESTART: /Users/lailabahman/Desktop/p1.py ==================
hello world
hello world
he
llo
Hello Laila
Your weight is 148.3781 pounds. Your age is 18 years.
Your weight is 148.38 pounds. Your age is 18 years.
Lists: grades = [98,95,88] nameZ= ['Laila', 'Bahman']
This is how you printon the same line
>>>
'''
