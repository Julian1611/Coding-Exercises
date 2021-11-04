# in this task we want to understand the volume traded on the stock market in specific years by the predefined stocks.
# We will use QUANDL to get the data - see here full tutorial https://medium.com/python-data/quandl-getting-end-of-day-stock-data-with-python-8652671d6661

import pandas as pd

# package to extract data from various Internet sources into a DataFrame
# make sure you have it installed
from pandas_datareader import data, wb

# package for dates
import datetime as dt

# TASK 1: Create your time range (start and end variables). The start date should be 01/01/2015 and the end should today (whatever your today is) - use dt.datetime

# we pick the Apple, Tesla, Twitter, IBM, LinkedIn stocks symbols and assign them to a variable called stocks
stocks = ['AAPL', 'TSLA', 'IBM', 'LNKD']

# Read the data from google, assign to df and print it
df = web.DataReader(stocks, 'google', start, end)
# we now create a dataFrame called vol, with the Volume values.
vol = df['Volume']
vol.head()

# we now want to Aggregate the data of Volume to weekly
vol['week'] = vol.index.week
vol['year'] = vol.index.year

week = vol.groupby(['week','year']).sum()
week.head()

# TASK 2: Find all the volume traded in the year of 2015
# tip: you will have to delete week column but also to use groupby
