# Dictionary Comprehension:-

# 1. Dictionary of Cubes:
cubes = {data: data**3 for data in range(1, 6)}
print(cubes)

# 2. Given a dictionary of numbers and their squares,
# create a dictionary comprehension to filter out the odd numbers.

square = {number: number**2 for number in range(1, 11)}
print(square)
odd_number = {key: value for key, value in square.items() if key % 2 != 0}
print(odd_number)

# 3. Given a dictionary with names as keys and ages as values,
# create a dictionary comprehension to transform the dictionary by adding 5 to each age.
ages = {"Alice": 25, "Bob": 30, "Charlie": 35}
print(ages)
new_age = {name: age + 5 for name, age in ages.items()}
print(new_age)

# 4. Given a list of words,
# create a dictionary comprehension where the keys are the words and the values are their lengths.

words = ["apple", "banana", "cherry"]
words_length = {word: len(word) for word in words}
print(words_length)

# 5.Given a string, create a dictionary comprehension to count the occurrences of each character.
text = "hello world"
char_count = {char: text.count(char) for char in text}
print(char_count)
