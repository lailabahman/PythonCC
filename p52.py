# p52.py
# Laila Bahman
# 7/31/2022
# Python 3.10.5
# Description:
'''
Create a class Item which has
- instance variables: itemName, itemCost
- class variable: numberItems (gets increased every time a new Item is created)
- a default constructor that allows the user to set itemName and itemCost
( the default constructor sets itemName="apple" itemCost=2.49 if the user does
not specify them)
- function to show() the item name and cost
- function to get() and set() the item name and cost

Create a list named groceryBag to store the objects:
- Fill the list with several Item's such as eggs, milk, carrots, bread, apples,
each with different price.
- use Item.numberItems to show how many items you have created.
- use a loop to calculate and show the totalCost for all the items in the bag
'''

class Item:
    numberItems = 0

    def __init__(self, itemName = "apple", itemCost = 2.49):
        
        self.name = itemName
        self.cost = itemCost

        Item.numberItems += 1

    def show(self):
        print('item = ', self.name, ', cost = ', self.cost)
    def setCost(self, itemCost):
        self.cost = itemCost
    def setName(self, itemName):
        self.name = itemName
    def getCost(self):
        return self.cost
    def getName(self):
        return self.name

anItem = Item()

anItem.show()

print('number of items =', Item.numberItems)

anotherItem = Item("avacado", 1.50)
anotherItem.show()

print('number of items=', Item.numberItems)

item3 = Item("milk", 4.25)

print('number of items=', Item.numberItems)

groceryBag = []

groceryBag.append(anItem)
groceryBag.append(anotherItem)
groceryBag.append(item3)

groceryBag[0].show()
groceryBag[1].show()
groceryBag[2].show()
for i in range(0, len(groceryBag),1):
    groceryBag[i].show()
    
totalCost = 0
for i in range(0, len(groceryBag),1):
    totalCost += groceryBag[i].getCost()
print('totalCost =', totalCost)

'''
================== RESTART: /Users/lailabahman/Desktop/p52.py ==================
item =  apple , cost =  2.49
number of items = 1
item =  avacado , cost =  1.5
number of items= 2
number of items= 3
item =  apple , cost =  2.49
item =  avacado , cost =  1.5
item =  milk , cost =  4.25
item =  apple , cost =  2.49
item =  avacado , cost =  1.5
item =  milk , cost =  4.25
totalCost = 8.24
'''
