"""
AtributeError
Es una excepción que se produce cuando se intenta acceder a un atributo o método inexistente en un objeto.
Esto ocurre cuando se realiza una referencia a un atributo o método que no ha sido definido previamente para el objeto en cuestión.
"""

## Ejemplo 1:
class MiClase:
    def __init__(self):
        self.atributo = "Hola"

objeto = MiClase()
print(objeto.atributo)  # Imprime "Hola"
#print(objeto.metodo)  # Genera un AttributeError: 'MiClase' object has no attribute 'metodo'
# Descomenta y ejecuta para ver el error

## Ejemplo 2:
cadena = "Hola, mundo!"
print(cadena.upper())  # Imprime "HOLA, MUNDO!"

#print(cadena.uppercase())  # Genera un AttributeError: 'str' object has no attribute 'uppercase'
# Descomenta y ejecuta para ver el error