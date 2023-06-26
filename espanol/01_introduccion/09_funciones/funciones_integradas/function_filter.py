"""
The filter() function in Python is a built-in function used to filter elements from a sequence 
(such as a list, tuple, or set) based on a specified condition. 
It takes two parameters: a function and a sequence.
"""
numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def validate_number(number):
    if number > 10:
        return True
    return False

print(list(filter(validate_number, numbers))) # [12, 14, 16]

# Using a lambda function

print(list(filter(lambda number: number > 10, numbers))) # [12, 14, 16]
