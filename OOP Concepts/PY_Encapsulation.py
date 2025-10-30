"""
Encapsulation in Python:

Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP). 
It refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single unit, typically a class. 
Encapsulation helps to restrict direct access to some of an object's components, which can prevent the accidental modification of data.
Key Points:
1. Encapsulation is achieved using classes in Python.
2. It restricts access to certain components of an object, which is a means of preventing unintended interference and misuse of the methods and data.
3. In Python, encapsulation is implemented using access specifiers: public, protected, and private.
   - Public: Attributes and methods are accessible from outside the class.
   - Protected: Attributes and methods are accessible within the class and its subclasses.
   - Private: Attributes and methods are accessible only within the class.
4. Getter and Setter methods are often used to access and update the value of private attributes.

"""

# Topic 1: Encapsulation with Access Specifiers
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self._balance = balance                  # Protected attribute

    # Getter method for account_number
    def get_account_number(self):
        return self.__account_number

    # Setter method for account_number
    def set_account_number(self, account_number):
        self.__account_number = account_number

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    # Public method to check balance
    def get_balance(self):
        return self._balance # here we are accessing protected attribute, meaning it can be accessed within the class and its subclasses.
    
class BankCustomer(BankAccount):
    def display_balance(self):
        print(f"Current Balance: {self.get_balance()}") 



# Lets understand the public, private and protected attributes with syntax

"""
Access Specifiers in Python:
Syntax for attributes:
    public: attribute_name
    protected: _attribute_name
    private: __attribute_name
Syntax for methods:
    public: method_name(self, parameters)
    protected: _method_name(self, parameters)
    private: __method_name(self, parameters)

"""

# Now lets understand the public, private and protected attributes with examples

# Public Attribute Real World Example:
class Car:
    def __init__(self, make, model):
        self.make = make          # Public attribute
        self.model = model        # Public attribute
car = Car("Toyota", "Camry")
print("Car Make:", car.make)    # Output: Car Make: Toyota
print("Car Model:", car.model)  # Output: Car Model: Camry
# In the above code, make and model are public attributes of the Car class.
# They can be accessed directly from outside the class.
# Lets see how another class can access these public attributes of the above class

class CarInfo:
    def display_info(self, car: Car):
        print(f"Car Make: {car.make}, Car Model: {car.model}")
car_info = CarInfo()
car_info.display_info(car)  # Output: Car Make: Toyota, Car Model: Camry
# In the above code, the CarInfo class has a method display_info that takes an instance of the Car class as a parameter.
# It accesses the public attributes make and model of the Car instance to display the car information.

# Protected Attribute Real World Example:
class Employee:
    def __init__(self, name, salary):
        self._name = name          # Protected attribute
        self._salary = salary      # Protected attribute
employee = Employee("Alice", 50000)
print("Employee Name:", employee._name)      # Output: Employee Name: Alice
print("Employee Salary:", employee._salary)  # Output: Employee Salary: 50000
# In the above code, _name and _salary are protected attributes of the Employee class.
# They can be accessed directly from outside the class, but by convention, they should be treated as protected and not accessed directly.
# Lets see how a subclass can access these protected attributes of the above class
class Manager(Employee):
    def display_info(self):
        print(f"Manager Name: {self._name}, Manager Salary: {self._salary}")

manager = Manager("Bob", 60000)
manager.display_info()  # Output: Manager Name: Bob, Manager Salary: 60000
# In the above code, the Manager class inherits from the Employee class.
# It accesses the protected attributes _name and _salary of the Employee class to display the manager information.
# Lets see how protected attributes are possible to acccess by another class or not
class HR:
    def display_employee_info(self, employee: Employee):
        print(f"HR Access - Employee Name: {employee._name}, Employee Salary: {employee._salary}")

hr = HR()
hr.display_employee_info(employee)  # Output: HR Access - Employee Name: Alice, Employee Salary: 50000
# In the above code, the HR class has a method display_employee_info that takes an instance of the Employee class as a parameter.
# It accesses the protected attributes _name and _salary of the Employee instance to display the employee information.
# Although it is possible to access protected attributes from outside the class, it is generally discouraged as it goes against the convention of treating them as protected.


# Private Attribute Real World Example:
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance                  # Private attribute
account = BankAccount("123456", 1000)
# Trying to access private attributes directly will raise an AttributeError 
# print("Account Number:", account.__account_number)  # Raises AttributeError
# print("Balance:", account.__balance)                # Raises AttributeError   
# In the above code, __account_number and __balance are private attributes of the BankAccount class.
# They cannot be accessed directly from outside the class.
# Lets see how we can access these private attributes using getter and setter methods
class BankAccountWithAccessors:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance                  # Private attribute

    # Getter method for account_number
    def get_account_number(self):
        return self.__account_number

    # Setter method for account_number
    def set_account_number(self, account_number):
        self.__account_number = account_number

    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Setter method for balance
    def set_balance(self, balance):
        self.__balance = balance
account_with_accessors = BankAccountWithAccessors("654321", 2000)
print("Account Number:", account_with_accessors.get_account_number())  # Output: Account Number: 654321
print("Balance:", account_with_accessors.get_balance())                # Output: Balance: 2000
# In the above code, we define getter and setter methods to access and update the private attributes __account_number and __balance.
# This allows controlled access to the private attributes while still keeping them encapsulated within the class.
# When is it required to use getter and setter methods?
# Getter and setter methods are used when you want to control access to private attributes.

