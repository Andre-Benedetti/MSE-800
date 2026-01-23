
class Student: #class to identify the students
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name        

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}"
    
    student = {'1': 'Joao', '2': 'Maria', '3': 'Pedro', '4': 'Ana', '5': 'Luis'}

class Grade: #class to identify the grades of the students in MSE800
    def __init__(self, student_id, subject, grade):
        self.student_id = student_id
        self.subject = subject
        self.grade = grade

    def __str__(self):
        return f"Student ID: {self.student_id}, Subject: {self.subject}, Grade: {self.grade}"
    
    grades = [
        {'student_id': '1', 'subject': 'MSE800', 'grade': 35},
        {'student_id': '2', 'subject': 'MSE800', 'grade': 90},
        {'student_id': '3', 'subject': 'MSE800', 'grade': 48},
        {'student_id': '4', 'subject': 'MSE800', 'grade': 92},
        {'student_id': '5', 'subject': 'MSE800', 'grade': 88},
    ]

def main():
    #creating a new dictionary with approved students
    approved_students = {k: v for k, v in zip (Student.student.keys(), Student.student.values()) if next((g['grade'] for g in Grade.grades if g['student_id'] == k), 0) >= 50}
    print("Approved Students:")
    for student_id, name in approved_students.items():
        print(f"ID: {student_id}, Name: {name}")

if __name__ == "__main__":
    main()