#Given two non-zero integers, print "YES" if exactly one of them is positive and print "NO" otherwise.
#Example input #1
#-5
#10
#Example output #1
#YES
#Example input #2
#5
#10
#Example output #2
#NO

# Read an integer:
# a = int(input())
# Print a value:
# print(a)

a = ""
b = ""
while not type(a) is int or not type(b) is int:
  try:
    a = int(input("Type first number: "))
    b = int(input("Type second number: "))
  except:
    print("Error - you need to type integer number")
# if a smaller 0 or b smaller 0 and also a not smaller 0 or b not smaller 0, only one is negative
# apply de morgans law for code readability
if (a < 0 or b < 0) and not(a < 0 and b < 0):
  print("YES")
else:
  print("NO")
