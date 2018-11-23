# Python is dynamic typed; unlike static typed languages like Java
name="jack"
mark=10
price=10.50

# conversion
print(float(mark))
print(int(price))
print(str(price))

# string is immutable
name="Jack Harry"

# String operations
print("hello".capitalize())
print("hello".replace("e","u"))
print("hello".isalpha())
print("hello".isdigit())
print("split this string".split(" "))

# String format
guest="Henry"
me ="Harry"
print("Welcome {0},I am {1}. How are you?".format(name,me))

# raw string
path=r'C:\Temp'
print(path)

# byte
data =b'some byte data'
print(data)
print(data.split())

# list
lstData = [1,"value",19]  # list with diff element type
lstData2 =[] # empty list
lstData2.append("check")

# boolean
python_course=True      # first letter needs to be in CAPS
java_course=False
print(int(python_course))
print(int(java_course))
print(str(python_course))

# none
alien_found=None

# if statement
number=5
if number == 5:
    print("Number is 5")
else:
    print("Number not 5")

# Truthy and Falsy value
number =10
count = None
if number:
    print("Number is truthy")
if count:
    print("Count is truthy")
else:
    print("Count is Falsy")

