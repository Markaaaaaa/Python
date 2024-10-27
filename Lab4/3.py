class Bird:
    def fly(self):
        print("Bird")

class Parrot(Bird):
    def fly(self):
        print("Parrot")

bird = Bird()
bird.fly()

parrot = Parrot()
parrot.fly()
