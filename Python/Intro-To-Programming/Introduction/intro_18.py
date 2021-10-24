#Write a Python program to print next 5 days starting from today

#Sample Output:
#2017-05-06 12:27:53.632939
#2017-05-07 12:27:53.632939
#2017-05-08 12:27:53.632939
#2017-05-09 12:27:53.632939
#2017-05-10 12:27:53.632939

import datetime

now = datetime.datetime.now()
today = datetime.date.today()

# get time for all dates
t = now.strftime(" %H:%M:%S.%f")

# get dates for all 5 days
day_1 = str(today) + t
day_2 = str(today + datetime.timedelta(days=1)) + t
day_3 = str(today + datetime.timedelta(days=2)) + t
day_4 = str(today + datetime.timedelta(days=3)) + t
day_5 = str(today + datetime.timedelta(days=4)) + t
# print dates
print(day_1)
print(day_2)
print(day_3)
print(day_4)
print(day_5)
