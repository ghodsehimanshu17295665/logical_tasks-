# object  oriented programming:- Class & Object :-


class Person:

    # class Variable
    company_name = "ABC Company"

    # constructor:-
    def __init__(self, name, age, profession):
        # data member(intance variable)
        self.name = name
        self.age = age
        self.profession = profession

    # Behavior (instance methods)
    def show(self):
        print(
            "Name:",
            self.name,
            "Age:",
            self.age,
            "Profession:",
            self.profession,
        )

    # Behavior (instance methods)
    def work(self):
        print(self.name, "working as a", self.profession)


# create object of a class
ram = Person("Ram", 25, "Software Engineer")

# call Method:-
ram.show()
ram.work()

# access class variable
print("Company name:", Person.company_name)

# call object value:-
print(ram.name)
print(ram.age)
print(ram.profession)
