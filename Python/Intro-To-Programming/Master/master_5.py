import pandas as pd
import numpy as np

# visualization
import matplotlib.pyplot as plt

%matplotlib inline

# Import the dataset from http://codingxcamp.com/datasets/appl_1980_2014.csv

# TASK 1: Assign it to a variable apple and read the head

# TASK 2: Check out the type of the columns

# We transform the Date column as a datetime type
# it seems APPLE DOES NOT SUPPORT ANYMORE stock fetching - please try to use QUANDL instead (https://medium.com/python-data/quandl-getting-end-of-day-stock-data-with-python-8652671d6661)
apple.Date = pd.to_datetime(apple.Date)

apple['Date'].head()

# TASK 3: Set the date as the index

# As the index is from the most recent date we make the first entry the oldest date.
apple.sort_index(ascending = True).head()

# we get the last business day of each month
apple_month = apple.resample('BM').mean()

apple_month.head()

# Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches
