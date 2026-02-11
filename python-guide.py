"""
COMPREHENSIVE PYTHON COMMANDS AND PROPERTIES GUIDE
==================================================
"""

# ============================================================================
# 1. DATA TYPES AND VARIABLES
# ============================================================================

# Basic Data Types
integer = 42
floating = 3.14
string = "Hello, Python!"
boolean = True
none_value = None

# Type Checking
type(integer)  # <class 'int'>
isinstance(integer, int)  # True
str(integer)  # Convert to string
int(3.14)  # Convert to int
float("3.14")  # Convert to float
bool(1)  # Convert to bool


# ============================================================================
# 2. STRING OPERATIONS AND PROPERTIES
# ============================================================================

text = "Python Programming"

# String Methods
text.lower()  # "python programming"
text.upper()  # "PYTHON PROGRAMMING"
text.capitalize()  # "Python programming"
text.title()  # "Python Programming"
text.strip()  # Remove leading/trailing whitespace
text.lstrip()  # Remove leading whitespace
text.rstrip()  # Remove trailing whitespace
text.replace("Python", "Java")  # Replace substring
text.split()  # Split by whitespace: ['Python', 'Programming']
text.split(",")  # Split by comma
text.join(["a", "b"])  # Join list with separator
text.find("Python")  # Find index of substring
text.startswith("Python")  # Check if starts with
text.endswith("ing")  # Check if ends with
text.count("n")  # Count occurrences
text.isdigit()  # Check if all digits
text.isalpha()  # Check if all alphabetic
text.isalnum()  # Check if alphanumeric
text.isspace()  # Check if all whitespace
text.isupper()  # Check if all uppercase
text.islower()  # Check if all lowercase
len(text)  # Length: 18

# String Formatting
name = "Alice"
age = 30
f"My name is {name} and I'm {age}"  # f-string
"My name is {} and I'm {}".format(name, age)  # .format()
"My name is %s and I'm %d" % (name, age)  # % formatting


# ============================================================================
# 3. LIST OPERATIONS AND PROPERTIES
# ============================================================================

my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "two", 3.0, True, None]

# List Methods
my_list.append(6)  # Add element to end
my_list.extend([7, 8])  # Add multiple elements
my_list.insert(0, 0)  # Insert at index
my_list.remove(2)  # Remove first occurrence
my_list.pop()  # Remove and return last element
my_list.pop(0)  # Remove and return at index
my_list.index(3)  # Find index of element
my_list.count(2)  # Count occurrences
my_list.sort()  # Sort in place
my_list.reverse()  # Reverse in place
my_list.copy()  # Create shallow copy
my_list.clear()  # Remove all elements
len(my_list)  # Length

# List Access
my_list[0]  # First element
my_list[-1]  # Last element
my_list[1:3]  # Slice from index 1 to 2
my_list[:3]  # First 3 elements
my_list[2:]  # From index 2 to end
my_list[::2]  # Every 2nd element

# List Comprehension
[x * 2 for x in my_list]  # [2, 4, 6, 8, 10]
[x for x in my_list if x > 2]  # Filter
[x if x > 2 else 0 for x in my_list]  # Conditional

# Unpacking
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4]  # first=1, rest=[2,3,4]


# ============================================================================
# 4. TUPLE OPERATIONS AND PROPERTIES
# ============================================================================

my_tuple = (1, 2, 3, 4, 5)
single_tuple = (1,)  # Note the comma
empty_tuple = ()

# Tuple Methods
my_tuple.count(2)  # Count occurrences
my_tuple.index(3)  # Find index
len(my_tuple)  # Length
my_tuple[0]  # Indexing
my_tuple[1:3]  # Slicing

# Tuples are immutable
# my_tuple[0] = 10  # Error!


# ============================================================================
# 5. DICTIONARY OPERATIONS AND PROPERTIES
# ============================================================================

my_dict = {"name": "Alice", "age": 30, "city": "NYC"}
empty_dict = {}
dict()  # Create empty dict

# Dictionary Methods
my_dict.get("name")  # Get value, returns None if not found
my_dict.get("name", "Unknown")  # Default value
my_dict.keys()  # Get all keys: dict_keys(['name', 'age', 'city'])
my_dict.values()  # Get all values
my_dict.items()  # Get key-value pairs
my_dict.pop("age")  # Remove and return value
my_dict.popitem()  # Remove and return last item
my_dict.update({"age": 31, "job": "Engineer"})  # Update multiple
my_dict.clear()  # Remove all items
my_dict.copy()  # Create shallow copy
my_dict.setdefault("age", 30)  # Get or set default
len(my_dict)  # Number of keys

