#In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method.
# Create 3 lists: numbers, strings and names
# Add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings list
# Add names John, Eric and Jessica to names list

#Create a new variable third_name with the third name taken from names list, using the brackets operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.

# At the end print all lists and one variable created.

# create the lists
numbers = []
strings = []
names = []
# add numbers, wors and names
numbers += [1, 2, 3]
strings += ["hello", "world"]
names += ["John", "Eric", "Jessica"]
# variable third_name
third_name = names[2]
# print everything
print(numbers)
print(strings)
print(names)
print(third_name)
