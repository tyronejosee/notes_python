"""
define filter
"""
numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def validate_number(number):
    if number > 10:
        return True
    return False

print(list(filter(validate_number, numbers))) # [12, 14, 16]

# Usando una función lambda

print(list(filter(lambda number: number > 10, numbers))) # [12, 14, 16]