# Dictionary Access
my_dict["name"]  # Access value
my_dict.get("name")  # Safe access
"name" in my_dict  # Check if key exists
"Alice" in my_dict.values()  # Check if value exists

# Dictionary Comprehension
{x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
{k: v for k, v in my_dict.items() if k != "age"}  # Filter


# ============================================================================
# 6. SET OPERATIONS AND PROPERTIES
# ============================================================================

my_set = {1, 2, 3, 4, 5}
set()  # Create empty set
set([1, 2, 2, 3])  # Create from list: {1, 2, 3}

# Set Methods
my_set.add(6)  # Add element
my_set.remove(1)  # Remove element, raises error if not found
my_set.discard(1)  # Remove element, no error if not found
my_set.pop()  # Remove and return arbitrary element
my_set.clear()  # Remove all elements
len(my_set)  # Number of elements
1 in my_set  # Check membership

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.union(set2)  # {1, 2, 3, 4, 5}
set1 | set2  # Union operator
set1.intersection(set2)  # {3}
set1 & set2  # Intersection operator
set1.difference(set2)  # {1, 2}
set1 - set2  # Difference operator
set1.symmetric_difference(set2)  # {1, 2, 4, 5}
set1 ^ set2  # Symmetric difference operator


# ============================================================================
# 7. CONTROL FLOW STATEMENTS
# ============================================================================

# Conditional Statements
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Ternary Operator
"positive" if x > 0 else "non-positive"

# Loops
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

for item in [1, 2, 3]:
    print(item)

for index, item in enumerate([1, 2, 3]):
    print(index, item)

for key, value in my_dict.items():
    print(key, value)

# While Loop
while x > 0:
    x -= 1

# Loop Control
for i in range(10):
    if i == 2:
        continue  # Skip this iteration
    if i == 5:
        break  # Exit loop
    print(i)

# Try-Except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
else:
    print("No error occurred")
finally:
    print("This always executes")


# ============================================================================
# 8. FUNCTIONS AND PROPERTIES
# ============================================================================

# Basic Function
def greet(name):
    return f"Hello, {name}!"

greet("Alice")

# Default Parameters
def greet(name="Guest"):
    return f"Hello, {name}!"

# Variable Arguments
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

# Keyword Arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)

# Lambda (Anonymous Function)
square = lambda x: x ** 2
square(5)  # 25

# Higher-Order Functions
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))  # [2, 4, 6, 8, 10]
odds = list(filter(lambda x: x % 2 != 0, numbers))  # [1, 3, 5]

# Decorators
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Closures
def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
add_5(3)  # 8


# ============================================================================
# 9. CLASSES AND OBJECT-ORIENTED PROGRAMMING
# ============================================================================

# Class Definition
class Person:
    # Class variable
    species = "Homo sapiens"
    
    # Constructor
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    
    # Instance method
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    # Class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)
    
    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18
    
    # Special methods
    def __str__(self):
        return f"Person: {self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
    
    def __len__(self):
        return self.age
    
    def __eq__(self, other):
        return self.age == other.age

# Creating Objects
person1 = Person("Alice", 30)
person1.greet()  # "Hello, I'm Alice"
Person.from_birth_year("Bob", 1994)
Person.is_adult(25)  # True

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def greet(self):
        return f"Hello, I'm {self.name}, a student"

# Property Decorator
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14 * self._radius ** 2

circle = Circle(5)
circle.area  # 78.5


# ============================================================================
# 10. FILE OPERATIONS
# ============================================================================

# Reading Files
with open("file.txt", "r") as file:
    content = file.read()  # Read entire file
    # content = file.readline()  # Read one line
    # content = file.readlines()  # Read all lines as list

# Writing Files
with open("file.txt", "w") as file:
    file.write("Hello, World!")
    # file.writelines(["line1\n", "line2\n"])

# Appending to Files
with open("file.txt", "a") as file:
    file.write("\nNew line")

# File Position
with open("file.txt", "r") as file:
    file.seek(0)  # Move to beginning
    file.tell()  # Get current position

