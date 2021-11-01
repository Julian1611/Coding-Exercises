# In this task you will visualize your data
# you should work with jupyter notebook! start it before doing the task.

#Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

%matplotlib inline

# we will use data from Titanic Kaggle data set: https://raw.githubusercontent.com/mslyon/mariorepo/master/train.csv

url = 'https://raw.githubusercontent.com/mslyon/mariorepo/master/train.csv'


titanic = pd.read_csv(url)

titanic.head()

# Lets set Set PassengerId as the index
titanic.set_index('PassengerId').head()

# now we want to create  a pie chart presenting the male/female proportion

# sum the instances of males and females
males = (titanic['Sex'] == 'male').sum()
females = (titanic['Sex'] == 'female').sum()

# put them into a list called proportions
proportions = [males, females]

# Create a pie chart
plt.pie(
    # using proportions
    proportions,

    # with the labels being officer names
    labels = ['Males', 'Females'],

    # with no shadows
    shadow = False,

    # with colors
    colors = ['blue','red'],

    # with one slide exploded out
    explode = (0.15 , 0),

    # with the start angle at 90%
    startangle = 90,

    # with the percent listed as a fraction
    autopct = '%1.1f%%'
    )

# View the plot drop above
plt.axis('equal')

# Set labels
plt.title("Sex Proportion")

# View the plot
plt.tight_layout()
plt.show()


# now we want to create a scatterplot with the Fare payed and the Age, differ the plot color by gender
# the code is
# creates the plot using
lm = sns.lmplot(x = 'Age', y = 'Fare', data = titanic, hue = 'Sex', fit_reg=False)

# set title
lm.set(title = 'Fare x Age')

# get the axes object and tweak it
axes = lm.axes
axes[0,0].set_ylim(-5,)
axes[0,0].set_xlim(-5,85)


# TASK 1: How many people survived?

# TASK 2: can you modify the previsous pie chart to display only the survived
