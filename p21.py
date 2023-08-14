# p21.py
# Laila Bahman
# 7/8/2022
# Python 3.10.5
# Description:
'''
Which of the below gives you more money?

1) A penny which doubles it's value every day over 30 days, or

2) A million dollars

Write a program which calculates exactly how much more (or less) you can make
with the penny on day 30. A loop must be used.
'''

penny = 1
for day in range(0,31,1):
    penny = penny * 2
    if day == 30:
        print('On the 30th day, there are')
        print( '{:,}'.format(penny), 'cents, or ', penny/100, 'dollars')
        x = 1000000 - penny/100
        if x < 0:
            print("You get $",abs(x), " more from a penny that doubles it's value every day over 30 days than a million dollars.")
        if x > 0:
            print("You get $",x, " more from a million dollars than a penny that doubles it's value every day over 30 days.")


'''
================== RESTART: /Users/lailabahman/Desktop/p21.py ==================
On the 30th day, there are
2,147,483,648 cents, or  21474836.48 dollars
You get $ 20474836.48  more from a penny that doubles it's value every day over 30 days than a million dollars.
'''
