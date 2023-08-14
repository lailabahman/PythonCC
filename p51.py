# p51.py
# Laila Bahman
# 7/31/2022
# Python 3.10.5
# Description:
'''
1) Create a Date class.

1a) The class should have 3 properties (instance variables):

month
day
year

1b) The class should have 2 actions (functions / methods) :

setDate()  - allows the user to enter a date in 12/31/02 format 
showDate() - displays the date. 
2) Create an instance of the Date class.

3) Test the object's setDate() and showDate() methods.

4) Submit your program code, including the test run at the bottom of your code.
'''
class date:
    def __init__(self):
        self.month = '07'
        self.day = '03'
        self.year = '03'

    def showDate(self):
        print('month =', self.month,', day =', self.day,', year =', self.year)
        print(self.month,'/',self.day,'/',self.year)

    def setDate(self, newMonth, newDay, newYear):
        self.month = newMonth
        self.day = newDay
        self.year = newYear

    def getMonth(self):
        return self.month
    def getDay(self):
        return self.day
    def getYear(self):
        return self.year

class aDay:
    def __init__(self, newMonth, newDay, newYear):
        self.month = newMonth
        self.day = newDay
        self.year = newYear

    def showDate(self):
        print('month =', self.month,', day =', self.day,', year =', self.year)
        print(self.month,'/',self.day,'/',self.year)

me = date()
you = aDay('06','04', '07')
you2 = aDay('12','24','23')

me.showDate()
you.showDate()
you2.showDate()

'''
================== RESTART: /Users/lailabahman/Desktop/p51.py ==================
month = 07 , day = 03 , year = 03
07 / 03 / 03
month = 06 , day = 04 , year = 07
06 / 04 / 07
month = 12 , day = 24 , year = 23
12 / 24 / 23
'''

