# Modify the below code so you input 2 numbers, do the sum through the function and print the result


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

x = ""
y = ""
while not type(x) is int or not type(y) is int:
  try:
    x = int(input("Input first number: "))
    y = int(input("Input second number: "))
  except:
    print("Error - Please input integer number!")
print("Your sum:", sum_two_numbers(x,y))
