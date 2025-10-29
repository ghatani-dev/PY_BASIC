"""
Global and Local Variables in Python
This script demonstrates the use of global and local variables in Python.
In python unlike some other programming languages we don't have to explicitly declare data types like int, float, string etc.
data types are declared when they are first assigned a value.
"""

# Global variable
global_var = "I am a global variable" # This variable is accessible throughout the script, and its of type string

def my_function():
    """Global and Local Variables in Python

    This script demonstrates the Python variable model with inline annotations.

    Key conceptual points (CPython implementation details):
    - In Python, names (variables) are references that point to objects.
    - Most objects (integers, strings, lists, dicts, user-defined objects) are heap-allocated
      in CPython. The actual object data lives on the heap; names in local/global scopes
      reference those objects.
    - A function call creates a frame (on the C call stack) that holds local name->object
      references. When references drop to zero, CPython normally reclaims objects using
      reference counting; a cyclical GC also runs to clean cycles.
    - Mutability matters: assignment binds a name to a (possibly new) object; mutating a
      mutable object (like a list) changes the same heap object that other names may
      reference.

    This file contains small examples and comments that illustrate these ideas.
    """

    # Global variable: the name `global_var` is bound to a str object (on the heap).
    global_var = "I am a global variable"

    def my_function():
        # Local variable: `local_var` is a name in the function frame bound to a str object.
        local_var = "I am a local variable"
        print(local_var)      # prints the string object referenced by local_var
        print(global_var)     # the function can read the global name; it references the global str


    my_function()

    # Trying to access the local variable outside its scope will raise a NameError
    # print(local_var)  # Uncommenting this line will cause a NameError: name 'local_var' is not defined


    # Accessing the global variable outside the function works because the module-level
    # name `global_var` is available in the module's global namespace.
    print(global_var)


    # Modifying a global variable inside a function
    def modify_global():
        # The `global` statement tells Python that assignments to global_var inside this
        # function should rebind the module-level name, not create a new local name.
        global global_var
        # This assignment rebinds the module-level name `global_var` to a new str object.
        global_var = "I have been modified"
        print("inside modify_global, global_var id:", id(global_var))


    modify_global()
    print("after modify_global, global_var id:", id(global_var))  # shows the new object id


    # Demonstrating local variable scope
    def another_function():
        local_var = "I am another local variable"
        print(local_var)


    another_function()
    # print(local_var)  # Uncommenting this line will cause a NameError


    # ---- Mutable vs Immutable demonstration ----
    # In Python assignment always binds a name to an object. Mutability determines whether
    # you can change the object's contents through a reference.

    print('\n-- Mutable vs Immutable demo --')

    # Immutable example (int): rebinding inside a function doesn't change caller's name.
    num = 10
    print('num before rebind, id:', id(num), 'value:', num)
    # Here id(num) gives the memory address of the int object 10
    # o/p:  num before rebind, id:  139393286063080 value:  10

    def rebind_number(x):
        # x is a new local name bound to the same int object initially
        print('  inside rebind_number before:', id(x), x)
        # o/p:  inside rebind_number before:  139393286063080 10
        x = x + 5  # creates a new int object and rebinds local name x to it
        print('  inside rebind_number after :', id(x), x)
        # o/p:  inside rebind_number after :  139393286063112 15


    rebind_number(num)
    print('num after rebind_number, id:', id(num), 'value:', num)
    # o/p:  num after rebind_number, id:  139393286063080 value:  10

    # Hence from the above we see that rebinding x inside rebind_number does not affect num, 
    # because integers are immutable and x was rebound to a new int object.
    # Therefore, the original num remains unchanged.


    # Mutable example (list): mutating the object affects all names referencing it.
    lst = [1, 2, 3]
    print('\nlst before mutate, id:', id(lst), 'value:', lst)
    # o/p:  lst before mutate, id:  139393285994688 value:  [1, 2, 3]

    def mutate_list(a_list):
        # a_list references the same list object; append mutates that object in-place
        print('  inside mutate_list before, id:', id(a_list), 'value:', a_list)
        # o/p:  inside mutate_list before, id:  139393285994688 value:  [1, 2, 3]
        a_list.append(4)
        print('  inside mutate_list after, id:', id(a_list), 'value:', a_list)
        # o/p:  inside mutate_list after, id:  139393285994688 value:  [1, 2, 3, 4]


    mutate_list(lst)
    print('lst after mutate_list, id:', id(lst), 'value:', lst)
    # o/p:  lst after mutate_list, id:  139393285994688 value:  [1, 2, 3, 4]

    # Hence from the above we see that mutating the list inside mutate_list affects lst,
    # because lists are mutable and both a_list and lst reference the same list object.
    


    # Summary:
    # - Names -> objects. In CPython objects live on the heap; names in scopes point to them.
    # - Assignment rebinds names to objects; it does not "copy" values like C value-types.
    # - Mutability (list/dict/set vs int/str/tuple) determines whether in-place changes are
    #   visible through other references.
    # - Use `global` to rebind a module-level name from inside a function (rarely needed).
