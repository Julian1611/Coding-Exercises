# import all necessary modules
import pdfplumber
import sys
import os

<<<<<<< HEAD
# open pdf to work with in current folder
# file name could change, may need to be done by input by user
statement = pdfplumber.open(os.path.join(sys.path[0], "Statement of Securities Account.pdf"))

# get text for all pages in entire statement
pages = statement.pages
for i, pg in enumerate(pages):
=======
statement = pdfplumber.open(os.path.join(sys.path[0], "Statement of Securities Account.pdf"))

pages = statement.pages
for i,pg in enumerate(pages):
>>>>>>> 500b8d177aa1a7acdf73cf9d826b9c200cf7dba4
    page = statement.pages[i]
    text = page.extract_text()
    print(text)
