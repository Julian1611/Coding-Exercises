#Given three integers. Determine how many of them are equal to each other. The program must print one of the numbers: 3 (if all are same), 2 (if two of them are equal to each other and the third one is different) or 0 (if all numbers are different).

#Example input
#10
#5
#10

#Example output
#2

# Read an integer:
# a = int(input())
# Print a value:
# print(a)

# import counter from collections to count if numbers in list are double or triple
from collections import Counter

a = ""
b = ""
c = ""
# get integers for a, b, c
while not type(a) is int or not type(b) is int or not type(c) is int:
  try:
    a = int(input("First integer: "))
    b = int(input("Second integer: "))
    c = int(input("Third integer: "))
  except:
    print("Error - input integer number!")
# put a, b, c in list
myList = [a, b, c]
# create list counter
counter = Counter(myList)
for i in counter:
  # check if values are twice or more in that list
  # print, if so, break loop after to avoid printing 0
  if counter[i] > 1:
    print(counter[i])
    break
  # else if last number, and still no doubles or triples found, must be true there is no twice or thrice number
  elif myList.index(i) == 2:
    print(0)
