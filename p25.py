# p25.py
# Laila Bahman
# 7/17/2022
# Python 3.10.5
# Description:
'''
Write a program that asks the user to input a sentence.

The program will ask the user what two letters are to be counted.

You must use a “for” loop to go through the sentence & count how many times the
chosen letter appears in the sentence.

You are not allowed to use python built-in function "count()" or you'll get a
Zero!

Output will show the sentence, the letter, and the number of times the letter
appears in the sentence.
'''

sentence = input('Please enter a sentence: ')
letter1 = input('Please enter the first letter to be counted: ')
letter2 = input('Please enter the second letter to be counted: ')
count1 = 0
count2 = 0
for i in range(0,len(sentence), 1):
    if sentence[i] == letter1:
        count1 += 1
    if sentence[i] == letter2:
        count2 += 1
print(letter1, "was found", count1, "times")
print(letter2, 'was found', count2, 'times')


'''
================== RESTART: /Users/lailabahman/Desktop/p25.py ==================
Please enter a sentence: hello world i am learning python
Please enter the first letter to be counted: e
Please enter the second letter to be counted: a
e was found 2 times
a was found 2 times
'''
