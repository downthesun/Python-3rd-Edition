def main():
    number = input("Enter the telephone number in the format XXX-XXX-XXXX: ")
    number = number.upper()
    converted = """"""
    letter = 0

    while letter < len(number):
        if (number[letter] == 'A' or number[letter] == 'B'
        or number[letter] == 'C'):
            converted += '2'
        elif (number[letter] == 'D' or number[letter] == 'E'
        or number[letter] == 'F'):
            converted += '3'
        elif (number[letter] == 'G' or number[letter] == 'H'
        or number[letter] == 'I'):
            converted += '4'
        elif (number[letter] == 'J' or number[letter] == 'K'
        or number[letter] == 'L'):
            converted += '5'
        elif (number[letter] == 'M' or number[letter] == 'N'
        or number[letter] == 'O'):
            converted += '6'
        elif (number[letter] == 'P' or number[letter] == 'Q'
        or number[letter] == 'R' or number[letter] == 'S'):
            converted += '7'
        elif (number[letter] == 'T' or number[letter] == 'U'
        or number[letter] == 'V'):
            converted += '8'
        elif (number[letter] == 'W' or number[letter] == 'X'
        or number[letter] == 'Y'or number[letter] == 'Z'):
            converted += '9'
        else:
            converted += number[letter]
        letter += 1

    print("The phone number is:", converted)

main()
