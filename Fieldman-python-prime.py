######################################
#######  PYTHON FIELD MANUAL #########
######################################

# Only what needed
# Python: easy quickscript, optimistic, step-by-step execution
# Runs and checks line-by-line (runtime errors only)
# Naming style: snake_case, Blocks: 4 space indentation

#=========================================
#== PRINT
x = 10
p = 0.45
print("Result:", p * x) # | Result: 4.5

str1 = "Text"
str2 = 'Text' # same as double-quotes
str3 = \
"On next line"

print(str1 * 2) # | TextText

10 ** (-27)


#=========================================
#== SCRIPT SCAFFOLD
#!/usr/bin/env python3
import sys

def main():
    for arg in sys.argv[1:]:
        print arg

if __name__ == "__main__":
    main()
# Set indentation to 4 spaces.

#=========================================
#== STRING FORMAT (pyth 3.6)
name = "Bob"
f_string = f"Hello, {name}"

template_string = "Hello, {}. Today is {}"
with_name = template_string.format(name, "monday")

square_meters = 4.98765
print(f"{square_meters:.2f}")


#=========================================
#== UTIL
id(x)       # memory related id
a = None    # Null


#=========================================
#== DISCOVERY
sp = []
# On any object:
dir(sp)         # available methods
help(sp)        # doc help
help(sp.copy)   # works on methods


#=========================================
#== INPUT (can use redirects of standard input)
#name = input("Enter your name: ") # .lower()
#age_input = input("Age: ")
#age = int(age_input) # also: int(input())


#=========================================
#== BOOLEAN (True // False)
5 == 5   # structural equality
x is x   # referential equality


"Bob" in ["Bob", "Smith"] # True
"B" in "Bob"


#=========================================
#== IF STATEMENT
if x == 10:
    pass # No-op
elif x != 12 and x in (1, 2, 3):
    pass
else:
    pass


#=========================================
#== LOOP
while x > 10:
    break
    continue

while (user_input := input(menu_text)) != "3": # Walrus operator (pyth 3.8)
        pass

for x in [1, 2, 3]:
    print(x, end=", ")


#=========================================
#== TUPLE
t = (1, "Text", 2)  # Can omit brackets
t_one = (1,)        # One element tuple


#=========================================
#== LIST
l = ["Bob", "Bob", "Rolf", "Smith"]
l[0] = "Something"
l.append("Smith")
list(t) # Convert to list
len(l)
sum([1, 2, 3])


#=========================================
#== SET
s1 = {"Bob", "Rolf"}
s2 = {"Bob"}
sd = s1.difference(s2) # Set difference (minus operation)
su = s1.union(s2)
si = s1.intersection(s2)


#=========================================
#== DICTIONARY
d = {"Hero": 30, "Book": 15}
d["Sword"] = 10
for key in d:
    print(key)
for key, value in d.items():
    print(f"{key}: {value}")


#=========================================
#== LIST COMPREHENSION
doubled = [n * 2 for n in [1, 3, 5]]
starts = [s for s in ["abc", "def"] if s.startswith("a")]


#=========================================
#== DICTIONARY COMPREHENSIONS
users = [
    (0, "Bob", "password"),
    (1, "Smith", "pass1"),
    (2, "Agent", "qwerty"),
]
username_mapping = {user[1]: user for user in users}
_, name, password = username_mapping["Bob"]


#=========================================
#== DESTRUCTURING VARIABLES (unpacking)
x, y = (5, 11)
x, y = 5, 11 # Can omit brackets, still is tuple

person = ("Bob", 20, "Janitor")
name, _, profession = person
head, *tail = person # Collect tail to list
*head, tail = person
first, second, third, *rest = [1, 2, 3, 4, 5]


#=========================================
#== SUBROUTINES
def f():
    print("Function")
f() # Run sub
a = 10
def g():
    a = a + 10 # Name shadowing. Creates local variable

def add(x, y=8): # Parameters, Default value
    pass
    return x + y
add(4, 8)        # Positional Arguments
add(x=4, y=23)   # Named Arguments


#=========================================
#== LAMBDA
lam = lambda x, y: x * y
(lambda a: print(a))(100)


#=========================================
#== HIGHER-ORDER FUNCTIONS
sequence = [1, 3, 5, 10]
doubled = map(lambda x: 2 * x, sequence) # returns map object
print(list(doubled))


#=========================================
#== VARARGS
def multiply(*args):
    print(args) # Is tuple
multiply(1, 3 ,5)

def apply(*args, operator): # Varargs + named parameter
    pass


#=========================================
#== KWARGS (keyword arguments)
def named(**kwargs): # Into dictionary
    for key, value in kwargs.items():
        print(f"{key} :: {value}")
named(a="text", b=100)
named(**d)

def combined(*args, **kwargs): # positional to args, named to kwargs
    pass


#=========================================
#== DESTRUCTURING ARGUMENTS
seq = [1, 4]
multiply(*seq)  # Destructure list to positional arguments
d = {"x": 10, "y": 20}
add(**d)        # Destructure dictionary to named arguments




