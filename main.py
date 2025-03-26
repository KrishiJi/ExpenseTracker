from database.db import initialize_db
from services.tacker import add_expense, view_expenses

def main():
    initialize_db()  # Initialize DB only once

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter amount: ").strip())
                category_id = int(input("Enter category ID (as a number): ").strip())  # Ensure integer input
                description = input("Enter description: ").strip()

                add_expense(amount, category_id, description)
            except ValueError:
                print("Invalid input! Please enter a valid amount and category ID.")

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

