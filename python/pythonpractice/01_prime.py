def filter_primes(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes


# Example usage:
print(filter_primes([7, 9, 3, 9, 10, 11, 27]))  # ➞ [7, 3, 11]
print(
    filter_primes(
        [1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]
    )
)
# [1009, 3, 61, 1087, 1091, 1093, 1097]