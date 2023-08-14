# p18.py
# Laila Bahman
# 7/8/2022
# Python 3.10.5
# Description:
'''
Write a program that displays the characters in the ASCII character table from
! to ~.

Display ten characters per line.

The characters are separated by exactly one space.
'''
count = 0
for asciiValue in range(33,43,1):
        print(chr(asciiValue), end = ' ')
        count = count + 1 
        if count == 10:
           print() 
           count = 0
for asciiValue in range(43,53,1):
        print(chr(asciiValue), end = ' ')
        count = count + 1 
        if count == 10:
           print() 
           count = 0
for asciiValue in range(53,63,1):
        print(chr(asciiValue), end = ' ')
        count = count + 1 
        if count == 10:
           print() 
           count = 0
for asciiValue in range(63,73,1):
        print(chr(asciiValue), end = ' ')
        count = count + 1 
        if count == 10:
           print() 
           count = 0
for asciiValue in range(73,83,1):
        print(chr(asciiValue), end = ' ')
        count = count + 1 
        if count == 10:
           print() 
           count = 0
for asciiValue in range(83,93,1):
        print(chr(asciiValue), end = ' ')
        count = count + 1 
        if count == 10:
           print() 
           count = 0
for asciiValue in range(93,103,1):
        print(chr(asciiValue), end = ' ')
        count = count + 1 
        if count == 10:
           print() 
           count = 0
for asciiValue in range(103,113,1):
        print(chr(asciiValue), end = ' ')
        count = count + 1 
        if count == 10:
           print() 
           count = 0
for asciiValue in range(113,123,1):
        print(chr(asciiValue), end = ' ')
        count = count + 1 
        if count == 10:
           print() 
           count = 0
for asciiValue in range(123,127,1):
        print(chr(asciiValue), end = ' ')
        count = count + 1 
        if count == 10:
           print() 
           count = 0

'''
>>>
================== RESTART: /Users/lailabahman/Desktop/p18.py ==================
! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = > 
? @ A B C D E F G H 
I J K L M N O P Q R 
S T U V W X Y Z [ \ 
] ^ _ ` a b c d e f 
g h i j k l m n o p 
q r s t u v w x y z 
{ | } ~
>>>
'''







