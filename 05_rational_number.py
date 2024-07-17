class RationalAdd:

    def __init__(self, p=0, q=1):
        self.p = p
        self.q = q

    def getValue(self):
        self.p = int(input("Enter value for Numerator: "))
        self.q = int(input("Enter value for Denominator: "))

    def calculate(self, value):
        temp = RationalAdd()

        if type(self) == type(value):
            temp.q = self.q * value.q
            temp.p = self.p * value.q + value.q * self.p

            return temp

    def show(self, value, temp):
        print(
            f"{self.p} / {self.q} + {value.p} / {value.q} = {temp.p} / {temp.q}"
        )


ob1 = RationalAdd(3, 5)
ob2 = RationalAdd(4, 7)
result = RationalAdd()
result = ob1.calculate(ob2)
ob1.show(ob2, result)
