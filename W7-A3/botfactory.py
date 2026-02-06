from abc import ABC, abstractmethod

class Unit(ABC):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def action(self):
        pass

class Helper(Unit):
    def action(self):
        print(f"{self.id} is assisting humans")

class Friend(Unit):
    def action(self):
        print(f"{self.id} is keeping company")

class Maker:
    @staticmethod
    def produce(unit_type, id):
        if unit_type == "helper":
            return Helper(id)
        elif unit_type == "friend":
            return Friend(id)
        else:
            raise ValueError("Unknown type")
        

#The design pattern used here is the Factory Pattern, as the objected creation responsability is on the Maker class. One advantage is that the Maker class doesn't need to knnow 
#the details of the objects it creates, and can easily be extended to create new types of units without modifying existing code.
#A disadvantage is that it can also make it to understand the code if there are too many classes.  
