# p46.py
# Laila Bahman
# 7/31/2022
# Python 3.10.5
# Description:
'''
Write a Python program to do the following:

Let the user enter a file name (such as "myMovies.txt").
Let the user enter the titles of 4 of their favorite movies using a loop.
Write using a loop the 4 movie titles to a file, one per line, and closes the
file.
Read the 4 movie titles from "myMovies.txt" using splitlines(), stores them in
a list, and then shows the list.
Write the titles in reverse order into a file "reverseOrder.txt"
'''

fileName = input('enter a file name: ')
newFile = open(fileName,'w') # makes a file named after the user input
for i in range(0,4,1):
    movie = input('enter movie title: ')
    newFile.write(movie + '\n')
newFile.close()

newFile = open(fileName,'r')
fileAsListOfLines = newFile.read().split()
newFile.close()

# if 4 lines -> fileAsListOfLines = ['one', 'two', 'three', 'four']
# INDEX                                0      1       2        3

newFile = open('reverseOrder.txt','w')
for i in range(3, -1, -1): # i = 3,2,1,0
    print('i = ', i)
    newFile.write(fileAsListOfLines[i])
    newFile.write('\n')
newFile.close()
'''
================== RESTART: /Users/lailabahman/Desktop/p46.py ==================
enter a file name: myMovies.txt
enter movie title: Jaws
enter movie title: Muppets
enter movie title: Cinderella
enter movie title: Gladiator
i =  3
i =  2
i =  1
i =  0
'''
