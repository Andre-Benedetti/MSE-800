import sqlite3
import sys
from datetime import datetime

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('exchange_app.db')
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        email TEXT PRIMARY KEY, 
                        password TEXT, 
                        role TEXT, 
                        approved INTEGER)''')
    
    # History table
    cursor.execute('''CREATE TABLE IF NOT EXISTS exchange_history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        rate REAL, 
                        updated_by TEXT, 
                        timestamp DATETIME)''')
    
    # Pre-populate the 3 specific users
    seed_users = [
        ('andre@gmail.com', '12345', 'admin', 1),
        ('cintia@gmail.com', '12345', 'customer', 1),
        ('ricardo@gmail.com', '12345', 'customer', 0)
    ]
    cursor.executemany("INSERT OR IGNORE INTO users VALUES (?, ?, ?, ?)", seed_users)
    
    # Set initial rate (1 USD = 1.65 NZD)
    cursor.execute("SELECT rate FROM exchange_history ORDER BY id DESC LIMIT 1")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO exchange_history (rate, updated_by, timestamp) VALUES (1.65, 'system', ?)", 
                       (datetime.now(),))
    
    conn.commit()
    return conn

db_conn = init_db()

# --- CLASS HIERARCHY ---

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def logout(self):
        print(f"\n {self.email} logged out successfully.")
        return False

class Admin(User):
    def dashboard(self):
        while True:
            cursor = db_conn.cursor()
            cursor.execute("SELECT rate FROM exchange_history ORDER BY id DESC LIMIT 1")
            rate = cursor.fetchone()[0]
            
            print(f"\n--- ADMIN PANEL | Current Rate: 1.00 USD = {rate} NZD ---")
            print("1. View/Approve Users\n2. Delete User\n3. Update Exchange Rate\n4. Logout")
            choice = input("Admin Select: ")

            if choice == "1":
                cursor.execute("SELECT email FROM users WHERE approved = 0")
                pending = cursor.fetchall()
                if not pending: print("No pending approvals.")
                for row in pending:
                    if input(f"Approve {row[0]}? (y/n): ").lower() == 'y':
                        cursor.execute("UPDATE users SET approved = 1 WHERE email = ?", (row[0],))
                db_conn.commit()
            elif choice == "2":
                target = input("Enter email to delete: ")
                cursor.execute("DELETE FROM users WHERE email = ? AND role != 'admin'", (target,))
                db_conn.commit()
                print(f"User {target} removed if they existed.")
            elif choice == "3":
                try:
                    new_rate = float(input("Enter new USD to NZD rate: "))
                    current_time = datetime.now().isoformat()
                    cursor.execute("INSERT INTO exchange_history (rate, updated_by, timestamp) VALUES (?, ?, ?)", 
                                   (new_rate, self.email, current_time))
                    db_conn.commit()
                except ValueError: print("Invalid numeric value.")
            elif choice == "4":
                return self.logout()

class Customer(User):
    def dashboard(self):
        while True:
            cursor = db_conn.cursor()
            cursor.execute("SELECT rate FROM exchange_history ORDER BY id DESC LIMIT 1")
            rate = cursor.fetchone()[0]

            print(f"\n--- CUSTOMER DASHBOARD: {self.email} ---")
            print(f"Rate: 1 USD = {rate} NZD")
            print("1. Convert USD to NZD\n2. Convert NZD to USD\n3. Logout")
            choice = input("Customer Select: ")

            if choice in ["1", "2"]:
                try:
                    amount = float(input("Enter amount to exchange: "))
                    if choice == "1":
                        print(f" {amount} USD = {amount * rate:.2f} NZD")
                    else:
                        print(f" {amount} NZD = {amount / rate:.2f} USD")
                except ValueError: print("Please enter a valid number.")
            elif choice == "3":
                return self.logout()

# --- MAIN APP LOGIC ---

def login():
    email = input("Email: ")
    pw = input("Password: ")
    
    cursor = db_conn.cursor()
    cursor.execute("SELECT password, role, approved FROM users WHERE email = ?", (email,))
    user_data = cursor.fetchone()

    if user_data and user_data[0] == pw:
        if not user_data[2]: # Approved column
            print("\nAccess Denied: Your account is waiting for Admin's approval.")
            return
        
        # Polymorphism: Create object based on database role
        user_obj = Admin(email, pw) if user_data[1] == 'admin' else Customer(email, pw)
        user_obj.dashboard()
    else:
        print("\nInvalid email or password.")

def main():
    while True:
        print("\n=== NZ DOLLAR EXCHANGE APP ===")
        print("1. Login\n2. Create New Account\n3. Exit")
        choice = input("> ")
        if choice == "1": login()
        elif choice == "2":
            email = input("Email: ")
            pw = input("Password: ")
            try:
                db_conn.execute("INSERT INTO users VALUES (?, ?, 'customer', 0)", (email, pw))
                db_conn.commit()
                print("Account created! Ricardo is in the same boat as you—waiting for approval.")
            except sqlite3.IntegrityError: print("Email already registered.")
        elif choice == "3": break

if __name__ == "__main__":
    main()