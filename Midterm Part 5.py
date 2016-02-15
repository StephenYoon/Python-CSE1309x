# Calculates the total amount of money required to purchase those items
# a = quantity of the items
# b = price of the corresponding items
# Assumption: both arrays have equal lengths
def items_price(a, b):
    grand_total = 0
    for k in range(len(a)):
        grand_total = grand_total + (a[k] * b[k])

    return grand_total

print(items_price([2, 3, 5, 7, 9], [5, 8, 4, 1, 11]))
