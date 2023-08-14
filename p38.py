# p38.py
# Laila Bahman
# 7/20/2022
# Python 3.10.5
# Description:
'''
Write a program that asks the user to enter a sentence.

The program then finds the longest word in the sentence, and shows it.

Note: The use of python functions max() and sorted() is not permitted!
'''

sentence = input('please enter a sentence: ')
print('Here is the sentence you entered: ', sentence)
words = sentence.split()
print('words: ', words)

print('there are ',len(words) ,' words in the sentence')

longest = words[0]
for i in range(1, len(words), 1):  #looking for longest word
    if len(words[i]) > len(longest):
        longest = words[i]  #make variable longest = first word

print('longest word is: ', longest)
print('the word "',longest,'" has ', len(longest),' characters.')

'''
================== RESTART: /Users/lailabahman/Desktop/p38.py ==================
please enter a sentence: hello everyone i am showing you my code
Here is the sentence you entered:  hello everyone i am showing you my code
words:  ['hello', 'everyone', 'i', 'am', 'showing', 'you', 'my', 'code']
there are  8  words in the sentence
longest word is:  everyone
the word " everyone " has  8  characters.
'''
