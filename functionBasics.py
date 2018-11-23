students = ["jack", "jill", "herry", "poter"]


# working with functions
def get_student_titlecase():
    """
    Fetch capitalizrd student name
    :return:
    """
    student_titlecase = []
    for student in students:
        student_titlecase.append(student.title())
    return student_titlecase  # return from function


print(get_student_titlecase())

# blank return statements returns None
def no_return():
    return


print(no_return())

# arguments in function
def add_student(name, student_id=10):  # student_id has a default value 10
    student_detail = {"name": name, "student_id": student_id}  # dictionary data type
    students.append(student_detail)
    return students


print(add_student("henry")) # without argument student_id,takes default value
print(add_student("marlin",15)) # with argument student_id


# variable number of arguments
def var_args(name,*args):
    print(name,args)


var_args("john",15,None,"check")


# key word arguments
def var_kwargs(name,**kwargs):
    print(name)
    print(kwargs)   # print whole kwargs
    print(kwargs["address"])    # print a specific element of kwargs based on key


var_kwargs("john",address="abc",feedback=None,amount=100)


# nested function
def get_employees():
    employees = ["employee1","employee2"]
    def get_employees_title():
        employee_title=[]
        for employee in employees:                  # inner function can access variables in outer function; called closure
            employee_title.append(employee.title())
        return employee_title
    print(get_employees_title())

get_employees()


# save data in file
def save_file(student):
    try:
        f=open("student.txt","a")
        f.write(student+"\n")
        f.close()
    except Exception:   # exception handling
        print("Could not write in file")


# read data from file
def read_file():
    try:
        f=open("student.txt","r")
        for student in f.readline():
            print(student)
        f.close()
    except Exception:
        print("Could not read file")


save_file("jack")
save_file("jill")
read_file()