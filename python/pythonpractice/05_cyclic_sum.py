#Create a function that will take a multi-digit number and return the cyclic sum of that number.
#Cyclic Sum : input: 12345  = 1+2+3+4+5 = 15 (which is still multi-digit) so 1+5 = 6 (output)

number = int(input("Enter Number:- "))


def cyclic(number):
    while number > 9:
        number = sum(int(digit) for digit in str(number))
    return number


print(cyclic(number))

# Example usage:
# cyclic_sum(12345)) ➞ 6
# cyclic_sum(9876))  ➞ 3
# cyclic_sum(4444))  ➞ 7