def is_Prime( integer ):
    even_Divisions = 0
    if integer <= 1:
        return False
    for number in range( 1, integer + 1 ):
        if integer % number == 0:
            even_Divisions = (even_Divisions + 1)
            if even_Divisions > 2:
                return False
    return True

def main():
    integer = int( input( "Please enter a number: " ))
    print()
    if is_Prime( integer ):
        print( integer, "is a prime number" )
    else:
        print( integer, "is a Not prime number" )

main()
            
