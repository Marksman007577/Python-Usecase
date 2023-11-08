class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale and Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()


    def swim(self):
        print("Moving in Water")

    def breathe(self):
        super().breathe()
        print("Doing this Underwater")


class Dog:
    def __init__(self):
        self.temperament = "loyal"


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"


fish = Fish()
print(fish.num_eyes)
fish.breathe()
fish.swim()

doggo = Dog()
sparky = Labrador()

print(f"A dog is {doggo.temperament}")
print(f"Sparky is {sparky.temperament}")
