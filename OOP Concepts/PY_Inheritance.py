"""

Inheritance in Python allows a class to inherit attributes and methods from another class. 
The class that is inherited from is called the parent class (or base class), 
and the class that inherits is called the child class (or derived class).

Key Points:
    1. Inheritance promotes code reusability.
    2. Child classes can override methods of the parent class.
    3. Python supports ***multiple inheritance***, where a class can inherit from multiple classes.
    4. The super() function is used to call methods from the parent class.

Types of Inheritance:
    1. Single Inheritance: A child class inherits from one parent class.
    2. Multiple Inheritance: A child class inherits from multiple parent classes.
    3. Multilevel Inheritance: A child class inherits from a parent class, which is also a child class of another parent class.
    4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
    5. Hybrid Inheritance: A combination of two or more types of inheritance.

"""


#Topic 1: Single Inheritance
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"
    

"""
The code above dosen't directly use inheritance or does not inherit from any explicit parent or base class.
But even if a class does not explicitly inherit from another class, it implicitly inherits from the built-in object class in Python.

So internally, class is treated like:
    class class_name(object):
    ...


=> Why does every class in python implilcitly inherit form object class?

This is because the object class is the root of all classes in Python.
It provides default implementations for several special methods that are common 
to all objects, such as : 

Python special method (also called dunder methods)


__str__(self): Returns a human-readable string representation of the object. Used by print() and str().
__repr__(self): Returns an unambiguous string representation meant for debugging. Used by repr() and interactive console. Ideally should be valid Python code to recreate the object.
__eq__(self, other): Defines behavior for equality operator ==.
__lt__(self, other): Defines behavior for < (less than).
__le__(self, other): Defines behavior for <= (less than or equal).
__gt__(self, other): Defines behavior for > (greater than).
__ge__(self, other): Defines behavior for >= (greater than or equal).
__ne__(self, other): Defines behavior for != (not equal).
__hash__(self): Returns a hash value, allowing the object to be used in sets or as dictionary keys. Must be consistent with __eq__.
__call__(self): Makes an object behave like a function when called with ().
__len__(self): Defines behavior for len() function.
__getitem__(self, key): Defines behavior for accessing items using square brackets (e.g., obj[key]).
__setitem__(self, key, value): Defines behavior for setting items using square brackets (e.g., obj[key] = value).
__delitem__(self, key): Defines behavior for deleting items using square brackets (e.g., del obj[key]).
__iter__(self): Defines behavior for iteration (e.g., for item in obj:).
__next__(self): Defines behavior for the next() function in iteration.
__contains__(self, item): Defines behavior for the in operator (e.g., item in obj).
__enter__(self): Defines behavior for entering a context (e.g., with statement).
__exit__(self, exc_type, exc_value, traceback): Defines behavior for exiting a context (e.g., with statement).
__init__(self, *args, **kwargs): Initializes a new instance of the class.
__new__(cls, *args, **kwargs): Creates a new instance of the class (before __init__).
__del__(self): Defines behavior for object deletion (e.g., del obj).
__distr__(self): Defines behavior for object destruction (called when an object is about to be destroyed).
__dist__(self): Defines behavior for object distribution (used in some advanced scenarios).
and others.

"""


#Topic 2: Explicit single inheritance
class Person:
    def __init__(self, name):
        self.name = name

class BankAccount(Person):  # Inheriting from Person class
    def __init__(self, account_number, balance, name):
        super().__init__(name)  # Call the constructor of the parent class
        self.account_number = account_number
        self.balance = balance

    def display_account_info(self):
        return f"Name: {self.name}, Account Number: {self.account_number}, Balance: {self.balance}"
    
"""
Super() Function:
    1. The super() function is used to call methods from a parent class.
    2. It is commonly used in the constructor of a child class to initialize attributes inherited from the parent class.
    3. It helps avoid explicitly naming the parent class, making the code more maintainable.
    4. It can also be used to call other methods from the parent class.
    5. It returns a proxy object that lets you call methods from a parent (super) class without explicitly naming the parent.
    6. super() is defined in Python’s core built-in namespace.
    7. You don’t need to import it — it’s automatically available.
"""


#Topic 3: Multiple Inheritance

"""
Lets understand multiple inheritance first.

ParentClass1       ParentClass2
      \                 /
       \               /
        \             /
         \           /
          \         /
           \       /
            \     /
           ChildClass
   

So a child class can inherit attributes and methods from more than one parent class.



Eg: In real world banking app.

-> A BankAccount "has a" Person(or Customer).
-> An Employee "is a" Person.
-> But a BankAccount "is not a" Person.


--> So Employee is-a Person

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Inheriting from Person class
    def __init__(self, employee_id, name):
        super().__init__(name)  # Call the constructor of the parent class
        self.employee_id = employee_id

    def display_employee_info(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}"


--> A Bank Account "is not a" person or an employee-it belongs to a person/employee.


class BankAccount:
    def __init__(self, account_number, balance, owner: Person):  # here owner is an object of class Person
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def display_account_info(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}, Owner: {self.owner.name}"

 --> With Diamong inheritance problem

      Person
     /      \
Employee   Person
     \      /
   BankAccount

--> Here BankAccount inherits from Person twice through Employee and directly.         

--> Diamond inheritance structure

      Person
     /      \
Employee   (direct)
     \      /   
   BankAccount


Note** : Multiple Inheritance shines when you are mixing orthogonal capabilities, means independent
or unrelated in purpose like two features that do not overlap or interfere with each other.

--> Python multiple inheritance allows a class to combine several independent behaviours from different sources.


Example: A BankAccount that can:
    -: Log every transaction -> Loggable mixin
    -: Serialize its data to JSON -> Serializable mixin
    -: Validate its data -> Validatable mixin
"""

