def is_armstrong(n):
    s = len(str(n))
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit**s
        temp = temp // 10
    # Check if the total is equal to the original number
    return sum == n


# Example usage:
print(is_armstrong(153))  # ➞ True
print(is_armstrong(9474))  # ➞ True
print(is_armstrong(9475))  # ➞ False


def find_first_n_armstrong_numbers(n):
    """Find the first n Armstrong numbers."""
    armstrong_numbers = []
    num = 0
    while len(armstrong_numbers) < n:
        if is_armstrong(num):
            armstrong_numbers.append(num)
        num += 1
    return armstrong_numbers


# Find the first 10 Armstrong numbers
first_10_armstrong_numbers = find_first_n_armstrong_numbers(11)
print(first_10_armstrong_numbers)  #  ➞ [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153]
