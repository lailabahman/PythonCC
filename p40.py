# p40.py
# Laila Bahman
# 7/20/2022
# Python 3.10.5
# Description:
'''
Ask the user to enter X numbers into a list. Calculate and show the sum,
average, min, max of those numbers.

Note: You are not allowed to use any pre-existing python functions such as
sample(), sum(), min(), max(), average(), sort(), sorted()!!!...unless you
write them yourself.
'''

X = int(input('How many numbers would you like to enter? '))
aList = []
for d in range(0, X, 1):
    num = int(input('please enter number %i : ' %(d + 1)))
    aList.append(num)
print('you entered:', aList)
print('there are', len(aList),'numbers in the list')

sumOfValues = 0
for index in range (0, len(aList), 1):
    sumOfValues = sumOfValues + aList[index]
print('the sum is:', sumOfValues)

avg = sumOfValues / len(aList)
print('the average is:', avg)

smallest = aList[0]
for i in range(1, len(aList), 1):
    if aList[i] < smallest:
        smallest = aList[i]
print('smallest is', smallest)

greatest = aList[0]
for i in range (1, len(aList), 1):
    if aList[i] > greatest:
        greatest = aList[i]
print('largest is', greatest)

'''
================== RESTART: /Users/lailabahman/Desktop/p40.py ==================
How many numbers would you like to enter? 6
please enter number 1 : 23
please enter number 2 : 86
please enter number 3 : 4
please enter number 4 : 2
please enter number 5 : 77
please enter number 6 : 4
you entered: [23, 86, 4, 2, 77, 4]
there are 6 numbers in the list
the sum is: 196
the average is: 32.666666666666664
smallest is 2
largest is 86
'''
