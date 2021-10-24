# complete the below program so it displays days between two dates.
from datetime import date
a = date(2017,2,28)
b = date(2018,2,28)
# get days and time between the dates
# get absolute value to be independent of whether a or b is a later date
delta = abs(a - b)
# format to only show days
print(delta.days)
