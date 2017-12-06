import random

def generate_Random_Number():
    random_Number = random.randint( 1 , 500 )
    return random_Number

def main():
    random_Number_File = input( "Enter the name of the file to which" + \
                                " results should be written: ")
    random_Number_Amount = int( input( "Enter the number of random numbers" + \
                                       " to be written to the file: " ) )
    writable_File = open( random_Number_File, "w" )
    
    for random_Number_Total in range( 1, random_Number_Amount + 1):
        random_Number = generate_Random_Number()
        writable_File.write( str( random_Number ) + "\n" )

main()