#==============================================================================
#                            PYTHON OOP
#==============================================================================

#=========================================
#== CLASS
class Agent: # Class
    TYPES = ("Special", "Regular") # Class data (not instance)

    def __init__(self, name):   # Constructor
        self.name = name        # Field
        self.sequence = (10, 20, 40)

    def method_one(self):   # `self` is receiver of method-message
        return sum(self.sequence)

    def __str__(self):  # To string method
        return f"Agent: {self.name}"

    def __repr__(self): # Representation, is used in debugger and other cases
        return f"<Agent({self.name}, {self.sequence})>"

    def inst_method(self):  # Instance method
        pass

    @classmethod
    def class_method(cls):  # Class method, gets class
        pass                # Usually factories

    @staticmethod
    def static_method():    # Static method, gets no class
        pass                # Just to place method inside class

agent = Agent("Smith") # New object
print(agent.name, agent.method_one())
Agent.method_one(agent) # Equal to agent.method_one()
Agent.class_method()
print(Agent.TYPES)
print(agent)
print(f"{agent!r}") # uses repr


#=========================================
#== FACTORY-METHODS EXAMPLE
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self): # Also used if no __str__ exists
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


heavy = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)


#=========================================
#== INHERITANCE
class Hero:
    def __init__(name, hp):
        self.name = name
        self.hp = hp
    def method():
        pass

class Mage(Hero):
    def __init__(name, hp, mp):
        super().__init__(name, hp)
        self.mp = mp
    def method():
        super().method()


#=========================================
#== COMPOSItION
class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)
print(shelf)


#=========================================
#==  TYPE HINTING (pyth 3.5)
def aver(sequence: list) -> float: # Works with IDE or linter
    return sum(sequence) / len(sequence)

class Hero:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
    @classmethod
    def create_mighty(cls, hp: int) -> "Hero":
        return cls("Mighty", hp)
h = Hero.create_mighty(100)




#==============================================================================
#                            ADDITIONAL
#==============================================================================

#=========================================
#==  IMPORT
print("module: ", __name__) # Global variable with module name
def main():
    pass
if __name__ == "__main__":  # File that is directly run has __main__
    main()                  # Run code, when main only

# import sys 
# from somemodule import func
# from folder.module import smt
# Note: for python 2 should create __init__.py inside folders

import sys
print(sys.path) # Folders where to look for modules, including current dir
                # Also includes dir from PYTHONPATH env var

print(sys.modules) # Already imported list
print("=" * 70)


#=========================================
#==  RELATIVE IMPORT
# from .somemodule import divine    // From current folder
# from ..lib import *               // From parent folder
# Note: All this works with specific restrictions (must be some levels deep)


#=========================================
#==  ERROR HANDLING
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor

try:
    divide(10, 4)
except ZeroDivisionError as e:
    print("Error occured, while dividing:", e)
    raise  # Optional: re-raise same error
except ValueError:
    pass
else: # Run if `try` succeeded
    pass
finally:
    pass


#=========================================
#==  CUSTOM ERROR
class ThreeLessThanTwoError(ValueError):
    pass
if 3 < 2:
    raise ThreeLessThanTwoError(
        "How is that possible"
    )


#=========================================
#==  FIRST-CLASS FUNCtION
def add(a, b):
    return a + b

def calc(*values, operator): # Function as parameter
    return operator(*values)

calc(3, 4, operator=add)
calc(1, 2, 3, operator=lambda *args: sum(args))


#=========================================
#==  DECORATORS
user = {"username": "G1", "access_level": "guest"}

def just_get_secret():
    return "Secret data"

def make_secure(func): # Decorator 
    def secure_function():
        if user["access_level"] == "admin":
            return func() # Calls original function if check is True
        else:
            return "No permissions"
    return secure_function
get_data_function = make_secure(just_get_secret)
print(get_data_function()) # | No permissions


@make_secure  # Decorator
def decorated_get():
    return "Secured data"

print(decorated_get())
# Note: This decoration will mess function name and docs
print(decorated_get.__name__) # | secure_function
# To avoid this use wraps-decorator
import functools
def make_secure(func):
    @functools.wraps(func) # Use on inner function
    def secure_function():
        pass # <...>

# Decorated function with parameters
def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function

# Decorator factory, using parameters
def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}."

        return secure_function

    return decorator


@make_secure(
    "admin"
)  # This runs the make_secure function, which returns decorator.
def get_admin_password():
    return "admin: 1234"


@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


#=========================================
#==  MUTABILITY
a = []
b = a # Same object in memory
print(id(a))
print(id(b))
a.append(35) # List is mutable
print(a, b)
# Note: Tuples, Strings, Integers are immutable

# Important: don't use mutable types for default parameters
# Example:
from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = []):  # This is bad!
        self.name = name
        self.grades = grades

class Student:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []  # New list created if one isn't passed




