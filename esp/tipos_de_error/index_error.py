"""
IndexError
Es una excepción que se produce cuando se intenta acceder a un índice inválido en una secuencia, 
como una lista o una cadena. Esto ocurre cuando se realiza una referencia a un índice que está fuera del 
rango de índices válidos para la secuencia en cuestión.
"""

## Ejemplo 1
lista = [1, 2, 3]

print(lista[0])  # Imprime 1
print(lista[2])  # Imprime 3

#print(lista[3])  # Genera un IndexError: list index out of range
# Descomenta y ejecuta para ver el error

## Ejemplo 2
cadena = "Hola"

print(cadena[0])  # Imprime 'H'
print(cadena[3])  # Imprime 'a'

#print(cadena[10])  # Genera un IndexError: string index out of range
# Descomenta y ejecuta para ver el error
