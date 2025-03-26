from models.expense import Expense
from database.db import connect_db

def is_valid_category(category_id):
    """Check if the category ID exists in the categories table."""
    conn = connect_db()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT id FROM categories WHERE id = %s", (category_id,))
        valid = cur.fetchone() is not None  # Returns True if the category exists
        cur.close()
        conn.close()
        return valid
    return False  # If DB connection fails

def add_expense(amount, category_id, description):
    """Adds an expense after validating the category ID."""
    if not is_valid_category(category_id):
        print(f"Error: Category ID {category_id} does not exist. Please enter a valid category ID.")
        return

    Expense.add_expense(amount, category_id, description)

def view_expenses():
    expenses = Expense.get_all_expenses()

    if expenses:
        print("\n--- Expense List ---")
        for expense in expenses:
            print(f"ID: {expense[0]}, Amount: {expense[1]}, Category ID: {expense[2]}, Description: {expense[3]}, Date: {expense[4]}")
    else:
        print("No expenses found or database connection error.")