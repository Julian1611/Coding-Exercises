#Write a Python program to reverse a string word by word.
# Input string : 'hello .py'
# Expected Output : '.py hello'

# class py_solution with reverse_words() inside
class py_solution:
  # function to reverse string word order
  def reverse_words(self, s):
    # split string into list of words
    wordList = s.split(" ")
    # reverse order of wordList
    wordList.reverse()
    # return list as string
    return " ".join(wordList)

# test
print(py_solution().reverse_words('hello .py'))
