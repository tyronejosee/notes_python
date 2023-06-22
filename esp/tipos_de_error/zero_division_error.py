"""
ZeroDivisionError
Es una excepción que se produce cuando se intenta dividir un número entre cero. 
Esto ocurre cuando se realiza una operación de división y el divisor es igual a cero, 
lo cual es una operación indefinida en matemáticas.
"""

## Ejemplo 1
#resultado = 10 / 0  # Genera un ZeroDivisionError: division by zero
# Descomenta y ejecuta para ver el error

## Ejemplo 2
numero = 0

if numero != 0:
    resultado = 10 / numero
    print("El resultado de la división es:", resultado)
else:
    print("No se puede realizar la división, el divisor es cero.")