# Checking File Existence
import os
os.path.exists("file.txt")
os.path.isfile("file.txt")
os.path.isdir("directory")
os.path.getsize("file.txt")


# ============================================================================
# 11. MODULES AND IMPORTS
# ============================================================================

# Import Module
import math
from math import sqrt, pi
from math import sqrt as square_root
import math as m

# Using Functions from Modules
math.sqrt(16)  # 4.0
sqrt(16)  # 4.0
square_root(16)  # 4.0
m.pi  # 3.14159

# Common Modules
import datetime
import random
import json
import csv
import re
import itertools
import collections
import functools
import operator


# ============================================================================
# 12. DATETIME AND TIME
# ============================================================================

import datetime

# Current Date and Time
now = datetime.datetime.now()
today = datetime.date.today()
current_time = datetime.time(12, 30, 45)

# Creating Dates
date1 = datetime.date(2024, 2, 6)
datetime1 = datetime.datetime(2024, 2, 6, 12, 30, 45)

# Date Operations
date1.year  # 2024
date1.month  # 2
date1.day  # 6
date1.weekday()  # 1 (Monday is 0)
date1.strftime("%Y-%m-%d")  # "2024-02-06"

# Timedelta
delta = datetime.timedelta(days=5, hours=3, minutes=30)
new_date = date1 + delta


# ============================================================================
# 13. REGULAR EXPRESSIONS
# ============================================================================

import re

text = "Hello, World! 123"

# Pattern Matching
re.search(r"\d+", text)  # Find first match
re.findall(r"\w+", text)  # Find all matches
re.match(r"Hello", text)  # Match at beginning
re.fullmatch(r".*", text)  # Match entire string

# Pattern Replacement
re.sub(r"\d+", "XXX", text)  # Replace digits

# Splitting
re.split(r"\s+", text)  # Split by whitespace

# Compiling Pattern
pattern = re.compile(r"world", re.IGNORECASE)
pattern.search(text)


# ============================================================================
# 14. LIST COMPREHENSIONS AND GENERATORS
# ============================================================================

# List Comprehension
[x**2 for x in range(10)]
[x for x in range(10) if x % 2 == 0]
[(x, y) for x in range(3) for y in range(3)]

# Generator Expression
gen = (x**2 for x in range(10))
next(gen)  # Get next value
list(gen)  # Convert to list

# Generator Function
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)


# ============================================================================
# 15. BUILT-IN FUNCTIONS
# ============================================================================

# Common Built-in Functions
abs(-5)  # 5
all([True, True, True])  # True
any([False, True, False])  # True
bin(10)  # '0b1010'
bool(1)  # True
chr(65)  # 'A'
ord('A')  # 65
dict()  # {}
dir(object)  # List attributes
divmod(10, 3)  # (3, 1)
enumerate([1, 2, 3])  # Indexed iterator
filter(lambda x: x > 2, [1, 2, 3, 4])  # Filter
float(10)  # 10.0
format(10, 'b')  # Binary format
getattr(object, 'attr')  # Get attribute
globals()  # Global variables
hasattr(object, 'attr')  # Check attribute
hash("string")  # Hash value
hex(255)  # '0xff'
id(object)  # Object identity
input("Prompt: ")  # Get user input
int("10")  # 10
isinstance(10, int)  # True
issubclass(bool, int)  # True
iter([1, 2, 3])  # Create iterator
len([1, 2, 3])  # 3
list("abc")  # ['a', 'b', 'c']
map(lambda x: x*2, [1, 2, 3])  # Apply function
max([1, 2, 3])  # 3
min([1, 2, 3])  # 1
oct(8)  # '0o10'
open("file.txt")  # File object
pow(2, 3)  # 8
print("Hello")  # Print to stdout
range(5)  # Range object
repr("string")  # String representation
reversed([1, 2, 3])  # Reversed iterator
round(3.14159, 2)  # 3.14
set([1, 2, 2, 3])  # {1, 2, 3}
setattr(object, 'attr', value)  # Set attribute
sorted([3, 1, 2])  # [1, 2, 3]
str(10)  # "10"
sum([1, 2, 3])  # 6
tuple([1, 2, 3])  # (1, 2, 3)
type(10)  # <class 'int'>
zip([1, 2], ['a', 'b'])  # [(1, 'a'), (2, 'b')]


