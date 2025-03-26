# Expense Tracker

A simple command-line-based Expense Tracker that allows users to add and view expenses, storing data in a PostgreSQL database.

## Features

- **Add Expense**: Users can add an expense by providing an amount, category, and description.
- **View Expenses**: Displays all recorded expenses with details like amount, category, description, and date.
- **Database Validation**: Ensures that only valid category IDs are accepted.
- **Basic Error Handling**: Prevents invalid inputs and handles database connection issues.

## Prerequisites

- Python 3.x
- PostgreSQL (version 12 or higher recommended)
- psycopg2 (Python library for PostgreSQL)
- Git (for cloning the repository)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
Install Python Dependencies:

bash
Copy
pip install -r requirements.txt
(Create a requirements.txt file containing:)

Copy
psycopg2>=2.9.3
Database Setup:

Install PostgreSQL on your system

Create a new database and user:

sql
Copy
CREATE DATABASE expense_tracker;
CREATE USER expense_user WITH PASSWORD 'securepassword';
GRANT ALL PRIVILEGES ON DATABASE expense_tracker TO expense_user;
Initialize Database Schema:
Run the SQL script located at database/schema.sql:

bash
Copy
psql -U expense_user -d expense_tracker -f database/schema.sql
Example schema.sql content:

sql
Copy
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    category_id INTEGER REFERENCES categories(id),
    description TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert default categories
INSERT INTO categories (name) VALUES 
('Food'), ('Transportation'), ('Entertainment'), 
('Utilities'), ('Rent'), ('Other');
Configure Database Connection:
Edit database/db.py:

python
Copy
import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="expense_tracker",
        user="expense_user",
        password="securepassword"
    )
Usage
Run the application:

bash
Copy
python main.py
Main Menu Options:
Add Expense

Enter the amount (must be positive number)

Select from available categories

Add optional description

View Expenses

Shows all expenses in chronological order

Displays:

Date

Category

Amount

Description

Exit

Gracefully exits the application

Project Structure
Copy
expense-tracker/
├── main.py            # Main application logic
├── database/
│   ├── db.py          # Database connection
│   └── schema.sql     # Database schema
├── models/
│   └── expense.py     # Expense model/operations
└── requirements.txt   # Dependencies
Error Handling
The application includes several error handling mechanisms:

Invalid Input Validation:

Non-numeric amounts

Negative amounts

Invalid category selections

Database Errors:

Connection failures

Query execution errors

Transaction rollbacks on failure

General Exceptions:

Graceful exit on unexpected errors

User-friendly error messages

Future Enhancements
User authentication system

Monthly expense summaries

Budget tracking functionality

Category management (add/edit/delete)

Data export (CSV/Excel)

Graphical reports

Multi-user support

Recurring expenses

Mobile/Web interface

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a feature branch (git checkout -b feature/your-feature)

Commit your changes (git commit -m 'Add some feature')

Push to the branch (git push origin feature/your-feature)

Open a Pull Request

License
MIT License

Copyright (c) [year] [your name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Copy

This comprehensive Markdown document includes:
1. Complete installation instructions
2. Detailed database setup
3. Full usage documentation
4. Project structure
5. Comprehensive error handling details
6. Roadmap for future features
7. Contribution guidelines
8. Complete MIT license text

You can copy this directly into your README.md file in the project repository.