# Celsius to Fahrenheit and Fahrenheit to Celsius Code:

# code starts here

# declare ask variable
ask = ""
# ask for input until "f" or "c"
while (not ask == "f") and (not ask == "c"):
    ask = input("Fahrenheit to Celsius (f) or Celsius to Fahrenheit (c)? Type f or c: ")
# if "f" get Fahrenheit float
if ask == "f":
  fahrenheit = ""
  # get fahrenheit until type is float
  while not type(fahrenheit) is float:
    try:
      fahrenheit = float(input("Fahrenheit: "))
    except:
      print("Error - you have to input float")
  # calculate celsius
  celsius = (fahrenheit - 32) * 5/9
  # print celsius
  print("Celsius: " + str(celsius))
# else if "c" get celsius float
elif ask == "c":
  celsius = ""
  # get celsius until type is float
  while not type(celsius) is float:
    try:
      celsius = float(input("Celsius: "))
    except:
      print("Error - you have to input float")
  # calculate fahrenheit
  fahrenheit = (celsius * 9/5) + 32
  # print fahrenheit
  print ("Fahrenheit: " + str(fahrenheit))
  # end of code
