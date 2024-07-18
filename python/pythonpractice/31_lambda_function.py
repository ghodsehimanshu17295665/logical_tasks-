#  lambda() function

# example of a lambda function that adds 10 to a number:
def my_fun():
    return lambda number: number + 10

add_ten = my_fun(10)
print(add_ten)


# multiply :-
multiply = lambda num1, num2: num1 * num2
print(multiply(10, 3))


# Convert List of Integers to Their Squares
list1 = [10, 20, 30, 40, 50]
square = list(map(lambda data: data ** 2, list1))
print(square)
