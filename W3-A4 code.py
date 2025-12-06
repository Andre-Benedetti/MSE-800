import sqlite3

def setup_college_database():
    
    # 1. Connect to the database file (creates it if it doesn't exist)
    conn = sqlite3.connect('college_database.db')
    cursor = conn.cursor()

        # --- 1. Create Teacher Table ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Teacher (
        T_ID INTEGER PRIMARY KEY,
        T_FNAME VARCHAR(255),
        T_LNAME VARCHAR(255),
        T_RANK VARCHAR(100)
    );
    """)
    

    # --- 2. Create Course Table ---
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Course (
        COU_ID INTEGER PRIMARY KEY,
        COU_NAME VARCHAR(255),
        COU_CREDIT VARCHAR(50),
        COU_DEPARTMEN VARCHAR(100),
        
        T_ID INTEGER,
        FOREIGN KEY (T_ID) REFERENCES Teacher(T_ID)
    );
    """)
    
    
    # --- 3. Create Student Table ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Student (
        STU_ID INTEGER PRIMARY KEY,
        STU_FNAME VARCHAR(255),
        STU_LNAME VARCHAR(255),
        STU_BIRTHD VARCHAR(50) -- Stored as text for simplicity
    );
    """)
    

    # --- 4. Create Linking Table: Assign (Enrollment) ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Assign (
        -- Composite Primary Key made of two Foreign Keys
        COU_ID INTEGER,
        STU_ID INTEGER,
        
        PRIMARY KEY (COU_ID, STU_ID),
        FOREIGN KEY (COU_ID) REFERENCES Course(COU_ID),
        FOREIGN KEY (STU_ID) REFERENCES Student(STU_ID)
    );
    """)
    

    # --- 5. Commit changes and close the connection ---
    conn.commit()
    conn.close()


# Execute the setup function
if __name__ == "__main__":
    setup_college_database()