# ============================================================================
# 16. OBJECT-ORIENTED PROPERTIES
# ============================================================================

# Property Example
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius"""
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Convert to Fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set from Fahrenheit"""
        self._celsius = (value - 32) * 5/9

temp = Temperature(0)
temp.celsius  # 0
temp.fahrenheit  # 32.0
temp.celsius = 100
temp.fahrenheit  # 212.0


# ============================================================================
# 17. SPECIAL METHODS (DUNDER METHODS)
# ============================================================================

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Length
    def __len__(self):
        return 2
    
    # Comparison
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
    
    # Arithmetic
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # Indexing
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")
    
    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector index out of range")
    
    # Iteration
    def __iter__(self):
        return iter([self.x, self.y])
    
    # Calling
    def __call__(self, factor):
        return Vector(self.x * factor, self.y * factor)
    
    # Container methods
    def __contains__(self, value):
        return value in [self.x, self.y]


# ============================================================================
# 18. CONTEXT MANAGERS
# ============================================================================

# Using Context Managers (with statement)
with open("file.txt", "r") as f:
    content = f.read()
# File automatically closes

# Creating Context Managers
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        return False

with MyContext() as ctx:
    print("Inside context")


# ============================================================================
# 19. ITERATORS AND ITERABLES
# ============================================================================

# Creating Iterator
class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

for num in CountUp(3):
    print(num)  # 1, 2, 3

# Using itertools
import itertools
list(itertools.count(1, 2))  # 1, 3, 5, ... (infinite)
list(itertools.repeat("x", 3))  # ['x', 'x', 'x']
list(itertools.chain([1, 2], [3, 4]))  # [1, 2, 3, 4]
list(itertools.combinations([1, 2, 3], 2))  # All 2-combinations


# ============================================================================
# 20. FUNCTIONAL PROGRAMMING
# ============================================================================

import functools
import operator

# reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
reduce(operator.add, numbers)  # 15
reduce(lambda x, y: x + y, numbers)  # 15

# partial
from functools import partial
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
square(5)  # 25

# wraps
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


# ============================================================================
# 21. USEFUL STDLIB MODULES REFERENCE
# ============================================================================

# Collections
import collections
Counter = collections.Counter
defaultdict = collections.defaultdict
OrderedDict = collections.OrderedDict
namedtuple = collections.namedtuple
deque = collections.deque

# functools
import functools
reduce = functools.reduce
partial = functools.partial
lru_cache = functools.lru_cache
wraps = functools.wraps

# itertools
import itertools
chain = itertools.chain
combinations = itertools.combinations
permutations = itertools.permutations
product = itertools.product
islice = itertools.islice

# operator
import operator
add = operator.add
mul = operator.mul
itemgetter = operator.itemgetter
attrgetter = operator.attrgetter

# json
# import json
# json.dump(data, file)  # Write JSON
# json.dumps(data)  # Convert to JSON string
# json.load(file)  # Read JSON
# json.loads(string)  # Parse JSON string

# CSV
# import csv
# csv.reader(file)  # Read CSV
# csv.writer(file)  # Write CSV
# csv.DictReader(file)  # Read as dictionaries
# csv.DictWriter(file, fieldnames)  # Write dictionaries

# Pathlib
from pathlib import Path
p = Path("file.txt")
p.exists()
p.is_file()
p.read_text()
p.write_text("content")


# ============================================================================
# 22. DEBUGGING AND TESTING
# ============================================================================

# Assertions
assert x > 0, "x must be positive"

# Printing for debugging
# print(f"Debug: {variable}")

# Using pdb (Python Debugger)
import pdb
pdb.set_trace()  # Breakpoint

# Logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

# Unit Testing
import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
    
    def setUp(self):
        """Run before each test"""
        pass
    
    def tearDown(self):
        """Run after each test"""
        pass


# ============================================================================
# 23. VIRTUAL ENVIRONMENTS AND PACKAGES
# ============================================================================

# Creating virtual environment
# python -m venv myenv
# myenv\Scripts\activate  (Windows)
# source myenv/bin/activate  (Mac/Linux)

# Installing packages
# pip install package_name
# pip install -r requirements.txt
# pip list
# pip freeze > requirements.txt

# Uninstalling packages
# pip uninstall package_name


