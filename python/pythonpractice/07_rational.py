class RationalAdd:

    def __init__(self, p=0, q=1):
        self.p = p
        self.q = q

    def getValue(self):
        self.p = int(input("Enter value for Numerator: "))
        self.q = int(input("Enter value for Denominator: "))

    def calculate(self, value):
        if type(self) is type(value):
            temp = RationalAdd()
            temp.q = self.q * value.q
            temp.p = self.p * value.q + value.p * self.q
            return temp

    def show(self, value, temp):
        print(
            f"{self.p} / {self.q} + {value.p} / {value.q} = {temp.p} / {temp.q}"
        )


def main():
    ob1 = RationalAdd()
    ob2 = RationalAdd()

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
