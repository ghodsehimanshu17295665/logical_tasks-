def sum_odd_even_digits(n):
    """Return the sum of odd and even digits of a multi-digit number in a dictionary."""
    sum_odd = 0
    sum_even = 0

    for digit in str(n):
        digit = int(digit)
        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit

    return {"odd_sum": sum_odd, "even_sum": sum_even}


# Example usage:
print(sum_odd_even_digits(12345))  # ➞ {'odd_sum': 9, 'even_sum': 6}
print(sum_odd_even_digits(2468))  # ➞ {'odd_sum': 0, 'even_sum': 20}
print(sum_odd_even_digits(13579))  # ➞ {'odd_sum': 25, 'even_sum': 0}
print(sum_odd_even_digits(112233))  # ➞ {'odd_sum': 6, 'even_sum': 6}
