"""
Python def Keyword Functions: def keyword is used to 
define a function, it is placed before a function name 
that is provided by the user. 

Syntax:
def function_name(parameters):
    # function body
    return value
"""


# Example 1: Calling a function without parameters
def greet():
    return "Hello, World!" 
print(greet())  # Output: Hello, World!

# Note: Here greet() is a function call that invokes the greet function and returns the string "Hello, World!" 
# which is then printed to the console.
# but if we just write greet without parentheses, it will return the function object itself, 
# not the result of calling the function.
print(greet)    # Output: <function greet at 0x7f9bc8c1d160>


# Example 2: Calling a function with parameters
def add(a, b):
    return a + b
print(add(5, 3))  # Output: 8


# Example 3: Function with default parameter values
def greet_user(name="Guest"):
    return f"Hello, {name}!" # here f-string is used for string formatting.
print(greet_user())          # Output: Hello, Guest!
print(greet_user("Alice"))   # Output: Hello, Alice!


# Example 4: Function with keyword arguments
def describe_person(name, age):
    return f"{name} is {age} years old." # here f-string is used for string formatting.
print(describe_person("Alice", 30))  # Output: Alice is 30 years old.


# Example 5: Function with variable-length arguments
def sum_all(*args):
    return sum(args) #sum is a built-in function in Python that returns the sum of all items in an iterable.
print(sum_all(1, 2, 3))        # Output: 6
print(sum_all(5, 10, 15, 20))   # Output: 50


def multiply(*args):
    result = 1 # Initialize result to 1 (multiplicative identity)
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))  # 24

# Example 6: Function with Arbitrary Keyword Arguments
# What is arbitrary keyword arguments?
# In Python, arbitrary keyword arguments allow a function to accept any number of keyword arguments (i.e., named arguments).
# This is done using the double asterisk (**) syntax in the function definition.
# The keyword arguments are passed to the function as a dictionary, where the keys are the argument names and the values are the corresponding argument values.
# Syntax: def function_name(**kwargs): where kwargs is a common convention, but you can use any valid variable name.
# will it accept list or tuple as input? No, it only accepts keyword arguments in the form of key-value pairs.
# when is it useful? It is useful when you want to create functions that can handle a variable number of keyword arguments,
# allowing for more flexible and dynamic function calls.
# Give us a real-world example:
# A function that prints user information, where the user can provide any number of details about themselves.
# like name, age, city, occupation, etc.
def print_info(**kwargs):
    for key, value in kwargs.items(): # Here items() method is used to get key-value pairs from the dictionary.
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York


# Example 7: Function with a return statement
def multiply(x, y):
    return x * y
result = multiply(4, 5)
print(result)  # Output: 20

# Example 8: Function without a return statement
def print_message(message):
    print(message)  
print_message("Hello, Python!")  # Output: Hello, Python!


# Example 9: Nested Functions
def calculate(operation, a, b):
    def add(x, y):
        return x + y
    
    def multiply(x, y):
        return x * y
    
    if operation == "add":
        return add(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    else:
        return "Invalid operation"

print(calculate("add", 5, 3))        # 8
print(calculate("multiply", 5, 3))   # 15


# Example 10: Lambda Functions
# A lambda function in Python is a small, anonymous 
# function defined using the lambda keyword. 
# It’s typically used when a short function is needed 
# for a short time.
# Lambda functions can take any number of arguments but can only have a single expression.
# Syntax: lambda arguments: expression

square = lambda x: x * x
print(square(5))  # Output: 25

add = lambda a, b: a + b
print(add(3, 4))  # Output: 7

# Lambda functions can be used wherever function objects are required.
# What is function object? 
# In Python, functions are first-class citizens, meaning they can be treated like any other object (e.g., integers, strings, lists).
# A function object is simply a reference to a function that can be passed around and invoked.
# They are often used in higher-order functions like map(), filter(), and reduce().


"""
Lets first understand what is function object in python:

By Definition: A function object is a first-class object that represents a callable block of code. In python functions are objects,
just like integers or lists. We can store them in a variable, pass them to other functions, attach attributes to them and 
return them from functions.


What that means:
1. First-class: means we can assign, pass, return, and store functions just like any other object.
2. Callable: means we can invoke or call the function using parentheses (f(..)). eg: f(1, 2)
3. Introspectable: means we can examine the properties of the function object, such as its name, docstring, annotations, etc. eg: f.__name__, f.__doc__
4. Mutable: means we can add or modify attributes of the function object. eg: f.custom_attr = 42
5. Distinct from methods: functions defined within a class become methods when accessed via an instance, with 'self' bound automatically.
"""

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers)) # Here map() function applies the lambda function to each item in the numbers list.
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


"""  Memory Diagram for the above code:
                 ┌───────────────────────────────┐
numbers ────────► [id:2001] [1,2,3,4,5]
                 │          │  │  │  │  │
                 │          ▼  ▼  ▼  ▼  ▼
                 │      [101][102][103][104][105]
                 └───────────────────────────────┘

lambda ─────────► [id:3001] <function λ x: x*x>

map(...) ───────► [id:4001] iterator using [3001] & [2001]

squared_numbers ─► [id:5001] [1,4,9,16,25]
                            │  │  │  │  │
                            ▼  ▼  ▼  ▼  ▼
                        [106][107][108][109][110]
"""


# Example 11: Recursive Functions
# A recursive function is a function that calls itself in order to solve a problem.
# It typically has a base case to terminate the recursion and a recursive case to continue the recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120


"""
Memory (Heap)
+----------------------------------+
| [id:3001] function factorial(n)  |
+----------------------------------+
| [id:4001] int 120                |
+----------------------------------+

Stack (Namespace)
+----------------------------------+
| name: factorial → [id:3001]      |
| temporary return value → 120     |
+----------------------------------+
"""


# Example 12: Function Annotations
# Function annotations are a way to attach metadata to function parameters and return values.
def add(x: int, y: int) -> int: # Here -> int indicates that the function is expected to return an integer value.
    return x + y
print(add(3, 4))  # Output: 7
print(add.__annotations__)  # Output: {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}, here __annotations__ is a built-in attribute that stores the annotations of the function.


# Example 13: Using Closures
# A closure is a nested function that captures the "state" of its enclosing environment.
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
# Here closure is a function that adds 10 to its argument and returns the result. 
# Closure captures the value of x from the outer_function which is 10 in this case.
closure = outer_function(10) # Closure value is 10 initially.
print(closure(5))  # Output: 15, here closure(5) adds 10 (captured value) + 5 (argument) = 15
print(closure(20)) # Output: 30, here closure(20) adds 10 (captured value) + 20 (argument) = 30