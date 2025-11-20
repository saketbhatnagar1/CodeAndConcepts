# ==========================
# 1. PYTHON ERRORS
# ==========================

# SyntaxError: Code violates Python syntax
# Example:
# print("Hello"   <- Missing closing parenthesis
# Output: SyntaxError: unexpected EOF while parsing

# NameError: Using an undefined variable
# Example:
# print(x)
# Output: NameError: name 'x' is not defined

# TypeError: Invalid operation on incompatible types
# Example:
# "2" + 3
# Output: TypeError: can only concatenate str (not "int") to str

# IndexError: Accessing invalid index in a list
# Example:
# lst = [1,2,3]
# print(lst[5])
# Output: IndexError: list index out of range

# KeyError: Accessing a non-existent key in dictionary
# Example:
# d = {"a": 1}
# print(d["b"])
# Output: KeyError: 'b'

# ValueError: Wrong type of value for a function
# Example:
# int("abc")
# Output: ValueError: invalid literal for int() with base 10: 'abc'

# AttributeError: Using invalid attribute/method
# Example:
# x = 10
# x.append(5)
# Output: AttributeError: 'int' object has no attribute 'append'


# ==========================
# 2. EXCEPTIONS HANDLING
# ==========================

try:
    # Code that might raise an exception
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    # Handles invalid input conversion
    print("Please enter a valid number!")
except ZeroDivisionError:
    # Handles division by zero
    print("Cannot divide by zero!")
except Exception as e:
    # Catch-all for other exceptions
    print(f"Something went wrong: {e}")
else:
    # Runs if no exception occurs
    print("Success! No errors.")
finally:
    # Always executes
    print("Execution finished.")

# Raising your own exception
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    return True

# ==========================
# 3. JSON DATA HANDLING
# ==========================

import json

# 1. Python dict -> JSON string (serialization)
data = {"name": "Alice", "age": 25, "city": "New York"}
json_string = json.dumps(data)  # Converts to JSON string
print(json_string)
# Output: '{"name": "Alice", "age": 25, "city": "New York"}'

# 2. JSON string -> Python dict (deserialization)
json_input = '{"name": "Bob", "age": 30, "city": "London"}'
py_dict = json.loads(json_input)
print(py_dict)
# Output: {'name': 'Bob', 'age': 30, 'city': 'London'}

# 3. Pretty print JSON
pretty_json = json.dumps(data, indent=4)
print(pretty_json)

# 4. Working with JSON files
# Write to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read from file
with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print(loaded_data)

# 5. Accessing JSON data
print(loaded_data["name"])  # Output: Alice

# ==========================
# QUICK TIPS
# ==========================

# Catch multiple exceptions:
# except (ValueError, TypeError):

# Always validate JSON data:
# try:
#     obj = json.loads(user_input)
# except json.JSONDecodeError:
#     print("Invalid JSON format")

# Use finally for cleanup actions (like closing files)