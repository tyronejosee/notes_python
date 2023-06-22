"""
ImportError
es una excepción que se produce cuando hay problemas para importar un módulo o paquete. 
Esto puede suceder por varias razones, como un nombre incorrecto del módulo, 
una ubicación incorrecta del archivo, dependencias faltantes o incompatibilidades entre versiones.
"""

## Ejemplo 1
try:
    import modulo_inexistente
except ImportError:
    print("No se pudo importar el módulo")

## Ejemplo 2
try:
    from modulo import mi_funcion
except ImportError:
    print("No se pudo importar la función")
