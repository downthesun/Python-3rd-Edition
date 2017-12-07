class Pet:
    def __init__(self, name, species, age):
        self.__name = name
        self.__type = species
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, species):
        self.__type = species

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__type

    def get_age(self):
        return self.__age

def get_Pet_Info():
    name = input("Enter the name of the pet: ")
    animal_type = input("Enter the type of animal: "
    age = input("Enter the age of the pet: ")

    pet1 = Pet(name, animal_type, age)

    print("Here is the data that you entered:")
    print("Pet name: ", pet1.get_name())
    print("Animal type: ", pet1.get_animal_type())
    print("Age of pet: ", pet1.get_age())

get_Pet_Info()
