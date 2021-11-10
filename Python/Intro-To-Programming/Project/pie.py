# proof of concept: pie chart for all ISIN
# put money-values in proportion

import stock
import matplotlib.pyplot as plt

statement = stock.read_traderepublic("Statement of Securities Account.pdf")
pages = stock.get_pages_traderepublic(statement)
ISIN_list = stock.get_isin_traderepublic(statement, pages)
money_value = stock.get_values_traderepublic(statement, pages)

proportion = []
# iterate through numbers equivalent to length of ISIN_list
for x in range(len(ISIN_list)):
    # iterate through money_value list to find the current total value
    for y in range(4):
        if y == 3:
            # print current total value
            proportion.append(money_value[(x+1)*(y+1)-1])

# format proportions correctly (into float format)
for i in range(len(proportion)):
    proportion[i] = proportion[i].replace(".", "")
    proportion[i] = proportion[i].replace(",", ".")
    proportion[i] = float(proportion[i])

plt.pie(
    # use proportions
    proportion,

    # ISIN as labels
    labels = ISIN_list,

    # with no shadows
    shadow = False,

    # with the start angle at 90%
    startangle = 90,

    # with the percent listed as a fraction
    autopct = '%1.1f%%',

    radius = 4,
    )

# View the plot drop above
plt.axis('equal')
# Set labels
plt.title("Depot Conclusion")

# View the plot
plt.tight_layout()
plt.show()