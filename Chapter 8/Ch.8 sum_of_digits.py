def get_Digits():=
    numbers = input('Enter a sequence of digits with nothing '
                        'separating them: ')
    
    total = 0

    for i in numbers:
        total += int(i) 
    print("The total of the digits in the string you entered is",total)
   
get_Digits()
