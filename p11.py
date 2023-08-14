# p11.py
# Laila Bahman
# 7/1/2022
# Python 3.10.5
# Description:
'''
Write a program to simulate rock-paper-scissors game.

Each players enters 'R', 'P', 'S' or 1, 2, 3 for Rock, Paper, Scissors.

The program then shows the winner on the basis of:

Paper covers Rock
Rock breack Scissors
Scissors cut Paper
Tie
Test your program multiple times to makes sure it works! Submit all 4 of your
tests as a comment.

Extra challenge: Have the Player 2 number be randomly generated by the computer
(not entered by the user).
'''
players = float(input('Enter number of players (up to 2):'))
if players > 2 or players < 1:
    print('invalid entry')
if players == 1:
    p1 = int(input('enter 1 for rock, 2 for paper, 3 for scissors:'))
    from random import randint
    randomNum = randint(1,3)
    rock = 1
    paper = 2
    scissors = 3
    if p1 == rock and randomNum == scissors:
        print("you win, rock breaks scissors")
    elif p1 == rock and randomNum == paper:
        print('you lose, paper covers rock')
    elif p1 == rock and randomNum == rock:
        print("tie")
        
    elif p1 == paper and randomNum == scissors:
        print('you lose, scissors cut paper')
    elif p1 == paper and randomNum == paper:
        print('tie')
    elif p1 == paper and randomNum == rock:
        print("you win, paper covers rock")
        
    elif p1 == scissors and randomNum == paper:
        print ("you win, scissors cut paper")
    elif p1 == scissors and randomNum == rock:
        print("you lose, rock breaks scissors")
    elif p1 == scissors and randomNum == scissors:
            print('tie')
    

if players == 2:
    p1 = int(input('p1 enter 1 for rock, 2 for paper, 3 for scissors:'))
    p2 = int(input('p2 enter 1 for rock, 2 for paper, 3 for scissors:'))
    print('p1 =', p1)
    print('p2 =', p2)
    rock = 1
    paper = 2
    scissors = 3
    if p1 == rock and p2 == scissors:
        print("you win, rock breaks scissors")
    elif p1 == rock and p2 == paper:
        print('you lose, paper covers rock')
    elif p1 == rock and p2 == rock:
        print("tie")
        
    elif p1 == paper and p2 == scissors:
        print('you lose, scissors cut paper')
    elif p1 == paper and p2 == paper:
        print('tie')
    elif p1 == paper and p2 == rock:
        print("you win, paper covers rock")
        
    elif p1 == scissors and p2 == paper:
        print ("you win, scissors cut paper")
    elif p1 == scissors and p2 == rock:
        print("you lose, rock breaks scissors")
    elif p1 == scissors and p2 == scissors:
            print('tie')
'''
>>>
================== RESTART: /Users/lailabahman/Desktop/p11.py ==================
Enter number of players (up to 2):1
enter 1 for rock, 2 for paper, 3 for scissors:1
you lose, paper covers rock
>>>
================== RESTART: /Users/lailabahman/Desktop/p11.py ==================
Enter number of players (up to 2):2
p1 enter 1 for rock, 2 for paper, 3 for scissors:2
p2 enter 1 for rock, 2 for paper, 3 for scissors:3
p1 = 2
p2 = 3
you lose, scissors cut paper
>>>
'''