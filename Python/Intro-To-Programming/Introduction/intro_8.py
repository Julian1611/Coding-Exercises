# Create 3 variables: mystring, myfloat and myint.
# mystring should contain the word "hello.The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
# Finally, print all 3 variables by checking if mystring equals to "hello" then print it out. You then check if myfloat is really a float number and is equal to 10.0 - then you print it out (if both conditions are satisfied)
# And you do the same for int

mystring = "hello"
myfloat = 10.0
myint = 20
if mystring == "hello":
  print(mystring)
if (type(myfloat) is float) and (myfloat == 10.0):
  print(myfloat)
if (type(myint) is int) and (myint == 20):
  print(myint)
