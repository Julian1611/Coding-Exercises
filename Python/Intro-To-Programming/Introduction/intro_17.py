# Write a Python program to print yesterday, today, tomorrow.

import datetime

# get current date
today = datetime.date.today()
#get dates for yesterday and tomorrow
yesterday = today + datetime.timedelta(days=-1)
tomorrow = today + datetime.timedelta(days=1)
# print dates
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)
