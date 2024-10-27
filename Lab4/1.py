class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

animal = Animal()
animal.make_sound()

dog = Dog()
dog.make_sound()
