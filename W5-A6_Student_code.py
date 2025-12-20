from W5_A6_Person_code import Person

class Student (Person):#subclass Student of parent class Person
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)
        self.student_id = student_id

    def greet(self):
       print ("Hi" + self.name)


if __name__ == "__main__":

student1 = Student ("Alice","123 Main St", 20, "S12345")
student1.greet()

