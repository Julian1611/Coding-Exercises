#Given a string "Hello World" . Determine how many words it has.
# Then create a new string "This is my life." and count number of characters 'i' it has and print it out.
#Example input
#Hello world
#Example output
#2
# String a has 3 characters i


a = "Hello World"
# split string a into list of single words
words = a.split()
# count elements in list and print out
print("Amount of words in 'Hello World':",len(words))

b = "This is my life."
# count i's in string b
amount_i = b.count("i")
# print out amount of i's
print("Amount of i's in 'This is my life.':", amount_i)
