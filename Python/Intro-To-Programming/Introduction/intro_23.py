# write a program that prints the sum of ten numbers that user has to Enter
# try to control for user's input and check if user entered number or string
# input: 1,2,3,4,5,6,7,8
# output: 36

# initialise sum variable
sum = 0
# for loop in range 10
for i in range(10):
  # sum as string every iteration
  num = ""
  # while loop until num is float
  while not type(num) is int:
    try:
      num = int(input(f"Type number {i+1}: "))
    except:
      print("Error - must input integer number!")
  sum += num
print("Your total sum is", sum)
