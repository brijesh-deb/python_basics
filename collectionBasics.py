# tuple is a heterogeneous immutable sequence of arbitrary objects; cannt be changed
# can contain any object like nested tuple
t = ("Norway",4.55,10)
print(t)

# tuple operations
print(t[0])                 # access an element
print(len(t))               # length
print(t*3)                  # repetation
print(t + ("check",166))    # concatination

# single element and empty tuple
k=(100)
print(type(k))      # not a tuple
n=(100,)
print(type(n))      # Is a tuple
m=()
print(type(m))      # Is a tuple

# parenthesis can be emitted
p = 1,1,3,2,5
print(type(p))

# tuple can be used for multiple return values
def getMinMax(items):
    return min(items), max(items)
print(getMinMax([56,67,41,14,89,7,189]))

# tuple unpacking allows to destructure directly into named references
min,max =getMinMax([56,67,41,14,89,7,189])
print(min)
print(max)

# swappin using tuple
a="first"
b="second"
a,b = b,a
print(a)
print(b)

print(5 in (3,5,17,88,9))
print(5 not in (3,5,17,88,9))

# Join/Split str
values = ",".join(["One","Two","Three"])
print(values)
print(values.split(","))
print("".join(["New","York"]))