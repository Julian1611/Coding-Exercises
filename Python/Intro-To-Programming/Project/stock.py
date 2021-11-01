import pdfplumber
import sys
import os

statement = pdfplumber.open(os.path.join(sys.path[0], "Statement of Securities Account.pdf"))

pages = statement.pages
for i,pg in enumerate(pages):
    page = statement.pages[i]
    text = page.extract_text()
    print(text)
