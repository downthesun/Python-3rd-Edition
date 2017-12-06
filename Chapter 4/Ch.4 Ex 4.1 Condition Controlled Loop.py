keepGoing = 'y'

while keepGoing == 'y':
    sales = float(input('Enter the amount of sales: '))
    commRate = float(input('Enter the commission rate: '))

    commission = (sales * commRate)

    print('The commission is $',
          format(commission, ',.2f'), sep='')

    keepGoing = input('Do you want to calculate another ' +
                      'commission (Enter y or Y for yes): ')
