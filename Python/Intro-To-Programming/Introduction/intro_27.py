# wite a function that will return the highest number out of 3.
# Input:
# 3 7 2
# Output:
# 7
#def
#
#
#print(myfunction(3, 7,2))

def highestnumber(a, b, c):
  highest = a
  myList = [a, b, c]
  for i in myList:
    if i > highest:
      highest = i
  return highest

x = ""
y = ""
z = ""
while not type(x) is int or not type(y) is int or not type(z) is int:
  try:
    x = int(input("First number: "))
    y = int(input("Second number: "))
    z = int(input("Third number: "))
  except:
    print("Error - Must input integer number!")
print("Highest number:",highestnumber(x, y, z))
