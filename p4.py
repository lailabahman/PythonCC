# p4.py
# Laila Bahman
# 6/27/22
# Python 3.10.5
# Description:

'''
Write a program that asks for a character INPUT from the keyboard and then
OUTPUTS a large block letter "C" composed of that character. For example, if
the user inputs the character "X", then the output should look as follows:

************************************************

            X X X                 
          X      X              
         X                      
        X                        
        X                          
        X                                
         X                      
          X      X              
            X X X                   
 
**************************************************
'''

x = input('Enter a letter: ')

print("************************************************")
print(" ")
print("            %s %s %s"   %(x,x,x))
print("          %s      %s"    %(x,      x))
print("         %s"            %(x))
print("        %s"              %(x))
print("        %s"              %(x))
print("        %s"              %(x))
print("         %s"            %(x))
print("          %s      %s"    %(x,      x))
print("            %s %s %s"   %(x,x,x))
print(" ")
print("************************************************")

'''
>>>
=================== RESTART: /Users/lailabahman/Desktop/p4.py ==================
Enter a letter: f
************************************************
 
            f f f
          f      f
         f
        f
        f
        f
         f
          f      f
            f f f
 
************************************************
>>>
'''
