"""
Python OOP Concepts

Key OOP concepts in Python include:
    1. Classes and Objects
    2. Inheritance
    3. Polymorphism
    4. Encapsulation
    5. Abstraction
    6. Method Overriding
    7. Constructors and Destructors
    8. Class and Instance Variables

"""


#Topic 1: Classes and Objects
class UserOrder:
    def __init__(self, order_id, user_id, product, quantity):
        self.order_id = order_id
        self.user_id = user_id
        self.product = product
        self.quantity = quantity

    def display_order(self):
        return f"Order ID: {self.order_id}, User ID: {self.user_id}, Product: {self.product}, Quantity: {self.quantity}"
    

#In the above code, we define a class UserOrder with attributes and a method to display order details.
# An object of the class can be created as follows:
order1 = UserOrder(101, 1, "Laptop", 2) #here order1 is an object of class UserOrder
print(order1.display_order()) #to call the method display_order of class UserOrder, we use the object order1
# Output: Order ID: 101, User ID: 1, Product: Laptop, Quantity: 2



#Lets understand the Constructors and Destructors in Python OOP

"""
__init__ Method (Constructor)

Key Points:
    1. The __init__ method is a special method in Python classes, known as the constructor.
    2. It is automatically called when an object of the class is created.
    3. It is used to initialize the attributes of the class.
    4. The first parameter of __init__ is always self, which refers to the instance being created.
    5. You can define additional parameters to pass values when creating an object.

Self keyword:
    1. The self keyword represents the instance of the class.
    2. It is used to access variables that belong to the class.
    3. It must be the first parameter of any function in the class.
    4. It is a convention to name it self, but you can use any name, like this, this_instance, etc.
    5. Using self allows you to differentiate between instance variables and local variables.
    6. It is used to call other methods within the class.
    7. self is a reference to the current object. It allows each object to store its own data.
    eg: 
           _________________________________________
            order1 = UserOrder(101, 1, "Laptop", 2)
            order2 = UserOrder(102, 2, "Phone", 1)

            print(order1.product)  # Laptop
            print(order2.product)  # Phone
          _________________________________________
    Each object has its own self, storing its own attributes.
    self ensures attributes are unique per object.


__del__ Method (Destructor)

Key Points:
    1. The __del__ method is a special method in Python classes, known as the destructor.
    2. It is called when an object is about to be destroyed or deleted.
    3. It is used to perform any cleanup actions, such as closing files or releasing resources.
    4. The __del__ method takes only one parameter, self, which refers to the instance being destroyed.
    5. It is not guaranteed to be called immediately when an object goes out of scope; it is called when the garbage collector destroys the object.
    6. You should avoid relying on __del__ for critical cleanup tasks, as its execution timing can be unpredictable.

syntax:
class ClassName:
    def __init__(self, parameters):
        # Constructor code here

    def __del__(self):
        # Destructor code here
"""


#Topic 2: Class and Instance Variables
class BankAccount:
    bank_name = "Global Bank"  # Class variable

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number  # Instance variable
        self.account_holder = account_holder    # Instance variable
        self.balance = balance                  # Instance variable

    def display_account_info(self):
        return f"Bank: {BankAccount.bank_name}, Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"
    

"""
Class Variables:
    1. Class variables are shared across all instances of a class.
    2. They are defined within the class but outside any instance methods.
    3. They can be accessed using the class name BankAccount.bank_name or through an instance like `self.bank_name`.
    4. Changes to a class variable affect all instances of the class.
"""

"""
Instance Variables:
    1. Instance variables are unique to each instance of a class.
    2. They are defined within the constructor (init method) using the self keyword.
    3. Each object can have different values for its instance variables.
    4. Changes to an instance variable do not affect other instances.
"""