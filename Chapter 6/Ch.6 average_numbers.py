def main():
    total = 0.0
    number_Of_Lines = 0.0

    try:
        file_Name = input( "Enter a file name: " )
        in_File = open( file_Name, "r" )
        for line in in_File:
            number_Of_Lines = number_Of_Lines + 1
            total = (total + float( line ) )
        average = ( total / number_Of_Lines )
        print( "Average: ", format( average, ".2f" ) )

        in_File.close()
    
    except IOError:
        print( "An error occured trying to read the file" )
    
    except ValueError:
        print( "Non-numeric data found in the file" )

main()
