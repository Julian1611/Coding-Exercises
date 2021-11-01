import pdfplumber

statement = pdfplumber.open('/Statement of Securities Account.pdf')

text = statement.extract_text()

print(text)
