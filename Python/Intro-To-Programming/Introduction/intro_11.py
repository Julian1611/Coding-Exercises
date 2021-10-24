#Given the two integers, print the least of them.
#Example input
#3
#7
#Example output
#3


# Read an integer:
# a = int(input())
# Print a value:
# print(a)

a = ""
b = ""
# get a and b until both integers
while not type(a) is int or not type(b) is int:
  try:
    a = int(input("First integer: "))
    b = int(input("Second integer: "))
  except:
    print("Type integer for both values!")

# compare a and b, print accordingly
if a<b:
  print(a)
elif b<a:
  print(b)
else:
  print("Both values are equal.")
