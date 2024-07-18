class RationalSub:

    def __init__(self, nume=0, deno=1):
        self.nume = nume
        self.deno = deno

    def getValue(self):
        self.nume = int(input("Enter value for Numerator: "))
        self.deno = int(input("Enter value for Denominator: "))

    def calculate(self, value):
        if type(self) is type(value):
            temp = RationalSub()
            temp.deno = self.deno * value.deno
            temp.nume = self.nume * value.deno - value.nume * self.deno
            return temp

    def show(self, value, temp):
        print(
            f"{self.nume} / {self.deno} - {value.nume} / {value.deno} = {temp.nume} / {temp.deno}"
        )


def main():
    ob1 = RationalSub()
    ob2 = RationalSub()

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
            ob1.getValue()
            ob2.getValue()
        elif choice == "2":
            result = ob1.calculate(ob2)
            ob1.show(ob2, result)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


main()
