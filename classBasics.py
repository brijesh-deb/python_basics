students = []


# self refers to instance of a class
# class definition
class Student:
    """
    This is a multiline comment
    Bla bla
    """

    school_name="Holycross school"          # class variable;doesnt change with instance

    def __init__(self, name, student_id):   # constructor
        self.name = name                    # instance variable
        self.student_id=student_id          # instance variable
        students.append(self)

    def __str__(self):
        return 'Student '+self.name

    def get_name_capitalized(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


# create a class using inheritance
class HighSchoolStudent(Student):           # Student is Parent class; HighSchoolStudent is derived

    school_name = "Holycross High School"   # Override

    def get_school_name(self):              # Override function
        return "This is high school student"

    def get_name_capitalized(self):
        return super().get_name_capitalized()+ "-HS"    # use super() to call method in parent class

# create an instance of Student class
jessy = Student("jessy", 10)
print(jessy)
print(jessy.get_name_capitalized())
print(jessy.get_school_name())

print(Student.school_name)                  # access class attribute directly

# create an instance of derived class HighSchoolStudent
mark = HighSchoolStudent("Mark",20)
print(mark.get_school_name())
print(mark.get_name_capitalized())