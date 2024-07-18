# Create a base class Employee with a method work. Subclass it to create Manager and Developer classes, each overriding the work method. 
# Write a function assign_work that takes an Employee object and calls its work method.

class Employee:
    def work(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Manager(Employee):
    def work(self):
        print("Manager is Working")


class Developer(Employee):
    def work(self):
        print("Developer is coding")


def assign_work(employee):
    employee.work()


manager = Manager()


developer = Developer()

assign_work(manager)  # Outputs: Manager is working
assign_work(developer)  # Outputs: Developer is coding
