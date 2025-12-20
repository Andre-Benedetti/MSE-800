from W5_A6_Person_code import Person

""" Its output ois different from the superclass Person because the greet() method is overridden 
in the subclass Student to provide a different implementation. """

class Student (Person):#subclass Student of parent class Person from file W5_A6_Person_code
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)
        self.student_id = student_id

    def greet(self):
       print ("Hi " + self._name)


if __name__ == "__main__":
    student1 = Student ("Alice","123 Main St", 20, "S12345")
    student1.greet()

