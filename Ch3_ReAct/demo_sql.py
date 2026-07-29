import os
import sqlite3

# 1. Target the correct absolute database path
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "SALES_DB", "sales.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 2. Define the extra records to add
new_customers = [
    ('Charlie',),
    ('David',),
    ('Eva',)
]

new_orders = [
    (1, 'Tablet'),     # Alice bought a Tablet
    (3, 'Headphones'), # Charlie bought Headphones
    (4, 'Monitor'),    # David bought a Monitor
    (5, 'Keyboard')    # Eva bought a Keyboard
]

try:
    # 3. Bulk insert the new records
    print("Inserting new records...")
    cursor.executemany("INSERT INTO customers (name) VALUES (?)", new_customers)
    cursor.executemany("INSERT INTO orders (customer_id, item) VALUES (?, ?)", new_orders)
    
    # 4. Commit changes to save them to the disk
    conn.commit()
    print("Records added successfully!")

except Exception as e:
    conn.rollback()
    print(f"Insertion failed. Rolling back changes. Error: {e}")

# 5. Verify and print all active data inside the tables
print("\n--- Current Customers Table ---")
cursor.execute('SELECT * FROM customers')
for row in cursor.fetchall():
    print(row)

print("\n--- Current Orders Table ---")
cursor.execute('SELECT * FROM orders')
for row in cursor.fetchall():
    print(row)

conn.close()
