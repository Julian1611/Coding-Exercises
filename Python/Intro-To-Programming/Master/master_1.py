# This first task to get familiar with Matlib, NumPy and Pandas - these 3 packages represent the most widely used Python libraries in data science

# STEP 1: Download and Install Anaconda (https://www.anaconda.com/download/) - preinstalled packages with python 3 - with this step we will switch to executing code on your PC (Note: select an easy to remember folder - eg: c:\anaconda3)

# STEP 2: Once you install Anaconda you should be able to run jupyter notebook which is a powerful online application containing an ordered list of input/output cells which can contain code, text, mathematics, plots and rich media.

# Launch jupyter notebook by opening a terminal in your PC: example in Windows --> Click on Run and neter cmd.exe - terminal window shoudl appear - type in: C:\Python>jupyter notebook

# STEP 3: once in jupyter notebook, click on NEW
# Enter:

import pandas as pd
import numpy
import matplotlib
print(matplotlib.__version__)
print(pd.__version__)
print (numpy.__version__)

# TASK: Send the output so make sure that all is installed correctly
#
#
# Output should be:
# 3.4.3
# 1.3.4
# 1.21.3
