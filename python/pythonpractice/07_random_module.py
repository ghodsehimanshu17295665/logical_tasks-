import random

# Seed the random number generator for reproducibility

# Generate random numbers
print("Random float between 0 and 1:", random.random())
print("Random float between 1.5 and 3.5:", random.uniform(1.5, 3.5))
print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random integer between 1 and 9:", random.randrange(1, 10))

# Random choice and shuffle
fruits = ["apple", "banana", "cherry", "date"]
print("Random fruit:", random.choice(fruits))
print("Random sample of 2 fruits:", random.sample(fruits, 2))

random.shuffle(fruits)
print("Shuffled fruits:", fruits)
