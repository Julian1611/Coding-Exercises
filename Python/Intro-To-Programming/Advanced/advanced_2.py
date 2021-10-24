"""Represent a small bilingual lexicon as a Python dictionary in the
following fashion {"merry":"god", "christmas":"jul", "and":"och",
"happy":gott", "new":"nytt", "year":"ar"} and use it to translate
your Christmas cards from English into Swedish.

That is, write a function translate() that takes a list of English words and returns
a list of Swedish words.

As output: you should have list of all swedish words
OUTPUT: ['god', 'jul', 'och', 'gott', 'nytt', 'ar']

"""

# dictionary english to swedish
dictionary = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

def translate(lst):
  # create list for swedish words
  swedish = []
  # translate english to swedish
  for i in lst:
    # try to find words in dictionary by making strings to lowercase and trying to find the according keys
    try:
      swedish.append(dictionary[i.lower()])
    # ignore words that aren't in dictionary (in this case: mom)
    except:
      pass
    # return list
  return swedish

# print translated list
print (translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year', 'mom']))
  
