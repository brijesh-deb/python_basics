import copy

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

# String operations
values = ",".join(["One","Two","Three"])
print(values)                               # join string seperated by ","
print(values.split(","))                    # split string based on ","
print("".join(["New","York"]))              # concatenate string using join
print(len("check length"))                  # check length
print("unforgetable".partition("forget"))   # partition based on a value
pre,separator,post = "London:Britain".partition(":")
print(pre)
print(post)

# List operations
s ="show how to index into sequences".split()   # returns a list of string
print(s)
copy1 = s[:]            # copy list
print(s is copy1)
print(s == copy1)
copy1[0]="1111"
print(s)
print(copy1)
copy2 = s.copy()            # copy list
print(copy2)
copy2[0]="2222"
print(s)
print(copy2)

copy3 = list(s)
copy3[0]="3333"
print(s)
print(copy3)

# shallow copy
org = [[1,2,3],[4,5,6]]
copy1 = copy.copy(org)
copy1[0][1]=10
print(org)
print(copy1)

# deep copy
org = [[1,2,3],[4,5,6]]
copy1 = copy.deepcopy(org)
copy1[0][1]=10
print(org)
print(copy1)

# list operations
lst = "this is a python list object. Use this for testing".split()
print(lst.index("python"))          # index of an element
print(lst.count("this"))            # count of an element
print("this" in lst)
print("this" not in lst)
lst.remove("this")                  # remove an element
print(lst)
lst.insert(0,"Hi!")
print(lst)
