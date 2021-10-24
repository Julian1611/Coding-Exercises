# Write a function filter_my_words() that takes a list of words and an integer n and returns the list of words that are longer than n
# you have to print the list of words

# input:  school education management
# input: 8
# output: education management

# function to filter words in list
def filter_my_words(str, n):
  # declare new list (for words larger than n)
  newList = []
  # for loop to get every word in list
  for i in str:
    # check if length of word is larger than n
    if len(i) > n:
      # add word to newList in that case
      newList.append(i)
  # return newList
  return newList

# main function
def main():
  # declare list
  words = []
  # ask for amount of elements in list
  amount = ""
  while not type(amount) is int or not amount > 0:
    try:
      amount = int(input("How long should your list be: "))
    except:
      print("Error - please input positive integer number.")
  # ask for each element, put each in list
  for i in range(amount):
    words.append(input(f"Please input element {i+1}: "))
  print("Your list:", words)
  # ask for integer that words have to be larger than
  integer = ""
  while not type(integer) is int or not integer > 0:
    try:
      integer = int(input("Length at which to check: "))
    except:
      print("Error - please input positive integer number.")
  # execute and print filter_my_words()
  print("Your revised list:",filter_my_words(words,integer))


# execute main()
main()
