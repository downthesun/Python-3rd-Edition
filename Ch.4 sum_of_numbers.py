total = 0.0

userNumber = float( input( "Enter a positive number (negative to quit): "))

while userNumber > -1:
    total = (total + userNumber)
    userNumber = float( input( "Enter a positive number (negative to quit): "))

print( "Total =", format(total, '.2f'))
    

