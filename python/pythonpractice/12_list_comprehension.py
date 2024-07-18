# List Comprehension :-

# 1. Creating a list of squares for numbers from 0 to 9.
squares = [data**2 for data in range(10)]
print(squares)

# 2. Creating a list of even numbers from 0 to 9.
even_number = [data for data in range(10) if data % 2 == 0]
print(even_number)

# 3. Creating a list of the lengths of each word in a list.
words = ["hello", "world", "python", "list", "comprehension"]
length = [len(word) for word in words]
print(length)

# 4. Given two lists, generate a list comprehension that finds the common elements between them.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_ele = [x for x in list1 if x in list2]
print(common_ele)

"""
5. Write a list comprehension that converts
      all the strings in a list to uppercase.
"""
words = ["hello", "world", "python"]
uppercase_word = [word.upper() for word in words]
print(uppercase_word)


# 6. Write a list comprehension that generates a list of prime numbers between 2 and 50.
def is_prime(number):
    if number < 2:
        return False
    for data in range(2, number):
        if number % data == 0:
            return False
    return True


primes = [number for number in range(2, 51) if is_prime(number)]
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
