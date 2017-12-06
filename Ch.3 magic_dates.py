MONTH = int(input('Enter the month in numeric form: ' ))
DAY = int(input('Enter the day of the month: ' ))
YEAR = int(input('Enter the year in two digit format: '))

MAGIC_DATE = (MONTH * DAY)

print('The date is: ', MONTH , '/' , DAY , '/' , YEAR)

if  MAGIC_DATE == YEAR:
    print('This is a magic date.')
else:
    print('This is not a magic date')
    

    
