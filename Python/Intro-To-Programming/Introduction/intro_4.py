# Days of week are numbered as: 0 — Sunday, 1 — Monday, 2 — Tuesday, ..., 6 — Saturday. An integer K in the range 1 to 365 is given. Find the number of day of week for K-th day of year provided that in this year January 1 was Thursday.
# Example input
#1

#Example output
#4

# Read an integer:
# a = int(input())
# Print a value:
# print(a)

K = 0
while not K in range(1,366):
  K = int(input())
K += 4
if not K%7 == 0:
  print((K%7)-1)
else:
  print(6)
