#Given a positive real number, print its first digit to the right of the decimal point.
#Example input
# 1.79

#Example output
# 7

# Read a float:
# a = float(input())
# Print a value:
# print(a)

a = 0.0
while not a > 0:
  a = float(input())
print(str(a).split(".")[1][0])