class Loggable:
    def log(self, message):
        print(f"Log: {message}")


class Serializable:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)


class Validatable:
    def validate(self):
        # Basic validation logic
        for key, value in self.__dict__.items():
            if value is None:
                print(f"Validation failed: {key} is None")
                return False
        print("Validation succeeded")
        return True

class BankAccount(Loggable, Serializable, Validatable):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.log("BankAccount created")
        self.validate()

        
acc = BankAccount("123456", 1000)
print(acc.to_json())
# Output:
# Log: BankAccount created


"""
Method Resolution Order (MRO)

    1. In multiple inheritance, the order in which base classes are searched when executing a method is called the Method Resolution Order (MRO).
    2. Python uses the C3 linearization algorithm to determine the MRO.
    3. You can view the MRO of a class using the __mro__ attribute or the mro() method.
    4. The MRO ensures that a class is always checked before its parent classes, and parent classes are checked in the order they are listed in the class definition.
    5. Understanding MRO is crucial when dealing with multiple inheritance to avoid unexpected behavior.

# Example to demonstrate MRO
    class A:
        def show(self):
            print("A")
    class B(A):
        def show(self):
            print("B")
    class C(A):
        def show(self):
            print("C")
    class D(B, C):
        pass
    d = D()
    d.show()  # Output: B

    print(D.__mro__)
    # Output: 
    # <class '__main__.D'>
    # <class '__main__.B'>
    # <class '__main__.C'> 
    # <class '__main__.A'>
    # <class 'object'>

# Understanding the MRO Logic (C3 Linearization)

Python uses C3 linearization to determine method lookup order. It resolves in a way that respects:

    -> Child before Parent (D before B before C before A)

    -> Left-to-right order of inheritance (B before C because class D(B, C))

    -> Avoids duplicating shared ancestors (A appears only once!)

So when Python builds the order, it merges the inheritance trees while preserving order:
"""


#Topic 4: Multilevel Inheritance

"""
Multilevel inheritance occurs when a class inherits from a derived class, 
creating a chain of inheritance.


Grandparent → Parent → Child


syntax:
    class Grandparent:
        pass

    class Parent(Grandparent):
        pass

    class Child(Parent):
        pass
"""


"""
Right Real-World Scenario: Modeling Organizational Roles

Problem:
    -> A generic Person
    -> An Employee (a Person with job details)
    -> A Manager (an Employee with team-management abilities)


   This is a natural "is-a" hierarchy.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_Person_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age, employee_id, position):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.position = position

    def display_Employee_info(self):
        return (super().display_Person_info() +
                f", Employee ID: {self.employee_id}, Position: {self.position}")

class Manager(Employee):
    def __init__(self, name, age, employee_id, position, team_size):
        super().__init__(name, age, employee_id, position)
        self.team_size = team_size

    def display_Manager_info(self):
        return (super().display_Employee_info() +
                f", Team Size: {self.team_size}")
    
# Example usage
mgr = Manager("Alice", 35, "E123", "Project Manager", 10)
print(mgr.display_Manager_info())
# Output: Name: Alice, Age: 35, Employee ID: E123, Position: Project Manager, Team Size: 10
print(mgr.display_Employee_info())
# Output: Name: Alice, Age: 35, Employee ID: E123, Position: Project Manager
print(mgr.display_Person_info())
# Output: Name: Alice, Age: 35


"""
A Manager "is an" Employee, and an Employee "is a" Person.

"""

"""
Wrong Real-World Scenario: Forcing Unnatural Hierarchies

Anti-pattern:


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        return "Moving..."

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def honk(self):
        return "Beep beep!"

# WRONG: A BankAccount "is NOT a" Car!
class BankAccount(Car):
    def __init__(self, account_number, balance, brand, model):
        super().__init__(brand, model)  # Why does a bank account need brand/model?
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount


-> Violates the "is-a" principle: A BankAccount is not a type of Car or Vehicle.
-> Introduces irrelevant attributes (brand, model) to BankAccount.
-> Leads to confusion and maintenance challenges.


"""

"""
How to Fix the Wrong Example?

Use composition, not inheritance:

"""
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class BankAccount:
    def __init__(self, account_number, balance, owner: Person):  
        self.account_number = account_number
        self.balance = balance
        self.owner = owner # Account Owner has a relationship with Person

    def withdraw(self, amount):
        self.balance -= amount


class car:
    def __init__(self, brand, model, owner: Person):
        self.brand = brand
        self.model = model
        self.owner = owner # Car Owner has a relationship with Person

    def honk(self):
        return "Beep beep!"
    

"""
Real-World Valid Examples of Multilevel Inheritance

1. UI Frameworks
Widget → Button → RoundedButton → AnimatedRoundedButton


2. Exceptions in Python
BaseException → Exception → ValueError → CustomValidationError

3. File Handling
File → TextFile → LogFile → RotatingLogFile

"""