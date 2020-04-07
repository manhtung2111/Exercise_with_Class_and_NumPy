class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.')


class Mammal(Animal):
    # Mammal la lop con thua ke tu lop Animal, cung co cac thuoc tinh cua no
    def __init__(self, mammal_Name):
        print(mammal_Name, 'is a warm-blooded animal.')
        super().__init__(mammal_Name) # khong can goi ham


class Non_Winged_Mammal(Mammal):
    def __init__(self, Non_Wing_Mammal):
        print(Non_Wing_Mammal, "can't fly.")
        super().__init__(Non_Wing_Mammal)


class Non_Marined_Mammal(Mammal):
    def __init__(self, Non_Marine_Mammal):
        print(Non_Marine_Mammal, "can't swim.")
        super().__init__(Non_Marine_Mammal)


class Dog(Non_Marined_Mammal, Non_Winged_Mammal):
    def __init__(self):
        print('Dog has 4 legs.');
        super().__init__('Dog') #super(Dog,self).__init__('Dog')


d = Dog()
print('')
bat = Non_Marined_Mammal('Bat')