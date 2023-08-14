# 43.py
# Laila Bahman
# 7/20/2022
# Python 3.10.5
# Description:
'''
The function returns the sorted list in ascending order if parameter 'reverse'
is False.
The function returns the sorted list in descending order if parameter 'reverse'
is True.
'''

aList = [5,1,4,3,2]
print('original list:', aList)

def sort(aList, reverse):
    if reverse == True:
        for i in range (0, len(aList)-1):
          for j in range (0, len(aList)-1-i): 
            if aList[j] < aList[j+1]:
              temp = aList[j]
              aList[j] = aList[j+1] 
              aList[j+1] = temp
    if reverse == False:
        for i in range (0, len(aList)-1):
          for j in range (0, len(aList)-1-i): 
            if aList[j] > aList[j+1]:
              temp = aList[j+1]
              aList[j+1] = aList[j] 
              aList[j] = temp
    return aList, reverse

print(sort(aList, True))
print(sort(aList, False))

'''
================== RESTART: /Users/lailabahman/Desktop/p43.py ==================
original list: [5, 1, 4, 3, 2]
([5, 4, 3, 2, 1], True)
([1, 2, 3, 4, 5], False)
'''

