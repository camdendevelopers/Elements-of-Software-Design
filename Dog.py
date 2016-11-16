class LivingThing:
    can_walk = "Yes"

    def printName(self):
        print("My name is ",self.name)

class Plant(LivingThing):
    can_walk = "No"

    def __str__(self):
        return("I am a plant")

class Animal(LivingThing):

    can_fly = "no"
    legs = 4

    def __str__(self):
        return ("I am an animal")

class Dog(Animal):
    def __init__(self):
        self.name = "Fido"

    def printName(self):
        print("My name is " + self.name + " and I am a dog.")

class Cat(Animal):

    name = "Meredith"

    def __init__(self):
        pass

    def changeAllNames(self, newName):
        Cat.name = newName

    def printName(self):
        print("Meow! I'm a cat and my name is ",self.name)

class Bird(Animal):

    can_fly = "yes"

    def __init__(self):
        self.name = ""
        self.legs = 2
        self.wings = 2

    def __str__(self):
        return("I am a bird")

class Fish(Animal):
    can_walk = "No"

class Penguin(Bird):
    can_fly = "No"

    def __str__(self):
        return("I am a penguin")

def main():

    dog1 = Dog()
    dog2 = Dog()
#    print (dog1.name)
#    print (dog2.name)

    dog2.name = "Spot"
#    print (dog1.name)
#    print (dog2.name)

    cat1 = Cat()
    cat2 = Cat()
#    print (cat1.name)
#    print (cat2.name)

    cat2.name = "Sylvester"
#    print (cat1.name)
#    print (cat2.name)

    cat3 = Cat()
#    print (cat1.name)
#    print (cat2.name)
#    print (cat3.name)

    cat1.changeAllNames("Puddy Tat")
#    print (cat1.name)
#    print (cat2.name)
#    print (cat3.name)

    bird1 = Bird()
    bird1.name = "Tweety"
#    print (bird1.name)
#    print (bird1.legs)
#    print (bird1.can_fly)

#    print (dog1.legs)
#    print (dog1.can_fly)

    bird2 = Bird()
    bird2.name = "Robin"
#    print (bird2.can_fly)
    bird2.can_fly = "No"
#    print (bird2.can_fly)
#    print (bird1.can_fly)
#    del(bird2.can_fly)
#    print (bird2.can_fly)

    penguin1 = Penguin()
    penguin1.name = "Opus"
    print(penguin1.can_fly)
    print(bird1.can_fly)
    print(bird2.can_fly)
    print(dog1.can_fly)
    print(penguin1.can_walk)
    print(penguin1)
    print(bird2)
    print(cat1)
    print(dog1)

    plant1 = Plant()
    plant1.name = "Audrey"
    print(plant1)
    
main()