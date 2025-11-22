



"""
Python Functions Cheat Sheet
Author: Saket Bhatnagar
Date: 2025-11-18

This cheat sheet covers everything about Python functions including:
- Definition & syntax
- Parameters & arguments
- Return values
- Lambda (anonymous) functions
- Default, keyword, and variable-length arguments
- Scope (local, global, nonlocal)
- Nested functions
- Docstrings and best practices
"""

# --------------------------------------------------------------------------------
# 1. Function Definition
# --------------------------------------------------------------------------------
# Syntax:
# def function_name(parameters):
#     """docstring (optional)"""
#     statement(s)
#     return value (optional)

# Example:
def greet(name):
    """Greets a person with their name"""
    print(f"Hello, {name}!")

greet("Saket")  # Output: Hello, Saket!

# --------------------------------------------------------------------------------
# 2. Function Arguments
# --------------------------------------------------------------------------------

# 2.1 Positional arguments
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5

# 2.2 Keyword arguments
def describe_person(name, age):
    print(f"{name} is {age} years old")

describe_person(age=25, name="Alice")  # Order doesn't matter

# 2.3 Default arguments
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # Output: 25 (5^2)
print(power(5, 3))   # Output: 125 (5^3)

# 2.4 Variable-length arguments
# *args → tuple of positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # Output: 10

# **kwargs → dictionary of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name="Bob", age=30)

# --------------------------------------------------------------------------------
# 3. Return Statement
# --------------------------------------------------------------------------------
def square(x):
    return x * x

result = square(4)
print(result)  # Output: 16

# Functions can return multiple values
def coordinates():
    x = 10
    y = 20
    return x, y

x_val, y_val = coordinates()
print(x_val, y_val)  # Output: 10 20

# --------------------------------------------------------------------------------
# 4. Lambda Functions (Anonymous)
# --------------------------------------------------------------------------------
# Syntax: lambda arguments: expression
square_lambda = lambda x: x * x
print(square_lambda(5))  # Output: 25

# Lambda with map, filter, reduce
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# --------------------------------------------------------------------------------
# 5. Function Scope
# --------------------------------------------------------------------------------
# Local scope: variables defined inside a function
# Global scope: variables defined outside functions
# nonlocal: modifies variable in enclosing (non-global) scope

global_var = "I am global"

def outer():
    outer_var = "I am outer"

    def inner():
        nonlocal outer_var
        outer_var = "Modified outer variable"
        print("Inner:", outer_var)
    
    inner()
    print("Outer:", outer_var)

outer()
print("Global:", global_var)  # Output: I am global

# --------------------------------------------------------------------------------
# 6. Nested Functions (Inner Functions / Closures)
# --------------------------------------------------------------------------------
def make_multiplier(n):
    """Returns a function that multiplies by n"""
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
print(times3(10))  # Output: 30

# --------------------------------------------------------------------------------
# 7. Docstrings & Help
# --------------------------------------------------------------------------------
def example_func():
    """This is an example function demonstrating docstrings."""
    pass

print(example_func.__doc__)  # Output: This is an example function demonstrating docstrings.

# --------------------------------------------------------------------------------
# 8. Best Practices & Tips
# --------------------------------------------------------------------------------
# - Use meaningful function names
# - Keep functions small and focused
# - Use docstrings for documentation
# - Avoid excessive use of global variables
# - Use default and keyword arguments for flexibility
# - Lambda functions for simple one-line operations

# --------------------------------------------------------------------------------
# 9. Summary Table (Quick Reference)
# --------------------------------------------------------------------------------
"""
Function Types:
1. Normal Function         -> def func(): ...
2. Lambda / Anonymous      -> lambda args: expression
3. Nested / Inner Function -> function inside function
Arguments Types:
- Positional
- Keyword
- Default
- *args (variable-length positional)
- **kwargs (variable-length keyword)
Scope:
- Local -> inside function
- Global -> outside function
- Nonlocal -> enclosing function
Return:
- return value or tuple of values
- return None (default)
"""

# End of Cheat Sheet
def format_name(fname,lname):
    """Function To Format First and Lastname""" #""" """ comments in """ """ allow us to write the documentation and description of the function
    if fname == "" or lname == "":
        return "Please Provide FirstName and Lastname"
    else:
        formatted_fname = fname.title()
        formatted_lname = lname.title()
    return f"{formatted_fname} {formatted_lname}"
 
name = format_name("SAKET","BHATNAGAR")
print(name) 

#To modify a golbal variable use the global keyword:

enimies = 0
def increase_enimies():
    global enimies #declare the global variable
    enimies+=1 #Perform the operation



# | Scope Type        | Description                                          | Example                                       |
# | ----------------- | ---------------------------------------------------- | --------------------------------------------- |
# | **L (Local)**     | Inside a function (temporary variables)              | Variables defined inside a function           |
# | **E (Enclosing)** | In nested functions (outer but not global)           | Variable in outer function of nested function |
# | **G (Global)**    | Defined at the top level of a script or module       | Variables defined outside functions           |
# | **B (Built-in)**  | Reserved names in Python (like `len`, `print`, etc.) | `len`, `sum`, `range`                         |

