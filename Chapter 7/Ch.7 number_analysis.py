def get_Values():
    values = []

    first_Num = int(input("Enter number 1 of 5: "))
    second_Num = int(input("Enter number 2 of 5: "))
    third_Num = int(input("Enter number 3 of 5: "))
    fourth_Num = int(input("Enter number 4 of 5: "))
    fifth_Num = int(input("Enter number 5 of 5: "))

    values.append(first_Num)
    values.append(second_Num)
    values.append(third_Num)
    values.append(fourth_Num)
    values.append(fifth_Num)

    return values

def get_Analysis (numbers):

    print(("Low:"),  str(min(numbers)))
    print(("High:"), str(max(numbers)))
    print(("Total:"), str(sum(numbers)))
    print(("Average:"), format(sum(numbers)/len(numbers), '.2f'))
  

def main():
    numbers = get_Values()
    get_Analysis(numbers)

main()

