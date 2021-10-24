#Fix the below code so it works
#This programm tells you if the given number is a float or not, and whether its above or below a 100

print ('Please input a float number')
try:
  a = float(input("Enter nb: "))
  print('Yes - that is a float number')
  if a > 100:
	  print('Your number is higher than 100')
  elif a == 100:
    print('Your number is equal to 100')
  else:
	  print('Your number is lower than 100')
except ValueError:
	print ('Error - that is not a float')
