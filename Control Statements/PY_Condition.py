"""
if condition:
    statements
else:
    statements
"""

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")



"""
if condition1:
    statements
elif condition2:
    statements
else:
    statements
"""

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")



"""
Nested if-else statements
if condition1:
    if condition2:
        statements
    else:
        statements
else:
    statements
"""

num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")    


"""
Ternary Operator
variable = value_if_true if condition else value_if_false
"""
age = int(input("Enter your age: "))
status = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(status)

"""
Match-Case Statement (Python 3.10+)
match variable:
    case value1:
        statements
    case value2:
        statements
    case _:
        statements
"""

day = input("Enter a day of the week: ").lower()
match day:
    case "monday":
        print("It's the start of the work week.")
    case "wednesday":
        print("It's the middle of the work week.")



# Example 2: Truthy vs Falsy Values in python
# In Python, the following values are considered "falsy":
# - None
# - False
# - 0, 0.0, 0j, 0e-4 (zero of any numeric type)
# - "" (empty string)
# - [] (empty list)
# - {} (empty dictionary)


# All other values are considered "truthy".


li = [2e-04, 'a', False, 87] 
tup = (6.22, 'boy', True, 554) 
for i in range(len(li)): 
    if li[i]: 
        li[i] = li[i] + tup[i] 
    else: 
        tup[i] = li[i] + li[i] 
        break


# for index 0: li[0] is 0.0002 (truthy), so li[0] = 0.0002 + 6.22 = 6.2202
# for index 1: li[1] is 'a' (truthy), so li[1] = 'a' + 'boy = 'aboy'
# for index 2: li[2] is False (falsy), so tup[2] = False + False = 0 and the loop breaks    
# When a falsy value (False) is found at index 2, 
# it tries to modify tup, which causes an error because tuples are immutable.