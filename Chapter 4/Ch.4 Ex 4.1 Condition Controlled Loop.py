#This program calculates sales commissions

#Creat variable to control the loop
keepGoing = 'y'

#Calculate a series of commissions
while keepGoing == 'y':
    #Get a salesperson's sales and commission rate
    sales = float(input('Enter the amount of sales: '))
    commRate = float(input('Enter the commission rate: '))

    #Calculate the commission rate
    commission = (sales * commRate)

    #Display the commission
    print('The commission is $',
          format(commission, ',.2f'), sep='')

    #See if the user wants to do another one
    keepGoing = input('Do you want to calculate another ' +
                      'commission (Enter y or Y for yes): ')
