# p57.py
# Laila Bahman
# 7/31/2022
# Python 3.10.5
# Description:
'''
In a weighted alphabet, every symbol is assigned a positive real number called
a weight.

A string formed from a weighted alphabet is called a weighted string, and its
weight is equal to the sum of the weights of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid alphabet
is the monoisotopic mass of the corresponding amino acid.

1) The mass of each possible amino acid is given in the file aa.txt
- Put the contents of the above file into a dictionary:  dictionary [ 'Letter' ]
= value

2) Ask the user to enter an amino acid string consisting of only the letters
shown in file aa.txt
- if the user enters an incorrect letter, then the program asks for another
string

3) Calculate the total weight of the amino acid
 a) use characters of the string as keys for the dictionary from (1)
 b) sum the weights for all letters and show the total weight
 
'''

myFile = open('aa.txt', 'r')
EachLineList = myFile.read().splitlines()
dictionary = {}


for i in range(0,len(EachLineList),1):
    EachLine = EachLineList[i].split()
    dictionary[EachLine[0]] = EachLine[1]   
myFile.close()


while True:
    sentence = input('Please enter the letters you would like to weight: ')
    sentence = sentence.upper()
    for i in range(0,len(sentence),1):
        if sentence[i] in ('B', 'J', 'O', 'U', 'X', 'Z'):
            break 
    else: 
         break

sum = 0
for i in range(0,len(sentence),1):
    sum += float(dictionary[sentence[i]])

print('Total weight: %.3f' %sum)

'''
================== RESTART: /Users/lailabahman/Desktop/p57.py ==================
Please enter the letters you would like to weight: abc
Please enter the letters you would like to weight: jdy
Please enter the letters you would like to weight: okl
Please enter the letters you would like to weight: uyn
Please enter the letters you would like to weight: xfr
Please enter the letters you would like to weight: zal
Please enter the letters you would like to weight: skadyek
Total weight: 821.392
'''
