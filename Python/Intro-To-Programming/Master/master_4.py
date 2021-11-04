# Use jupyter notebook again
# we will use data set from kaggle on us-baby-names
# dataset is here:
# https://raw.githubusercontent.com/mslyon/testone/master/US_Baby_Names_right.csv
#Import the necessary libraries
import pandas as pd

#import the dataset from the above address / best is to download it locally
url = 'https://raw.githubusercontent.com/mslyon/testone/master/US_Baby_Names_right.csv'

# TASK 1: Assign it to a variable called baby_names
baby_names = pd.read_csv(url)
# TASK 2: Check the info with .info()
print("Task 2: ")
baby_names.info()
# TASK 3: Check head with head()
print("Task 3:\n",baby_names.head())
# TASK 4: Delete the column 'Unnamed: 0' and 'Id'
# one method to delete content
baby_names.drop(
    labels=["Unnamed: 0", "Id"],
    axis=1,
    inplace=True
    )
print("Task 4:\n",baby_names)
#  delete the Year column, so sum() works properly for all names
# another method to delete content
del baby_names["Year"]
# TASK 5: Group the dataset by name and assign to names
# use .groupby("Name").sum()
unique_names = baby_names.groupby("Name").sum()
print("Task 5:\n",unique_names)
# TASK 6: sort from the biggest value to the smallest one / use .sort_values
unique_names = unique_names.sort_values(by="Count", ascending=False)
print("Task 6:\n",unique_names)
# TASK 7: as we have already grouped by the name, all the names are unique already.
# get the length of names - use len
print("Amount of unique names:",len(unique_names))
# TASK 8: What is the name with most occurrences?
print("The name with the most occurences:",unique_names.index[0])
