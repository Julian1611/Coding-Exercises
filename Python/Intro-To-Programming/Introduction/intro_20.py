#Write a Python program to delete an existing item from the array

#Sample Input: which element nb you want to deleted?
# 3

#Original array: array('i', [1, 3, 5, 7, 9])

#Delete array nb 4:
#New array: array('i', [1, 3, 7, 9, 11])

#from array import *

### code starts here ###
# work with lists instead of arrays
myList = []
# ask for amount of elements
amount = ""
while not type(amount) is int or not amount > 0:
  try:
    amount = int(input("How many elements: "))
  except:
    print("Error - please input positive integer number.")
# ask for each element
for i in range(amount):
  myList.append(input("Add an element: "))
# print list
print("Your list:", myList)
# ask which element should be deleted
delete = ""
while not type(delete) is int or not delete in range(1, amount+1):
  try:
    delete = int(input("What element number do you want to delete? "))
  except:
    print(f"Error - please input integer number in range 1 to {amount}")
# delete element
