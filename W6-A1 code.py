
class Student: #class to identify the students
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name        

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}"
    
    student = {'1': 'Joao', '2': 'Maria', '3': 'Pedro', '4': 'Ana', '5': 'Luis'}

class Grade_MSE800: #class to identify the grades of the students in MSE800
    def __init__(self, student_id, subject, grade):
        self.student_id = student_id
        self.subject = subject
        self.grade = grade

    def __str__(self):
        return f"Student ID: {self.student_id}, Subject: {self.subject}, Grade: {self.grade}"
    
    grades = {'1':35, '2':90, '3':48, '4':92, '5':88}

def main():
    #creating a new dictionary with approved students
    approved_students = {k: v for k, v in Student.student.items() if Grade_MSE800.grades.get(k, 0) >= 50    }
    print("Approved Students:")
    for student_id, name in approved_students.items():
        print(f"ID: {student_id}, Name: {name}")

if __name__ == "__main__":
    main()