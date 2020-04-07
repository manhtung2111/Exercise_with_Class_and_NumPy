class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")


class Cat(Pet):
    def __init__(self, name, age, color, type):
        super().__init__(name, age)
# Thay vi phai khai bao lai toan bo cac thuoc tinh thi ta chi can dung super de ke thua lai cac thuoc tinh da co cua Pet
        self.color = color
        self.type = type

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old, {self.type} and I am {self.color}")

    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Bird(Pet):
    pass


p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 25, "Short Hair cat", "yellow")
c.show()
d = Dog("Tam", 16)
d.speak()
b = Bird("Tu", 12)
b.speak()
