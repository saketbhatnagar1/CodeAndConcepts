import sqlite3
from main import Employee

conn = sqlite3.connect('employee.db')
c = conn.cursor()

# Ensure table exists
c.execute("""
CREATE TABLE IF NOT EXISTS employee (
    first TEXT,
    last TEXT,
    pay INTEGER
)
""")

# Employee objects
emp_1 = Employee('John','Doe',80000)
emp_2 = Employee('Johnny','Niss',100000)

def insert(emp):
    """Insert Employee object into database safely using named placeholders"""
    c.execute(
        "INSERT INTO employee (first, last, pay) VALUES (:first, :last, :pay)",
        {'first': emp.first, 'last': emp.last, 'pay': emp.pay}
    )

# Insert employees
insert(emp_1)
insert(emp_2)

# Select all rows to verify
c.execute("SELECT * FROM employee")
print(c.fetchall())  # [('John', 'Doe', 80000), ('Johnny', 'Niss', 100000)]
c.execute("""SELECT * FROM employee where last = (?)""",('Bhatnagar',))
print(c.fetchall())
conn.commit()
conn.close()
