import os
import sqlite3

# 1. Use the absolute path logic to make sure it always finds the correct database
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "SALES_DB", "sales.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 2. Create the customers table if it does not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# 3. Create the orders table if it does not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        item TEXT NOT NULL,
        FOREIGN KEY(customer_id) REFERENCES customers(id)
    )
''')

# 4. Insert dummy data if the tables are empty
cursor.execute("SELECT COUNT(*) FROM customers")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO customers (name) VALUES ('Alice'), ('Bob')")
    cursor.execute("INSERT INTO orders (customer_id, item) VALUES (1, 'Laptop'), (2, 'Phone')")
    conn.commit()  # Save changes to the database file

# 5. Fetch and print the data safely
print("--- Customers ---")
cursor.execute('SELECT * FROM customers')
print(cursor.fetchall())

print("\n--- Orders ---")
cursor.execute('SELECT * FROM orders')
print(cursor.fetchall())

print("\nDone")
conn.close()
