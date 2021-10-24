#Write a Python program to append a new item to the end of the array
# Once added, print the total length of the array together with the new array
#Original array: array('i', [1, 3, 5, 7, 9])

#Sample Output:
#Enter an element to append to the list: 11
#New array length is: 6 array is:[1, 3, 5, 7, 9, 11]

# work with list, not array
myList = []
# ask for size of list
size = 0
while not type(size) is int or not size > 0:
  try:
    size = int(input("Size of list: "))
  except:
    print("Error - please input positive integer number.")
# ask for each element
for i in range(size):
  myList.append(input(f"Add element {i+1}: "))
# print list
print("Your list:", myList)
# ask for element to add
add_element = ""
myList.append(input("Please add element: "))
# print list and size of list
print("Your list of size", len(myList), "is:", myList)
