vehicleSpeed = float( input( "What is the speed of the vehicle in MPH? "))

hoursTraveled = int( input( "Enter the number of hours traveled: "))

print( "----------------------" )
for currentHour in range( 1, hoursTraveled + 1):
    distanceTraveled = (vehicleSpeed * currentHour)
    print( currentHour,"Hour(s) ",distanceTraveled,"Miles", sep='' )



