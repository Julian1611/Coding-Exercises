# import all necessary modules
import pdfplumber
import sys
import os

# open pdf to work with in current folder
# file name could change, may need to be done by input by user
statement = pdfplumber.open(os.path.join(sys.path[0], "Statement of Securities Account.pdf"))

# get text for all pages in entire statement
pages = statement.pages
for i, pg in enumerate(pages):
    page = statement.pages[i]
    text = page.extract_text()
    print(text)
