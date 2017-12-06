PACKAGE = 99.00

QUANTITY = int(input('Enter the number of packages purchased: ' ))

TOTAL_PAID = float(QUANTITY * PACKAGE)

DISCOUNT1 = float(TOTAL_PAID * 0)
DISCOUNT2 = float(TOTAL_PAID * 0.10)
DISCOUNT3 = float(TOTAL_PAID * 0.20)
DISCOUNT4 = float(TOTAL_PAID * 0.30)
DISCOUNT5 = float(TOTAL_PAID * 0.40)

GRAND_TOTAL = float(TOTAL_PAID)
GRAND_TOTAL2 = float(TOTAL_PAID - DISCOUNT2)
GRAND_TOTAL3 = float(TOTAL_PAID - DISCOUNT3)
GRAND_TOTAL4 = float(TOTAL_PAID - DISCOUNT4)
GRAND_TOTAL5 = float(TOTAL_PAID - DISCOUNT5)

if QUANTITY >= 100:
    print ('Enter the number of packages purchased: ', QUANTITY)
    print ('Discount amount: $', format(DISCOUNT5, '.2f'))
    print ('Total Amount: $', format(GRAND_TOTAL5, '.2f'))
elif QUANTITY >= 50:
    print ('Enter the number of packages purchased: ', QUANTITY)
    print ('Discount amount: $', format(DISCOUNT4, '.2f'))
    print ('Total Amount: $', format(GRAND_TOTAL4, '.2f'))
elif QUANTITY >= 20:
    print ('Enter the number of packages purchased: ', QUANTITY)
    print ('Discount amount: $', format(DISCOUNT3, '.2f'))
    print ('Total Amount: $', format(GRAND_TOTAL3, '.2f'))
elif QUANTITY >= 10:
    print ('Enter the number of packages purchased: ', QUANTITY)
    print ('Discount amount: $', format(DISCOUNT2, '.2f'))
    print ('Total Amount: $', format(GRAND_TOTAL2, '.2f'))
elif QUANTITY < 10:
    print ('Enter the number of packages purchased: ', QUANTITY)
    print ('Discount amount: $', format(DISCOUNT1, '.2f'))
    print ('Total Amount: $', format(GRAND_TOTAL1, '.2f'))
