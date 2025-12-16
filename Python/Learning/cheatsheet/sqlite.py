"""
================================================================================
SQLITE IN PYTHON – COMPLETE, LINE‑BY‑LINE CHEAT SHEET (SINGLE FILE)
================================================================================
This file is a FULL reference for using SQLite with Python using the built‑in
`sqlite3` module. Every important concept is explained inline with comments.

You can:
- Read it top to bottom to learn SQLite in Python
- Run parts of it directly
- Copy snippets into real projects

SQLite = lightweight, serverless, file‑based relational database
Python sqlite3 module = DB‑API 2.0 compliant
================================================================================
"""

# -----------------------------------------------------------------------------
# 1. IMPORTING SQLITE
# -----------------------------------------------------------------------------
import sqlite3  # Built‑in Python module to interact with SQLite databases

# Optional but useful
from sqlite3 import Error  # For catching database‑specific errors

# -----------------------------------------------------------------------------
# 2. CONNECTING TO A DATABASE
# -----------------------------------------------------------------------------

# Connect to a database file (creates file if it does not exist)
conn = sqlite3.connect("example.db")
# "example.db" is a file stored on disk

# Special case: In‑memory database (exists only while program runs)
# conn = sqlite3.connect(":memory:")

# Enable returning rows as dictionaries instead of tuples (optional)
conn.row_factory = sqlite3.Row

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# -----------------------------------------------------------------------------
# 3. CREATING A TABLE
# -----------------------------------------------------------------------------

# SQL statement to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique row ID
    name TEXT NOT NULL,                    -- Text field (cannot be NULL)
    email TEXT UNIQUE,                     -- Must be unique
    age INTEGER,                           -- Integer column
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# Execute SQL command
cursor.execute(create_table_query)

# Commit changes to database
conn.commit()

# -----------------------------------------------------------------------------
# 4. INSERTING DATA (CRUD – CREATE)
# -----------------------------------------------------------------------------

# NEVER use string formatting for SQL → SQL injection risk ❌
# Use parameterized queries (placeholders ?)

insert_query = """
INSERT INTO users (name, email, age)
VALUES (?, ?, ?);
"""

# Single insert
cursor.execute(insert_query, ("Saket", "saket@example.com", 22))

# Multiple inserts at once
users_data = [
    ("Aman", "aman@example.com", 21),
    ("Riya", "riya@example.com", 23),
]
cursor.executemany(insert_query, users_data)

conn.commit()  # Save inserts

# -----------------------------------------------------------------------------
# 5. READING DATA (CRUD – READ)
# -----------------------------------------------------------------------------

# Select all rows
cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()  # Returns list of rows

for row in rows:
    # Access by index
    print(row[0], row[1])

    # Access by column name (only if row_factory is set)
    print(row["name"], row["email"])

# Select specific columns
cursor.execute("SELECT name, age FROM users;")

# Select with condition
cursor.execute("SELECT * FROM users WHERE age > ?;", (21,))

# Fetch one row
one_user = cursor.fetchone()

# -----------------------------------------------------------------------------
# 6. UPDATING DATA (CRUD – UPDATE)
# -----------------------------------------------------------------------------

update_query = """
UPDATE users
SET age = ?
WHERE name = ?;
"""

cursor.execute(update_query, (25, "Saket"))
conn.commit()

# Check number of affected rows
print(cursor.rowcount)

# -----------------------------------------------------------------------------
# 7. DELETING DATA (CRUD – DELETE)
# -----------------------------------------------------------------------------

delete_query = "DELETE FROM users WHERE name = ?;"
cursor.execute(delete_query, ("Aman",))
conn.commit()

# -----------------------------------------------------------------------------
# 8. TRANSACTIONS
# -----------------------------------------------------------------------------

try:
    conn.execute("BEGIN")  # Start transaction

    cursor.execute(insert_query, ("Temp", "temp@example.com", 99))
    cursor.execute(update_query, (30, "Riya"))

    conn.commit()  # Commit if everything works
except Error as e:
    conn.rollback()  # Undo all changes if error occurs
    print("Transaction failed:", e)

# -----------------------------------------------------------------------------
# 9. AGGREGATE FUNCTIONS
# -----------------------------------------------------------------------------

cursor.execute("SELECT COUNT(*) FROM users;")
print(cursor.fetchone()[0])

cursor.execute("SELECT AVG(age) FROM users;")

cursor.execute("SELECT MAX(age), MIN(age) FROM users;")

# -----------------------------------------------------------------------------
# 10. ORDER BY, LIMIT, OFFSET
# -----------------------------------------------------------------------------

cursor.execute("""
SELECT * FROM users
ORDER BY age DESC
LIMIT 2 OFFSET 0;
""")

# -----------------------------------------------------------------------------
# 11. JOINS (FOREIGN KEYS)
# -----------------------------------------------------------------------------

# Enable foreign key constraints (IMPORTANT)
conn.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
""")

# INNER JOIN example
cursor.execute("""
SELECT users.name, orders.product
FROM users
INNER JOIN orders ON users.id = orders.user_id;
""")

# -----------------------------------------------------------------------------
# 12. INDEXES (PERFORMANCE)
# -----------------------------------------------------------------------------

cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);")
conn.commit()

# -----------------------------------------------------------------------------
# 13. SQL INJECTION SAFE EXAMPLE
# -----------------------------------------------------------------------------

# ❌ BAD (never do this)
# cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")

# ✅ GOOD
user_input = "Saket"
cursor.execute("SELECT * FROM users WHERE name = ?;", (user_input,))

# -----------------------------------------------------------------------------
# 14. CONTEXT MANAGER (BEST PRACTICE)
# -----------------------------------------------------------------------------

# Automatically commits or rolls back
with sqlite3.connect("example.db") as conn2:
    cur = conn2.cursor()
    cur.execute("SELECT * FROM users;")

# -----------------------------------------------------------------------------
# 15. ERROR HANDLING
# -----------------------------------------------------------------------------

try:
    cursor.execute("SELECT * FROM non_existing_table;")
except sqlite3.OperationalError as e:
    print("SQL Error:", e)

# -----------------------------------------------------------------------------
# 16. DATABASE METADATA
# -----------------------------------------------------------------------------

# List tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# Get table schema
cursor.execute("PRAGMA table_info(users);")
print(cursor.fetchall())

# -----------------------------------------------------------------------------
# 17. VACUUM (DATABASE OPTIMIZATION)
# -----------------------------------------------------------------------------

cursor.execute("VACUUM;")  # Rebuilds database file

# -----------------------------------------------------------------------------
# 18. CLOSING CONNECTION
# -----------------------------------------------------------------------------

cursor.close()  # Close cursor
conn.close()    # Close database connection

# -----------------------------------------------------------------------------
# END OF SQLITE CHEAT SHEET
# -----------------------------------------------------------------------------
