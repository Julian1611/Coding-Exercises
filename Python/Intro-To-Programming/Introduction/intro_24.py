# write a function that does the sum of 3 integers passed to a function (you can call it sumofthree(). Numbers are passed as arguments.
# example: sumofthree(5,3,10)
# output: 18

# function to return sum of a,b,c
def sumofthree(a, b, c):
  return a+b+c

# declare x,y,z as variables
x = ""
y = ""
z = ""
# ask for x,y,z to get three numbers
while not type(x) is int or not type(y) is int or not type(z) is int:
  try:
    x = int(input("Type first number: "))
    y = int(input("Type second number: "))
    z = int(input("Type third number: "))
  except:
    print("Error - Must input integer number!")
# print sum by using function sumofthree
print("The sum of your three numbers is:", sumofthree(x, y, z))
