"""
You should now improve the previous translator by asking user 2 options:
1) Enter a new word into the dictionary (when user enters new word then you should also ask for the swedish translation and add both words to the list)
or
2) Translate user's input
 example: user says 'Merry' OUTPUT: god
"""

"""
This program asks the user if he wants to translate from english to swedish or add to the english-to-swedish dictionary

Next, it asks for the according input and either translates or adds to the dictionary

Lastly, it returns the new dictionary or the translation and prints it out

The user can choose to repeat the program or end it at the end
"""

# dictionary english to swedish
dictionary = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

# function to translate english to swedish
def translate(lst):
  # create list for swedish words
  swedish = []
  # translate english to swedish
  for i in lst:
    # try to find words in dictionary by making strings to lowercase and finding the according values
    try:
      swedish.append(dictionary[i.lower()])
    # print english words that aren't in dictionary
    except:
      print("The word", i, "is not in your dictionary.")
  # return list as string
  return " ".join(swedish)

# function to add words to dictionary
def add_to_dictionary(english, swedish):
  #add key and value to dictionary (make sure everything's lowercase, to keep integrity of dictionary)
  dictionary[english.lower()] = swedish.lower()
  # return the dictionary
  return dictionary

# main function
def main():
  # loop until discontinued by User (until loop=False)
  loop = True
  while loop:
    # ask user if addition to dictionary or translation
    option = ""
    while not option == "a" and not option == "b":
      option = input("Do you want to add something to the dictionary (a) or translate something (b)?\n")
      if not option == "a" and not option == "b":
        print("Error - Must input a or b!")
    # if addition to dictionary, ask for english word and according swedish translation
    if option == "a":
      english = input("What is the english word you want to add to your dictionary?\nEnglish: ")
      swedish = input("What is the according swedish translation?\nSwedish: ")
      # print what dictionary is returned by add_to_dictionary()
      print("New dictionary:",add_to_dictionary(english, swedish))
    # if translation, ask for english sentence
    elif option == "b":
      sentence = input("The sentence you want to translate (without special characters like ',', '.', '-', etc., else the translation won't work):\nEnglish: ")
      # split string sentence into list wordsList
      wordsList = sentence.split(" ")
      # print the by translation() returned variable
      print("Swedish:", translate(wordsList))
    # check if user wants to end program or continue
    cont = input("Do you want to continue? Press enter to continue or anything else+enter to stop:\n")
    if cont=="":
      loop = True
    else:
      loop = False

# execute main
main()
