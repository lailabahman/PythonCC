# p42.py
# Laila Bahman
# 7/20/2022
# Python 3.10.5
# Description:
'''
Write the below 5 functions according to the following requirements:

sum (list_parameter) : returns the sum of numbers inside a list
average (list_parameter) : returns the average of numbers inside a list
min (list_parameter) : returns the smallest of all numbers inside a list
max (list_parameter) : returns the largest of all numbers inside a list
main () : calls all the other functions above
'''
x = int(input('how many numbers would you like to enter? '))
aList = []
for d in range(0, x, 1):
    num = int(input('enter number %i: '%(d+1)))
    aList.append(num)


def sum(aList):
    total = 0
    for i in range(0, len(aList), 1):
        total += aList[i]
    return total

def avg(aList):
    for i in range(0, len(aList), 1):
        total = sum(aList)/len(aList)
    return total


def min(aList):
    smallest = aList[0]
    for i in range(1, len(aList), 1):
        if aList[i] < smallest:
            smallest = aList[i]
    return smallest

def max(aList):
    greatest = aList[0]
    for i in range(1, len(aList), 1):
        if aList[i] > greatest:
            greatest = aList[i]
    return greatest
    
def main():
    print('sum:', sum(aList))
    print('average:', avg(aList))
    print('min:', min(aList))
    print('max:', max(aList))

main()

'''
================== RESTART: /Users/lailabahman/Desktop/p42.py ==================
how many numbers would you like to enter? 6
enter number 1: 32
enter number 2: 66
enter number 3: 58
enter number 4: 2
enter number 5: 43
enter number 6: 7
sum: 208
average: 34.666666666666664
min: 2
max: 66
'''
