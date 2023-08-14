# p47.py
# Laila Bahman
# 7/31/2022
# Python 3.10.5
# Description:
'''
Write a program which :

Writes a random number (50 to 55) of numbers (0 to 100) in a file
Opens the file and reads the numbers from it into a list
Sorts the list and Shows it.
Calculates the median.
Note: You may NOT use the Python built in functions: sort(), sorted(), sum(),
median()
'''
from random import randint
totalNumbers = randint(50,55)
newFile = open('randomNumbers.txt', 'w')
for i in range(0, totalNumbers, 1):
    newFile.write(str(randint(0,100)) +'\n')
newFile.close()

newFile = open('randomNumbers.txt', 'r')
fileAsLineList = newFile.read().splitlines()
print(len(fileAsLineList))
print('fileAsLineList = ', fileAsLineList)

#bubble sort:
for j in range (0, len(fileAsLineList)-1, 1):
    for i in range (0, len(fileAsLineList)-1, 1):
        if int(fileAsLineList[i]) > int(fileAsLineList[i + 1]):
            temp = fileAsLineList[i]
            fileAsLineList[i] = fileAsLineList[i + 1]
            fileAsLineList[i + 1] = temp
print('fileAsLineList = ', fileAsLineList)

# find index of median for odd numbers

if len(fileAsLineList) % 2!= 0 :
    medianIndex = int(len(fileAsLineList) / 2)
    print('medianIndex = ', medianIndex)
    median = fileAsLineList[medianIndex]
    print('median = ', median)
    
else: # if list has even number of numbers (length even)
    medianIndex2 = int(len(fileAsLineList) / 2)
    print('medianIndex2 = ', medianIndex2)
    medianIndex1 = medianIndex2 -1
    print('medianIndex1 = ', medianIndex1)
    median = (int(fileAsLineList[medianIndex1]) + int(fileAsLineList[medianIndex2])) / 2
    print('median = ', median)

'''
================== RESTART: /Users/lailabahman/Desktop/p47.py ==================
50
fileAsLineList =  ['73', '29', '50', '81', '41', '61', '69', '80', '48', '5', '10', '13', '41', '53', '31', '84', '33', '38', '40', '23', '3', '51', '94', '95', '93', '91', '32', '20', '99', '76', '31', '34', '93', '72', '19', '11', '85', '16', '84', '18', '80', '73', '44', '92', '21', '26', '49', '71', '17', '55']
fileAsLineList =  ['3', '5', '10', '11', '13', '16', '17', '18', '19', '20', '21', '23', '26', '29', '31', '31', '32', '33', '34', '38', '40', '41', '41', '44', '48', '49', '50', '51', '53', '55', '61', '69', '71', '72', '73', '73', '76', '80', '80', '81', '84', '84', '85', '91', '92', '93', '93', '94', '95', '99']
medianIndex2 =  25
medianIndex1 =  24
median =  48.5

================== RESTART: /Users/lailabahman/Desktop/p47.py ==================
51
fileAsLineList =  ['73', '84', '82', '24', '73', '61', '89', '37', '100', '77', '13', '73', '50', '34', '62', '11', '53', '27', '91', '72', '25', '89', '24', '91', '17', '97', '7', '71', '83', '52', '1', '34', '55', '16', '22', '47', '10', '24', '32', '2', '53', '56', '82', '96', '17', '67', '62', '7', '65', '63', '82']
fileAsLineList =  ['1', '2', '7', '7', '10', '11', '13', '16', '17', '17', '22', '24', '24', '24', '25', '27', '32', '34', '34', '37', '47', '50', '52', '53', '53', '55', '56', '61', '62', '62', '63', '65', '67', '71', '72', '73', '73', '73', '77', '82', '82', '82', '83', '84', '89', '89', '91', '91', '96', '97', '100']
medianIndex =  25
median =  55
'''
