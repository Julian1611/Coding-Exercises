import stock

statement = stock.read_traderepublic("Statement of Securities Account.pdf")
pages = stock.get_pages_traderepublic(statement)
ISIN_list = stock.get_isin_traderepublic(statement, pages)
money_value = stock.get_values_traderepublic(statement, pages)


# proof of concept: connect ISIN with current total value in depot
# iterate through numbers equivalent to length of ISIN_list
for x in range(len(ISIN_list)):
    # print ISIN
    print(ISIN_list[x])
    # iterate through money_value list to find the current total value
    for y in range(4):
        if y == 3:
            # print current total value
            print(money_value[(x+1)*(y+1)-1])
