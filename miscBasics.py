# import statements
import math
from math import factorial          # import specific function from math module
from math import factorial as fac

# elif block
no=42
if no>50:
    print("Greater than 50")
elif no<20:
    print("Less than 20")
else:
    print("Between 20 to 50")

# working with loops
students = ["jack", "jill", "herry", "poter"]
for name in students:
    print("Student name is {0}".format(name))

# get user input
# username = input("Enter name: ")
# print(username)

# object identifier
a=10
print(id(a))
b=15
print(id(b))
b=a
print(id(b))

# Type and Attributes of an object
print(type(a))  # get type of an object including function, module etc
print(dir(a))   # get attributes of an object
