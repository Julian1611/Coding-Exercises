# This gets the random number generator.
# There are 3 mistakes in this code - FIX them

import random
i = random.randrange(10,51)
print ('Your number is', i)

if i < 20:
    print ("That is less than 20.")
    if i % 3 == 0:
      print ("It is divisible by 3.")
elif i == 20:
    print ("That is exactly twenty.  How nice for you.")
else:
    if i % 2 == 1:
        print ("That is an odd number.")
    else:
        print ("That is twice", i / 2, '.')
    print ("Wow! That's more than 20!")
