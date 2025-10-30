"""
Abstraction in Python:

Abstraction is one of the fundamental concepts of Object-Oriented Programming (OOP). 
It allows you to focus on the essential features of an object while hiding the unnecessary details. 
In Python, abstraction can be achieved through abstract classes and interfaces.

Key Points:
1. Abstraction helps in reducing complexity by hiding unnecessary details.
2. It allows you to define a blueprint for a group of related classes.
3. Abstract classes cannot be instantiated directly.
4. Subclasses must implement the abstract methods defined in the abstract class.

"""


# Topic 1: Understanding Abstraction with Abstract Base Classes (ABC)
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def num_sides(self):
        pass

    @abstractmethod
    def radius(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
rectangle = Rectangle(5, 10)
print("Rectangle Area:", rectangle.area())           # Output: Rectangle Area: 50
# In the above code, we define an abstract class Shape with two abstract methods: area and perimeter.
# The Rectangle class inherits from Shape and provides implementations for the abstract methods.


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

circle = Circle(7)
print("Circle Area:", circle.area())                 # Output: Circle Area: 153.93804002589985
# The Circle class inherits from Shape and provides implementations for the abstract methods.


#Topic 2: Components of Abstraction
"""
Components of Abstraction:
1. Abstract Method:
    - A method that is declared but contains no implementation.
    - It is defined using the @abstractmethod decorator.
    - Subclasses must provide an implementation for all abstract methods.
2. Abstract Class:
    - A class that contains one or more abstract methods.
    - It cannot be instantiated directly.
    - It serves as a blueprint for other classes.
3. Concrete Class:
    - A class that provides implementations for all abstract methods of its abstract superclass.
    - It can be instantiated to create objects.
4. Interface:
    - A contract that defines a set of methods that a class must implement.
    - In Python, interfaces can be created using abstract base classes (ABC).
5. Abstract properties:
    - Similar to abstract methods, but for properties.
    - They are defined using the @property decorator in conjunction with @abstractmethod.
    - Subclasses must implement these properties.
6. Class Instantiation rules:
    - Abstract classes cannot be instantiated directly.
    - Concrete classes must implement all abstract methods before they can be instantiated.
"""

# Example of Abstract Property
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @property
    @abstractmethod
    def num_wheels(self):
        pass
class Car(Vehicle):
    @property
    def num_wheels(self):
        return 4
car = Car()
print("Car Wheels:", car.num_wheels)  # Output: Car Wheels: 4

#Why Abstract property is used in above example?
# In the above code, we define an abstract class Vehicle with an abstract property num_wheels.
# The Car class inherits from Vehicle and provides an implementation for the abstract property.


# Topic 3: Understanding the indepth concept of abstract class and interface in python


#Abstract Class vs Interface:
#1. Abstract Class:
# - Can have both abstract methods (without implementation) and concrete methods (with implementation).
# example:
from abc import ABC, abstractmethod
class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass

    def my_concrete_method(self):
        return "This is a concrete method"
# __________________________________________________________
# - Can have instance variables and constructors.
# example:
from abc import ABC, abstractmethod
class MyAbstractClass(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def my_abstract_method(self):
        pass
#__________________________________________________________              
# - A class can inherit from only one abstract class (single inheritance).
#  example:
from abc import ABC, abstractmethod
class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass

class MyConcreteClass(MyAbstractClass):
    def my_abstract_method(self):
        return "Implementation of abstract method"

#  example 2:
from abc import ABC, abstractmethod
class AnotherAbstractClass(ABC):
    @abstractmethod
    def another_abstract_method(self):
        pass

# This will raise an error because Python does not support multiple inheritance from abstract classes
class InvalidClass(MyAbstractClass, AnotherAbstractClass):
    def my_abstract_method(self):
        return "Implementation of abstract method"

    def another_abstract_method(self):
        return "Implementation of another abstract method"
#___________________________________________________________
# 2. Interface:
# - Can only have abstract methods (without implementation).
# example:
from abc import ABC, abstractmethod
class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass
#___________________________________________________________
# - Cannot have instance variables or constructors.
# example:
from abc import ABC, abstractmethod
class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass
# ___________________________________________________________
# - A class can implement multiple interfaces (multiple inheritance).
# example:
from abc import ABC, abstractmethod
class InterfaceA(ABC):
    @abstractmethod
    def method_a(self):
        pass

class InterfaceB(ABC):
    @abstractmethod
    def method_b(self):
        pass

class MyConcreteClass(InterfaceA, InterfaceB):
    def method_a(self):
        return "Implementation of method A"

    def method_b(self):
        return "Implementation of method B"
# ___________________________________________________________
