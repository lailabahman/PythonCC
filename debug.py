# debug.py
# Laila Bahman
# 7/21/2022
# Python 3.10.5
# Description:
'''
Debug the program below so that it works as shown in the test run.

num = input ("Please enter a number: ")

def  isEven( ): # should have a parameter
  if  num%2 = 0
     retrn True: 
  else (num%2 != 0):
     return False

def  main(): # needs to be called first
   print ("The number %i is even: %s" , (num; iseven(num))

main

Test Run:

=== OUTPUT ===
>>> 
Enter a number: 5
The number 5 is even: False
>>> 
'''

num = int(input("Enter a number: "))
#add int() bc we want an integer

def isEven(num):
  # should have a parameter
  if num %2 == 0:
    #added space before %2 and = and :
     return True
    #spelling of return, removed :
  else:
    #add :
    num %2 != 0
    #new line, removed ( and : and space btwn 0 and before %2
    return False

def  main():
  # needs to be called first
   print ('The number', num,'is even:', isEven(num))
   #change iseven to isEven, change ; to , and add closing )

main()
#add ()

'''
================= RESTART: /Users/lailabahman/Desktop/debug.py =================
Enter a number: 5
The number 5 is even: False

================= RESTART: /Users/lailabahman/Desktop/debug.py =================
Enter a number: 4
The number 4 is even: True
'''
