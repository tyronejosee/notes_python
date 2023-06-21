"""
The map() function in Python is a built-in function used to apply a function
to every element of one or more sequences (such as lists, tuples, or sets),
and it returns an iterator containing the results.
"""
numbers = [2, 4, 6, 8, 10]

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers))) # [4, 8, 12, 16, 20]

# Using a lambda function

print(list(map(lambda number: number * 2, numbers))) # [4, 8, 12, 16, 20]
