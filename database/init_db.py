import sqlite3

def init_db():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('expense_splitter.db')
    cursor = conn.cursor()

    # Create a table for storing expenses
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        user TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    # Create a table for storing users
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()