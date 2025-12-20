class Person:#superclass
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def greet(self):
        return f"Hello, my name is {self.name} and my ID is {self.id}"

class Student(Person):#subclass Student
    def __init__(self, id, name, student_id):#subclass Student of superclass Person
        super().__init__(id, name)
        self.student_id = student_id

    def greet(self):
        base_greet = super().greet()
        return f"{base_greet}. My student ID is {self.student_id}."
    
class Staff(Person):#subclass Staff
    def __init__(self, id, name, staff_id, tax_number):#subclass Staff of superclass Person
        super().__init__(id, name)
        self.staff_id = staff_id
        self.tax_number = tax_number

    def greet(self):
        base_greet = super().greet()
        return f"{base_greet}. My staff ID is {self.staff_id} and my tax number is {self.tax_number}."

class General(Staff):#subclass General of parent class Staff
    def __init__(self, id, name, staff_id, tax_number, rate_of_pay):
        super().__init__(id, name, staff_id, tax_number)
        self.rate_of_pay = rate_of_pay

    def greet(self):
        base_greet = super().greet()
        return f"{base_greet}. My general ID is {self.id} and my rate of pay is {self.rate_of_pay}."

class Academic(Staff):#subclass Academic of parent class Staff
    def __init__(self, id, name, staff_id, tax_number, publications):
        self.publications = publications

    def greet(self):
        base_greet = super().greet()
        pub_list = ", ".join(self.publications) if self.publications else "No publications"
        return f"{base_greet}. My academic ID is {self.id} and my publications are {pub_list}."

if __name__ == "__main__":#main function to test the classes
    
    student1 = Student("P001", "Alice", "S123")#subclass Student must include all attributes of superclass Person
    print(student1.greet())
    
    teacher1 = Academic("P002", "Bob", "T456", "TX789", ["Paper1", "Paper2"])#subclass Academic must include all attributes of parent class Staff and superclass Person
    print(teacher1.greet())

    general1 = General("P003", "Charlie", "G101", "TX111",5000)#subclass General must include all attributes of parent class Staff and superclass Person
    print(general1.greet())