# ============================================================================
# 24. CONDITIONAL EXPRESSIONS (CONDITIONAL ASSIGNMENT)
# ============================================================================

# Ternary operator
x = 10
result = "positive" if x > 0 else "non-positive"

# Chained conditionals
result = "positive" if x > 0 else "negative" if x < 0 else "zero"

# Short-circuit evaluation
value = x or 0  # Use x if truthy, else 0
value = x and "valid" or "invalid"


# ============================================================================
# 25. SLICING AND INDEXING
# ============================================================================

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic Indexing
lst[0]  # 0
lst[-1]  # 9
lst[-2]  # 8

# Slicing [start:stop:step]
lst[2:5]  # [2, 3, 4]
lst[:5]  # [0, 1, 2, 3, 4]
lst[5:]  # [5, 6, 7, 8, 9]
lst[:]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst[::2]  # [0, 2, 4, 6, 8]
lst[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
lst[2:8:2]  # [2, 4, 6]
lst[-3:]  # [7, 8, 9]
lst[:-2]  # [0, 1, 2, 3, 4, 5, 6, 7]


# ============================================================================
# 26. NUMPY - NUMERICAL COMPUTING
# ============================================================================

import numpy as np

# Creating Arrays
np.array([1, 2, 3])  # From list
np.zeros(5)  # [0. 0. 0. 0. 0.]
np.ones(5)  # [1. 1. 1. 1. 1.]
np.arange(5)  # [0 1 2 3 4]
np.arange(0, 10, 2)  # [0 2 4 6 8]
np.linspace(0, 10, 5)  # [0. 2.5 5. 7.5 10.]
np.logspace(0, 2, 5)  # Logarithmic spacing
np.eye(3)  # Identity matrix
np.diag([1, 2, 3])  # Diagonal matrix
np.random.rand(3, 3)  # Random 3x3 array
np.random.randint(0, 10, 5)  # Random integers
np.random.normal(0, 1, 100)  # Normal distribution

# 2D Arrays (Matrices)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_2d.shape  # (2, 3)
arr_2d.ndim  # 2 (dimensions)
arr_2d.size  # 6 (total elements)
arr_2d.dtype  # dtype('int64')

# Array Indexing and Slicing
arr = np.array([1, 2, 3, 4, 5])
arr[0]  # 1
arr[-1]  # 5
arr[1:3]  # [2 3]
arr[::2]  # [1 3 5]

# 2D Indexing
arr_2d[0]  # First row: [1 2 3]
arr_2d[0, 1]  # Element at row 0, col 1: 2
arr_2d[:, 1]  # All rows, column 1
arr_2d[0, :]  # Row 0, all columns
arr_2d[0:2, 1:3]  # Subarray

# Array Operations
arr + 5  # Add to all elements
arr * 2  # Multiply each element
arr ** 2  # Square each element
np.sqrt(arr)  # Square root
np.exp(arr)  # Exponential
np.log(arr)  # Natural logarithm
np.sin(arr)  # Sine
np.cos(arr)  # Cosine

# Element-wise Operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr1 + arr2  # [5 7 9]
arr1 * arr2  # [4 10 18]
arr1 ** arr2  # [1 32 729]

# Matrix Operations
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
mat1 + mat2  # Element-wise addition
mat1 @ mat2  # Matrix multiplication
np.dot(mat1, mat2)  # Matrix multiplication
mat1.T  # Transpose
np.linalg.inv(mat1)  # Inverse
np.linalg.det(mat1)  # Determinant
np.linalg.eig(mat1)  # Eigenvalues and eigenvectors
np.linalg.solve(mat1, np.array([1, 2]))  # Solve linear system

# Aggregation Functions
arr = np.array([1, 2, 3, 4, 5])
arr.sum()  # 15
arr.mean()  # 3.0
arr.std()  # Standard deviation
arr.var()  # Variance
arr.min()  # 1
arr.max()  # 5
np.median(arr)  # 3.0
np.percentile(arr, 75)  # 75th percentile

# Along axis (for 2D arrays)
arr_2d.sum(axis=0)  # Sum columns
arr_2d.sum(axis=1)  # Sum rows
arr_2d.mean(axis=0)  # Mean of columns

# Reshaping
arr = np.arange(12)
arr.reshape(3, 4)  # 3x4 matrix
arr.reshape(-1, 3)  # Auto-calculate dimension
arr.flatten()  # Flatten to 1D
arr.ravel()  # Flatten to 1D

# Concatenation
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
np.concatenate([a1, a2])  # [1 2 3 4 5 6]
np.vstack([a1, a2])  # Vertical stack
np.hstack([a1, a2])  # Horizontal stack

# Boolean Indexing
arr = np.array([1, 2, 3, 4, 5])
arr > 2  # [False False True True True]
arr[arr > 2]  # [3 4 5]
arr[(arr > 2) & (arr < 5)]  # [3 4]

# Sorting and Searching
arr = np.array([3, 1, 4, 1, 5])
np.sort(arr)  # [1 1 3 4 5]
np.argsort(arr)  # Indices that sort array
np.where(arr > 2)  # Indices where condition is true
np.unique(arr)  # Unique elements


# ============================================================================
# 27. PANDAS - DATA ANALYSIS AND MANIPULATION
# ============================================================================

import pandas as pd

# Series (1D)
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s['a']  # 1
s[0]  # 1
s.values  # [1 2 3 4]
s.index  # Index(['a', 'b', 'c', 'd'], dtype='object')

# DataFrame (2D)
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
})

