# stock conclusion for trade republic

# import all necessary modules
import pdfplumber
import sys
import os
import re

# declare all lists for program
ISIN_list_page = []
ISIN_list = []
all_strings = []
value = []
money_value = []
    
def read_traderepublic(name):
    # open pdf to work with in current folder
    # file name could change, may need to be done by input by user
    statement = pdfplumber.open(os.path.join(sys.path[0], name))
    return statement

def get_pages_traderepublic(statement):
    # get ISIN numbers for all pages in entire statement
    pages = statement.pages
    return pages

def get_isin_traderepublic(statement, pages):
    # enumerate through all pages of the document
    for i, pg in enumerate(pages):
        page = statement.pages[i]
        text = page.extract_text()
        # extract all strings on current page page
        all_strings = re.split("\s", text)
        # extract ISIN numbers on current page
        ISIN_list_page = re.findall("ISIN: [A-Z][A-Z].........[0-9]", text)
        for n in ISIN_list_page:
            ISIN_list.append(n)
    return ISIN_list

def get_values_traderepublic(statement, pages):
    for i, pg in enumerate(pages):
        page = statement.pages[i]
        text = page.extract_text()
        # extract all strings on current page page
        all_strings = re.split("\s", text)
        # get only numbers on page with , and without % in them, ie. value per stock, buying value, profit/loss, current value
        # establish counter to ignore certain numbers not meant as values
        count_occurances = 0
        counter = 0
        # iterate through each word in the statement
        for n in all_strings:
            # find all words including the format digit,digit digit (e.g. 0,01 or 122,54)
            value = re.findall("[0-9],[0-9][0-9]", n)
            # add one to the counter for each iteration
            counter += 1
            # check if we found a word with the required format, have below 4 occurances thus far and no % in the word
            # the reason for below 4 occurances is that the TR statement is built this way, that we only want to find the first 4 occurances of numbers for one stock
            if value and count_occurances < 4 and not "%" in n:
                # append the found word to our list money_value
                money_value.append(n)
                # set counter back to 0
                counter = 0
                # add 1 to occurances
                count_occurances += 1
            # if the counter is above 9, set occurances back to 0, as we are at the next stock
            if counter > 9:
                count_occurances = 0
    return money_value

# just for testing purposes. MUST BE DEACTIVATED FOR FINAL PROGRAM
'''
statement = read_traderepublic("Statement of Securities Account.pdf")
pages = get_pages_traderepublic(statement)
ISIN_list = get_isin_traderepublic(statement, pages)
money_value = get_values_traderepublic(statement, pages)

# print all ISIN Numbers on the page
print("List of ISIN:", ISIN_list)
print("All ISIN:", len(ISIN_list))
# print all values in document
print("List of money_values:", money_value)
print("All values in document:", len(money_value))
'''