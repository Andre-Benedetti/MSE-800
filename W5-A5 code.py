"""" Can we see the different objects respond differently to the same method call? if yes/ no 
explain it in short? and what the usage of this concept? 

Yes, Polymorphism was used on the methods walk() and swim() in the subclasses Dog and Shark 
respectively, changing the behavior of these methods in each subclass. Heritage was used to inherit 
methods from parent classes in other subclasses like Cat and Salmon, using the same method without 
modification."""


class Animal:#superclass Animal
    def __init__(self, name):
        self.name = name

class Mammal(Animal):#subclass Mammal of parent superclass Animal
    def __init__(self, name):
        super().__init__(name)
        self.feature = "mammal"
    
    def walk(self):
        return f"{self.name} the {self.feature} is walking."

class Dog(Mammal):#subclass Dog of parent class Mammal
    def walk (self): #override walk method
        return f"{self.name} is a {self.feature} and is running."
               
class Cat(Mammal):#subclass Cat of parent class Mammal
    pass #inherits walk method from Mammal
       
class Bird(Animal):#subclass Bird of parent superclass Animal
    def __init__(self, name):
        super().__init__(name)
        self.feature = "bird"
    
    def fly(self):
        return f"{self.name} the {self.feature} is flying."
    
    def swim(self):
        return f"{self.name} the {self.feature} is swimming."
       
class Eagle(Bird):#subclass Eagle of parent class Bird
    def __init__(self, name):
        super().__init__(name)
        super().fly() #use fly method from Bird
       
       
class Penguin(Bird):#subclass Penguin of parent class Bird
    def __init__(self, name):
        super().__init__(name)       
        super().swim() #use swim method from Bird

class Fish(Animal):#subclass Fish of parent superclass Animal
    def __init__(self, name):
        super().__init__(name)
        self.feature = "fish"

    def swim(self):
        return f"{self.name} the {self.feature} is swimming."

class Salmon(Fish):#subclass Salmon of parent class Fish
   pass #inherits swim method from Fish

class Shark(Fish):#subclass Shark of parent class Fish
    def swim(self): #override swim method
        return f"{self.name} is a {self.feature} and is hunting silently in the deep sea."
    
if __name__ == "__main__":#main function to test the classes
    dog1 = Dog("Buddy")
    print(dog1.walk())
    
    cat1 = Cat("Whiskers")
    print(cat1.walk())
    
    eagle1 = Eagle("Freedom")
    print(eagle1.fly())

    penguin1 = Penguin("Waddles")
    print(penguin1.swim())

    salmon1 = Salmon("Nemo")
    print(salmon1.swim())

    shark1 = Shark("Jaws")
    print(shark1.swim())