# Accessing Data
df['name']  # Column as Series
df[['name', 'age']]  # Multiple columns
df.iloc[0]  # First row
df.loc[0]  # Row with label 0
df.iloc[0, 1]  # Element at row 0, col 1
df.at[0, 'age']  # Element by label
df.iat[0, 1]  # Element by position

# DataFrame Properties
df.shape  # (3, 3)
df.columns  # Column names
df.index  # Row indices
df.dtypes  # Data types
df.info()  # Summary info
df.describe()  # Statistical summary
df.head()  # First 5 rows
df.tail()  # Last 5 rows
len(df)  # Number of rows

# Creating DataFrames
# pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
# pd.DataFrame({'x': [1, 2], 'y': [3, 4]})
# pd.read_csv('file.csv')  # From CSV
# pd.read_excel('file.xlsx')  # From Excel
# pd.read_json('file.json')  # From JSON
# pd.read_sql('SELECT * FROM table', connection)  # From SQL

# Data Manipulation
df['salary'] = [5000, 6000, 7000]  # Add column
df.drop('city', axis=1)  # Drop column
df.drop(0)  # Drop row
df.rename(columns={'age': 'years'})  # Rename columns
df.set_index('name')  # Set index
df.reset_index()  # Reset index

# Filtering and Selection
df[df['age'] > 25]  # Filter rows
df[(df['age'] > 25) & (df['city'] == 'NYC')]  # Multiple conditions
df.query('age > 25')  # Query
df.isin(['NYC', 'LA'])  # Check membership

# Sorting
df.sort_values('age')  # Sort by column
df.sort_values(['age', 'name'])  # Sort by multiple
df.sort_values('age', ascending=False)  # Descending
df.sort_index()  # Sort by index

# Grouping and Aggregation
df.groupby('city').size()  # Count per group
df.groupby('city')['age'].mean()  # Mean age per city
df.groupby('city').agg({'age': 'mean', 'salary': 'sum'})  # Multiple agg
df.pivot_table(values='salary', index='city', aggfunc='sum')  # Pivot table

# Missing Data
df.isnull()  # Check for null
df.notnull()  # Check for non-null
df.dropna()  # Drop rows with null
df.fillna(0)  # Fill null with value
df.fillna(method='ffill')  # Forward fill
df.fillna(method='bfill')  # Backward fill

# Data Types
df.astype({'age': 'float'})  # Convert type
pd.to_numeric(df['age'])  # Convert to numeric
pd.to_datetime(df['date'])  # Convert to datetime

# String Operations (on columns)
df['name'].str.upper()  # Uppercase
df['name'].str.lower()  # Lowercase
df['name'].str.len()  # Length
df['name'].str.startswith('A')  # Check prefix
df['name'].str.contains('li')  # Check substring
df['name'].str.replace('a', 'X')  # Replace

# Merging and Joining
df1 = pd.DataFrame({'key': ['a', 'b'], 'val': [1, 2]})
df2 = pd.DataFrame({'key': ['a', 'b'], 'val2': [3, 4]})
pd.merge(df1, df2, on='key')  # Inner join
pd.merge(df1, df2, on='key', how='left')  # Left join
pd.concat([df1, df2], axis=0)  # Vertical concatenation
pd.concat([df1, df2], axis=1)  # Horizontal concatenation

