# p20.py
# Laila Bahman
# 7/8/2022
# Python 3.10.5
# Description:
'''
Write a program that reads in X whole numbers and outputs (1) the sum of all
positive numbers, (2) the sum of all negative numbers, and (3) the sum of all
positive and negative numbers. The user can enter the X numbers in any different
order every time, and can repeat the program if desired.
'''
while True:
    x = int(input('How many numbers would you like to enter?: '))

    Sum = 0
    sumNeg = 0
    sumPos = 0

    for index in range(0, x, 1):
        number = float(input('Enter number %i:' %(index+1)))
        Sum += number

        if number < 0:
            sumNeg += number

        if number > 0:
            sumPos += number

    print('Sum of all numbers= ', Sum)
    print('Sum of negative numbers = ', sumNeg)
    print('Sum of positive numbers = ', sumPos)

    while True:
        answer = str(input('Would you like to repeat this? (y/n): '))

        if answer in 'Yy':
            break
        
        if answer in 'Nn':
            print('Goodbye.')
            break
        
    if answer in 'Yy':
        continue
 
    break


'''
================== RESTART: /Users/lailabahman/Desktop/p20.py ==================
How many numbers would you like to enter?: 3
Enter number 1:-65
Enter number 2:32
Enter number 3:-16
Sum of all numbers=  -49.0
Sum of negative numbers =  -81.0
Sum of positive numbers =  32.0
Would you like to repeat this? (y/n): y
How many numbers would you like to enter?: 4
Enter number 1:-7
Enter number 2:340
Enter number 3:-76
Enter number 4:2
Sum of all numbers=  259.0
Sum of negative numbers =  -83.0
Sum of positive numbers =  342.0
Would you like to repeat this? (y/n): n
Goodbye.
'''
