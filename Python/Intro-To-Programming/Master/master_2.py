# In this task you will analyze basic data with pandas

#Import the necessary libraries
import pandas as pd

# Assign it to a variable called users and use the 'user_id' as index
users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|', index_col='user_id')

# Your tasks are below

# Task1
# See the first 25 entries
print(users.head(25))
# Task2
# See the last 10 entries
print(users.tail(10))
# Task3
# What is the number of observations in the dataset?
print("\nAmount of rows:",len(users))
# Task4
# What is the number of columns in the dataset?
print("Amount of columns:",len(users.columns))
# Task5
# What is the data type of each column?
print("\nData type:\n", users.dtypes)
# Task 6
# How many different occupations there are in this dataset?
print("\n\nThere are",users["occupation"].value_counts().count(), "different occupations.")
# Task 7
# Summarize the DataFrame.
print("\n\nSummarize DataFrame:\n",users.describe())
# Task 8
# Summarize all the columns
print("\n\nSummarize all columns:\n",users.describe(include="all"))
