"""
Write a function is_member() that takes a value
i.e. a number, string, etc) x and a list of values a,
and returns True if x is a member of a, False otherwise.

(Note that this is exactly what the in operator does,
but for the sake of the exercise you should pretend
Python did not have this operator.)
"""

def is_member(ele, lst):
  # pretend in operator doesn't exist, so no for "ele in lst"
  # also no "for i in lst"
  # get length of lst to be able to simulate "fake" for loop with while loop
  listLength = len(lst)
  i = 0
  # "fake" for loop
  while listLength > i:
    # if ele = lst at any point, return True instantly
    if ele == lst[i]:
      return True
    # add one to i to resume or stop while loop
    i += 1
  # return False if ele doesn't equal lst at any point
  return False


#test
print (is_member("e", ['a', 'e', 'i', 'o', 'u']))
print (is_member(19, [1,3,4,6,18,20]))
print (is_member('right', ['wrong', 'list', 'to', 'search']))
print (is_member('panda', ['lion', 'zebra', 'elephant', 'panda']))
