import sqlite3

class StudentDB: #create a class to handle database operations
    def __init__(self, db_name="university.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):# Create the students table if it doesn't already exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT,
                score INTEGER
            )
        ''')
        self.conn.commit()

    def populate_data(self):# Initial data
        
        names = {'1': 'Joao', '2': 'Maria', '3': 'Pedro', '4': 'Ana', '5': 'Luis'}
        scores = {'1': 35, '2': 90, '3': 48, '4': 92, '5': 88}
        students_data = [(student_id, name, scores.get(student_id, 0)) for student_id, name in names.items()]
        #scores.get(student_id, 0) ensures a default score of 0 if not found
        
        # Insert or update records
        self.cursor.executemany('''
            INSERT OR REPLACE INTO students (student_id, name, score)
            VALUES (?, ?, ?)
        ''', students_data)
        self.conn.commit()

    def get_top_students(self): # SQL query to retrieve the top N students ordered by score in descending order
        query = "SELECT student_id, name, score FROM students ORDER BY score DESC LIMIT 3 "
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):# Close the database connection safely
        self.conn.close()

def main():
    
    db = StudentDB()
    db.populate_data()

    top_students = db.get_top_students()

    print("Top 3 Students")
    for student in top_students:
        sid, name, score = student
        print(f"ID: {sid} | Name: {name:<6} | Score: {score}")

    # Ensure the connection is closed after execution
    db.close()

if __name__ == "__main__":
    main()