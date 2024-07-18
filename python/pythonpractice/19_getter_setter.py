# Getters and Setters in Python


class student:
    def __init__(self, name, age):
        # private member
        self.name = name
        self.__age = age

    # getter method:
    def get_age(self):
        return self.__age

    # setter method:
    def set_age(self, age):
        self.__age = age


stud = student("Shiv", 20)

# retrieving age using getter
print("Name:", stud.name, stud.get_age())

# Changing are using setter
stud.set_age(23)
# retrieving age using getter
print("Name:", stud.name, stud.get_age())
