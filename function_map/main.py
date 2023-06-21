"""
Uso de la función integrada map, creando una lista y pasandole una función
"""
numbers = [2, 4, 6, 8, 10]

def multiply_two(number):
    # Retorna el número y lo multiplica por 2
    return number * 2

print(list(map(multiply_two, numbers)))
