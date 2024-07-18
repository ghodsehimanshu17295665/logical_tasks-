# Access Modifiers in Python:- Public, Private, Protected

# Private Member:-
print("private member---------")


class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private data member
        self.__salary = salary

    # public instance method:-
    def show(self):
        # private members are accessible from a class
        print("Name:", self.name, "Salary:", self.__salary)


# creating object of a class :-
obj1 = Employee("Jessa", 10000)


# accessing private data members
# print('Salary:', obj1.__salary) #AttributeError: 'Employee' object has no attribute '__salary'

# Access Private member outside of a class using an instance method
obj1.show()  # calling public method of the class.

# Name Mangling to access private members :-
print(
    "Salary:", obj1._Employee__salary
)  # direct access to private member using name mangling


# Protected Member:-
print("protected member ----------------")


# base class
class Company:
    # constructor
    def __init__(self):
        # Protected member
        self._project = "NLP"


# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)


obj2 = Employee("Jessa")
obj2.show()
# Direct access protected data member
print("Project:", obj2._project)
