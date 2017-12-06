shares_purchased = int(x=2000)
per_share = float(40.00)
percentage = float(0.03)

total_paid = shares_purchased*per_share
commission_paid = (total_paid*percentage)

shares_sold = int(x=2000)
sold_for = float(42.75)
total_sold = shares_sold*sold_for
commission_sold = (total_sold*percentage) 

total_commission = commission_paid+commission_sold
profit = total_sold-total_paid-total_commission

print('Amount paid for the stock: $', total_paid )
print('Commission paid on the purchase: $', commission_paid )
print('Amount the stock sold for: $', total_sold)
print('Commission paid on the sale: $', commission_sold )
print('Profit (or loss is negative): $', profit )



