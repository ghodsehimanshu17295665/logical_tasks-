class Rational:

    def __init__(self, nume=0, deno=1):
        self.nume = nume
        self.deno = deno

    def getValue(self):
        self.nume = int(input("Enter value for Numerator: "))
        self.deno = int(input("Enter value for Denominator: "))

    def add(self, value):
        tem = Rational()
        tem.deno = self.deno * value.deno
        tem.nume = self.nume * value.deno + value.nume * self.deno
        return tem

    def subtract(self, value):
        tem = Rational()
        tem.deno = self.deno * value.deno
        tem.nume = self.nume * value.deno - value.nume * self.deno
        return tem
    
    def multiply(self, value):
        tem = Rational()
        tem.nume = self.nume * value.nume
        tem.deno = self.deno * value.deno
        return tem
    
    def divide(self, value):
        tem = Rational()
        tem.nume = self.nume * value.deno
        tem.deno = self.deno * value.nume
        return tem

    def show(self, operator, value, result):
        print(
            f"{self.nume}/{self.deno} {operator} {value.nume}/{value.deno} = {result.nume}/{result.deno}"
        )


def operation_menu(rational_1, rational_2, operation):
    while True:
        print(
            """
            1] change Value
            2] calculate Rational Number
            3] exit
            """
        )
        choice = input("enter your choice: ")

        if choice == "1":
            rational_1.getValue()
            rational_2.getValue()
        elif choice == "2":
            if operation == "add":
                result = rational_1.add(rational_2)
            elif operation == "subtract":
                result = rational_1.subtract(rational_2)
            elif operation == "multiply":
                result = rational_1.multiply(rational_2)
            elif operation == "divide":
                result = rational_1.divide(rational_2)
            rational_1.show(operation, rational_2, result)
        elif choice == "3":
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please choose again.")


def main():
    rational_1 = Rational()
    rational_2 = Rational()
    while True:
        print(
            "\n1. Rational Addition\n2. Rational Subtraction\n3. Rational Multiplication\n4. Rational Division\n5. Exit"
        )
        choice = input("Choose an option: ")

        if choice == "1":
            operation_menu(rational_1, rational_2, "add")
        elif choice == "2":
            operation_menu(rational_1, rational_2, "subtract")
        elif choice == "3":
            operation_menu(rational_1, rational_2, "multiply")
        elif choice == "4":
            operation_menu(rational_1, rational_2, "divide")
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")


main()
