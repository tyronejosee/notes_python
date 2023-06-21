"""
Uso de la función integrada map, creando una lista y pasandole una función
"""
numbers = [2, 4, 6, 8, 10]

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))

# Usando una función lambda
print(list(map(lambda number: number * 2, numbers)))