# Writing Data
# df.to_csv('file.csv', index=False)  # To CSV
# df.to_excel('file.xlsx', index=False)  # To Excel
# df.to_json('file.json')  # To JSON
# df.to_sql('table_name', connection)  # To SQL
df.to_html()  # To HTML

# Applying Functions
df['name'].apply(len)  # Apply function to column
df[['age', 'salary']].apply(np.sum)  # Apply to rows
df.applymap(lambda x: x**2)  # Element-wise apply

# Iterating
for idx, row in df.iterrows():
    print(idx, row['name'])

for idx, row in df.itertuples(index=True):
    print(row)

# Duplicate Handling
df.duplicated()  # Check duplicates
df.drop_duplicates()  # Remove duplicates
df.drop_duplicates(subset=['name'])  # Remove by column


# ============================================================================
# 28. MATPLOTLIB - DATA VISUALIZATION
# ============================================================================

import matplotlib.pyplot as plt
import numpy as np

# Basic Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sine Wave')
plt.show()

# Figure and Axes
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Sine Wave')
plt.show()

# Multiple Subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, np.sin(x))
axes[0, 1].plot(x, np.cos(x))
axes[1, 0].plot(x, x**2)
axes[1, 1].plot(x, np.log(x + 1))
plt.show()

# Line Styles and Colors
plt.plot(x, y, color='red', linestyle='--', linewidth=2, label='sin(x)')
plt.plot(x, np.cos(x), 'b-', label='cos(x)')
plt.plot(x, np.tan(x), 'g:', label='tan(x)')
plt.legend()  # Add legend
plt.show()

# Scatter Plot
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y, alpha=0.5, s=30, c='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

# Bar Plot
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]
plt.bar(categories, values, color='skyblue', edgecolor='navy')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.show()

# Horizontal Bar Plot
plt.barh(categories, values, color='lightgreen')
plt.xlabel('Values')
plt.title('Horizontal Bar Plot')
plt.show()

# Pie Chart
sizes = [30, 25, 20, 25]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'blue', 'green', 'yellow']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.show()

# Heatmap (using numpy)
data = np.random.randn(10, 10)
plt.imshow(data, cmap='hot', aspect='auto')
plt.colorbar()  # Add color scale
plt.title('Heatmap')
plt.show()

# Box Plot
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data, labels=['Std=1', 'Std=2', 'Std=3'])
plt.ylabel('Value')
plt.title('Box Plot')
plt.show()

# Violin Plot
plt.violinplot(data, positions=range(3))
plt.xticks(range(3), ['Std=1', 'Std=2', 'Std=3'])
plt.ylabel('Value')
plt.title('Violin Plot')
plt.show()

# Plot Styling
plt.style.use('ggplot')  # Use style preset
plt.figure(figsize=(10, 6))  # Set figure size
plt.plot(x, y)
plt.tight_layout()  # Adjust spacing
plt.show()

# Saving Figures
plt.plot(x, y)
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.savefig('plot.pdf')

# Customization
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2, label='sin(x)')
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_title('Sine Wave', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)  # Add grid
ax.legend(loc='upper right')
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
plt.show()

# 3D Plot
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# x = np.linspace(-5, 5, 100)
# y = np.linspace(-5, 5, 100)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(np.sqrt(X**2 + Y**2))
# ax.plot_surface(X, Y, Z)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
plt.show()

# Subplots with Different Plots
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].plot(x, np.sin(x))
axes[0].set_title('Line Plot')
axes[1].scatter(np.random.randn(50), np.random.randn(50))
axes[1].set_title('Scatter Plot')
axes[2].hist(np.random.randn(1000), bins=30)
axes[2].set_title('Histogram')
plt.show()

# Interactive Features
plt.ion()  # Turn on interactive mode
plt.plot(x, y)
plt.draw()
plt.pause(2)
plt.close()

# Contour Plot
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
plt.contour(X, Y, Z, levels=10)
plt.colorbar()
plt.title('Contour Plot')
plt.show()

# Filled Contour Plot
plt.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar()
plt.title('Filled Contour Plot')
plt.show()


print("Python Commands and Properties Guide Complete!")
