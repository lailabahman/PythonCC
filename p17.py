# p17.py
# Laila Bahman
# 7/8/2022
# Python 3.10.5
# Description:
'''
Suppose that the tuition for a university is $10,000 this year and increases 5%
every year.

Write a program that computes the tuition in ten years and displays a table of
the years and tuition costs. A loop must be used.
'''
tuition = 10000
for year in range(1,10,1):
    print ("Year %2i"  %year, ", Tuition = %.2f" %tuition)
    tuition = tuition + tuition * 0.05

'''
>>>
================== RESTART: /Users/lailabahman/Desktop/p17.py ==================
Year  1 , Tuition = 10000.00
Year  2 , Tuition = 10500.00
Year  3 , Tuition = 11025.00
Year  4 , Tuition = 11576.25
Year  5 , Tuition = 12155.06
Year  6 , Tuition = 12762.82
Year  7 , Tuition = 13400.96
Year  8 , Tuition = 14071.00
Year  9 , Tuition = 14774.55
>>>
'''
