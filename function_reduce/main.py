


from functools import reduce

# Definimos una lista de números
numeros = [1, 2, 3, 4, 5]

# Utilizamos reduce para obtener la suma de los números
suma = reduce(lambda x, y: x + y, numeros)

print(suma)  # Salida: 15