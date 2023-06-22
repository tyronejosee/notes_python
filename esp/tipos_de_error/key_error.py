"""
KeyError
Es una excepción que se produce cuando se intenta acceder a una clave que no existe en un diccionario. 
Esto ocurre cuando se realiza una referencia a una clave que no ha sido definida previamente en el diccionario.
"""

## Ejemplo 1
diccionario = {'a': 1, 'b': 2, 'c': 3}

print(diccionario['a'])  # Imprime 1
print(diccionario['b'])  # Imprime 2
#print(diccionario['d'])  # Genera un KeyError: 'd'
# Descomenta y ejecuta para ver el error

## Ejemplo 2
diccionario = {'a': 1, 'b': 2, 'c': 3}

clave = 'd'

if clave in diccionario:
    valor = diccionario[clave]
    print(valor)
else:
    print(f"La clave '{clave}' no existe en el diccionario")
