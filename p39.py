# p39.py
# Laila Bahman
# 7/20/2022
# Python 3.10.5
# Description:
'''
Write a program that asks the user to enter a sentence.
Your program will:

Show how many words are in the sentence 
Show the last word of the sentence
Ask the user to enter their own word, and count how many times their word
appears in the sentence
Note: you can't use the built-in python function count() to do this!
'''

sentence = input('enter a sentence: ')
print('the sentence entered: ', sentence)
words = sentence.split()
print('words in the sentence: ', words)
print('there are ', len(words),' words in the sentence')
print('first word: ', words[0])
print('last word: ', words[len(words)-1])
#INDEX 0,1,2,3,4 ... five words is index 4, so last word of 5 is len(words)-1

word = input('enter a word: ')
count = 0
for i in range(0, len(words), 1):
    if words[i] == word:
        count += 1


print('the word', word,'appears', count,'times')

'''
================== RESTART: /Users/lailabahman/Desktop/p39.py ==================
enter a sentence: hello everyone i want to show my code
the sentence entered:  hello everyone i want to show my code
words in the sentence:  ['hello', 'everyone', 'i', 'want', 'to', 'show', 'my', 'code']
there are  8  words in the sentence
first word:  hello
last word:  code
enter a word: code
the word code appears 1 times
'''
