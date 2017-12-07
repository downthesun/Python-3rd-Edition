class RetailItem:
    def __init__(self, desc, units, price):
        self.__desc = desc
        self.__units = units
        self.__price = price
        
    def set_desc(self, desc):
        self.__desc = desc

    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price

    def get_desc(self):
        return self.__desc

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price


def main():
    first_desc = "Jacket"
    first_units = "12"
    first_price = 59.95
    
    second_desc = "Designer Jeans"
    second_units = "40"
    second_price = 34.94

    third_desc = "Shirt"
    third_units = "40"
    third_price = 24.95

    item1 = RetailItem(first_desc, first_units, first_price)
    item2 = RetailItem(second_desc, second_units, second_price)
    item3 = RetailItem(third_desc, third_units, third_price)

    print("Retail Item 1: ")
    print("Description: ", item1.get_desc())
    print("Units in inventory: ", item1.get_units())
    print("Price: $", item1.get_price())
    print()
    print("Retail Item 2: ")
    print("Description: ", item2.get_desc())
    print("Units in inventory: ", item2.get_units())
    print("Price: $", item2.get_price())
    print()
    print("Retail Item 3: ")
    print("Description: ", item3.get_desc())
    print("Units in inventory: ", item3.get_units())
    print("Price: $", item3.get_price())

main()
