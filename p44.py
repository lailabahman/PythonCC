# p44.py
# Laila Bahman
# 7/21/2022
# Python 3.10.5
# Description:
'''
You have 1000 lockers and 1000 students. All lockers are initially locked.

1st student opens all lockers

2nd student closes every other locker

3rd student opens(if closed) or closes (if open) every 3rd locker

4th student opens(if closed) or closes (if open) every 4th locker

.

.

.

1000th student opens(if closed) or closes (if open) every 1000th locker

Write a program to determine which exact locker numbers are open, and total
number that are open.

You are not allowed to use Python function  count()!!
'''

lockers = []
for i in range(0,1000,1):
    lockers.append(1) # fill list w 1000 1s

for i in range(0,1000,1):
    lockers[i] = 0

for i in range(0,1000,2):
    lockers[i] = 1

for j in range(3,1001,1):   #open and close for students 3-1000
    for i in range(0,1000,j):
        if lockers[i] == 0:
            lockers[i] = 1
        elif lockers[i] == 1:
            lockers[i] = 0

count = 0
for i in range(0,1000,1):
    if lockers[i] == 0:
        count += 1
        print('lockers',i,'is open')

print('there are',count,'open lockers')

'''
================== RESTART: /Users/lailabahman/Desktop/p44.py ==================
lockers 1 is open
lockers 4 is open
lockers 9 is open
lockers 16 is open
lockers 25 is open
lockers 36 is open
lockers 49 is open
lockers 64 is open
lockers 81 is open
lockers 100 is open
lockers 121 is open
lockers 144 is open
lockers 169 is open
lockers 196 is open
lockers 225 is open
lockers 256 is open
lockers 289 is open
lockers 324 is open
lockers 361 is open
lockers 400 is open
lockers 441 is open
lockers 484 is open
lockers 529 is open
lockers 576 is open
lockers 625 is open
lockers 676 is open
lockers 729 is open
lockers 784 is open
lockers 841 is open
lockers 900 is open
lockers 961 is open
there are 31 open lockers
'''
