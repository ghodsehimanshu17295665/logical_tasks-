# Class Methods:-
# 1.Instance Method  2.Class Method  3.Static Method


# 1.Instance Method:-
class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print("Name:", self.name, "Age:", self.age)


# create first object
print("First Student")
obj1 = Student("Jessa", 14)
# call instance method
obj1.show()

# create second object
print("Second Student")
obj2 = Student("Kelly", 16)
# call instance method
obj2.show()


# 2.Class Method :-
# Access Class Variables in Class Methods:-
class Student:
    # Class variable:-
    school_name = "ABC School"

    # Constructor to initilize instance variable
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    @classmethod  # class Method:-
    def change_school(cls, school_name):
        # class_name.class_variable
        cls.school_name = school_name

    # instance Method:-
    def show(self):
        print(self.name, self.age, "School: ", Student.school_name)


# create  object:-
jessa = Student("Jessa", 20)
jessa.show()

# change school_name
Student.change_school("XYZ School")
jessa.show()


# 3.Static Method:-
class Employee:
    @staticmethod  # static Method
    def sample(x):
        print("Inside static method", x)


# call static method
Employee.sample(10)

# can be called using object
emp = Employee()
emp.sample(10)
