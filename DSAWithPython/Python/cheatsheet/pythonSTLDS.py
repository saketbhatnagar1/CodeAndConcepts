"""
Python Data Structures Cheat Sheet
Author: Saket Bhatnagar
Date: 2025-11-18

This cheat sheet covers Python's main data structures:
- Lists
- Tuples
- Dictionaries
- Sets
- Strings (as immutable sequences)
- Other useful operations
- Best practices and tips
"""

# --------------------------------------------------------------------------------
# 1. LISTS
# --------------------------------------------------------------------------------
# Ordered, mutable collection
# Syntax: my_list = [item1, item2, item3]

my_list = [1, 2, 3, 4, 5]
print(my_list[0])      # Access first element -> 1
print(my_list[-1])     # Access last element -> 5

# Adding elements
my_list.append(6)      # Add at end
my_list.insert(2, 99)  # Insert at index 2
print(my_list)

# Removing elements
my_list.remove(99)      # Remove by value
last = my_list.pop()    # Remove last and return it
del my_list[0]          # Delete by index

# Slicing
print(my_list[1:4])     # [2, 3, 4]
print(my_list[:3])      # [2, 3, 4] (from start)
print(my_list[::2])     # [2, 4] (step)

# List comprehension
squared = [x**2 for x in range(5)]
print(squared)          # [0, 1, 4, 9, 16]

# Iterating
for item in my_list:
    print(item)

# --------------------------------------------------------------------------------
# 2. TUPLES
# --------------------------------------------------------------------------------
# Ordered, immutable collection
# Syntax: my_tuple = (item1, item2, item3)

my_tuple = (1, 2, 3)
print(my_tuple[1])      # Access -> 2

# Tuple unpacking
a, b, c = my_tuple
print(a, b, c)          # 1 2 3

# Single element tuple
single = (5,)           # Comma is mandatory
print(type(single))     # <class 'tuple'>

# --------------------------------------------------------------------------------
# 3. DICTIONARIES
# --------------------------------------------------------------------------------
# Unordered (Python 3.7+ maintains insertion order), mutable key-value pairs
# Syntax: my_dict = {"key1": value1, "key2": value2}

my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # Access by key -> Alice

# Adding / updating
my_dict["city"] = "Bologna"
my_dict["age"] = 26

# Removing
my_dict.pop("city")
del my_dict["age"]

# Iterating
for key, value in my_dict.items():
    print(key, value)

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares)           # {0:0, 1:1, 2:4, 3:9, 4:16}

# --------------------------------------------------------------------------------
# 4. SETS
# --------------------------------------------------------------------------------
# Unordered, mutable, no duplicates
# Syntax: my_set = {1, 2, 3}

my_set = {1, 2, 3, 3}
print(my_set)            # {1, 2, 3} -> duplicates removed

# Adding / removing
my_set.add(4)
my_set.remove(2)
my_set.discard(5)        # No error if element not present
my_set.pop()             # Removes arbitrary element

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union -> {1,2,3,4,5}
print(a & b)  # Intersection -> {3}
print(a - b)  # Difference -> {1,2}
print(a ^ b)  # Symmetric difference -> {1,2,4,5}

# --------------------------------------------------------------------------------
# 5. STRINGS (Immutable sequences)
# --------------------------------------------------------------------------------
# Access like lists
s = "Python"
print(s[0])      # P
print(s[-1])     # n
print(s[0:4])    # Pyth

# Useful methods
print(s.upper())         # PYTHON
print(s.lower())         # python
print(s.replace("P", "J")) # Jython
print(s.split("y"))      # ['P', 'thon']
print(" ".join(["Hello","World"]))  # 'Hello World'

# String formatting
name = "Alice"
age = 25
print(f"{name} is {age} years old")   # f-string
print("{} is {}".format(name, age))   # format method

# --------------------------------------------------------------------------------
# 6. OTHER DATA STRUCTURES
# --------------------------------------------------------------------------------
# 6.1 Arrays (via array module)
import array
arr = array.array('i', [1,2,3])   # 'i' -> integer type
arr.append(4)
print(arr)

# 6.2 Deque (efficient insertion/removal from both ends)
from collections import deque
dq = deque([1,2,3])
dq.appendleft(0)
dq.pop()
print(dq)      # deque([0,1,2])

# 6.3 Namedtuple (immutable tuple with named fields)
from collections import namedtuple
Point = namedtuple("Point", ["x","y"])
p = Point(1,2)
print(p.x, p.y)  # 1 2

# 6.4 Counter (count frequency of elements)
from collections import Counter
cnt = Counter([1,2,2,3,3,3])
print(cnt)        # Counter({3:3,2:2,1:1})

# --------------------------------------------------------------------------------
# 7. BEST PRACTICES & TIPS
# --------------------------------------------------------------------------------
# - Use list for ordered mutable collection
# - Use tuple for immutable sequences
# - Use dict for key-value mapping
# - Use set for uniqueness and set operations
# - Prefer comprehensions for concise, readable code
# - Use collections module for specialized structures

# --------------------------------------------------------------------------------
# 8. QUICK REFERENCE
# --------------------------------------------------------------------------------
"""
List       -> [a, b, c]        Mutable, ordered
Tuple      -> (a, b, c)        Immutable, ordered
Dict       -> {k:v}            Mutable, unordered (keys unique)
Set        -> {a, b, c}        Mutable, unordered, unique
String     -> "abc"             Immutable, ordered
Deque      -> deque([...])      Efficient pops/appends from both ends
NamedTuple -> namedtuple(...)   Immutable tuple with field names
Counter    -> Counter([...])    Count frequency of elements
"""

# End of Data Structures Cheat Sheet
