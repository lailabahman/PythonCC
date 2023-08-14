# p48.py
# Laila Bahman
# 7/31/2022
# Python 3.10.5
# Description:
'''
Write a program which reads the data from file sunspots.txt
...and computes the average for each year, writing them one per line to a file
averages.txt
'''
myFile = open('sunspots.txt', 'r')
fileAsListOfLines = myFile.read().splitlines() 
myFile.close()

#print(fileAsListOfLines)
'''
aLine = fileAsListOfLines[0]
print(aLine)
lineData = aLine.split()
print(lineData)
year = lineData[0]
print('year = ', year)
sumData = 0
for i in range(1,len(lineData),1):
    sumData += float(lineData[i])
avg = sumData / (len(lineData)-1)
print('year', year,'avg %.2f' %avg)
'''

otherFile = open('averages.txt','w')
otherFile.write('year averages\n')
for j in range(0,len(fileAsListOfLines),1):
    aLine = fileAsListOfLines[j]
    #print(aLine)
    lineData = aLine.split()
    #print(lineData)
    year = lineData[0]
    #print('year = ', year)
    sumData = 0
    for i in range(1,len(lineData),1):
        sumData += float(lineData[i])
    avg = sumData / (len(lineData)-1)
    otherFile.write('%s  %.2f \n' %(year,avg))
otherFile.close()


'''    
# Open the File to Read
myFile = open('sunspots.txt', 'r')
# Read the data from file into a list
listOfLines = myFile.read().splitlines() 
# Each list item is a new line from the file
listItem = listOfLines[0].split() # split each line by spaces
print(listItem) # shows list of strings ['1945','18.5','11.8',...,'28.4']
# Convert each of the strings to float in order to do math with them!
'''

'''
================== RESTART: /Users/lailabahman/Desktop/p48.py ==================
'''
