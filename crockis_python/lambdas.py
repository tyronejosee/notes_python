"""
Este codigo es base de contenido visto en el curso de mauro dev
esta vez trato las lambdas y como estas funcionan
una era una creacion simple y otro ejemplo dentro de una función
"""

### Lambdas ###

pruebas = lambda a, b: a+b


def funcion_de_prueba(valor_uno: str, valor_dos: str):
    """
    esta funcion acepta dos parametros y suma la lambda anterior
    retorna resultado
    """
    print(f"Tus valores son {valor_uno} y {valor_dos} que deseas realizar? ")
    resultado = valor_uno + valor_dos + pruebas
    print(f"El resultado de tu suma es {resultado}")
    return resultado

funcion_de_prueba(2, 3)
