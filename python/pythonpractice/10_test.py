def is_prime(number):
    """Function to check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def is_armstrong(number):
    """Function to check if a number is an Armstrong number."""
    num_str = len(str(number))
    temp = number
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit**num_str
        temp = temp // 10
    # Check if the total is equal to the original number
    return sum == number


def cyclic(number):
    """Function to calculate the cyclic sum of digits of a number."""
    while number > 9:
        number = sum(int(digit) for digit in str(number))
    return number


def sum_of_digits(number):
    """Function to calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(number))


# Main program
while True:
    print(
        """
    1] check prime
    2] check armstrong number
    3] cyclic sum
    4] sum of digits
    5] exit
    """
    )
    choice = input("enter your choice: ")

    if choice == "1":
        number = int(input("enter a number: "))
        if is_prime(number):
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")

    elif choice == "2":
        number = int(input("enter a number: "))
        if is_armstrong(number):
            print(f"{number} is an Armstrong number")
        else:
            print(f"{number} is not an Armstrong number")

    elif choice == "3":
        number = int(input("enter a number: "))
        cyclic_sum_result = cyclic(number)
        print(f"Cyclic sum of digits of {number} is: {cyclic_sum_result}")

    elif choice == "4":
        number = int(input("enter a number: "))
        sum_of_digits_result = sum_of_digits(number)
        print(f"Sum of digits of {number} is: {sum_of_digits_result}")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
