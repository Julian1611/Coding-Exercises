# Write a function you can call it sumthree that will sum three numbers
# IMPORTANT: sum function has to be defined as a function with def sumthree():
# you have to read all three numbers using for loop and add them to the list.
# in the sumthree function you will to the sum of the list elements


def sumthree():
  sum = 0
  nums = []
  # get integers to add to list
  for i in range(3):
    num = ""
    while not type(num) is int:
      try:
        num = int(input(f"Input number {i+1}: "))
      except:
        print("Error - input integer number!")
    nums.append(num)
  # add list elements to sum
  for n in nums:
    sum += n
  # return sum
  return sum

print("Sum:",sumthree())
