import psycopg2
from database.db import connect_db

class Expense:
    @staticmethod
    def add_expense(amount, category_id, description):
        conn = connect_db()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO expenses (amount, category_id, description) VALUES (%s, %s, %s)",
                    (amount, category_id, description)
                )
                conn.commit()
                cur.close()
                conn.close()
                print("Expense added successfully!")
            except psycopg2.Error as e:
                print(f"Database error: {e}")
        else:
            print("Failed to connect to the database.")

    @staticmethod
    def get_all_expenses():
        conn = connect_db()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT id, amount, category_id, description, date FROM expenses")
            expenses = cur.fetchall()  # Fetch data
            
            cur.close()
            conn.close()

            return expenses  # RETURN THE DATA
        
        return None  # Explicitly return None if connection fails
