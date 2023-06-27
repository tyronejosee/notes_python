"""
Decoradores
"""

### Asignar funciones a variables
def plus_one(number):
    return number + 1

add_one = plus_one
add_one(5)

### Definición de funciones dentro de otras funciones
def plus_one(number):
    def add_one(number):
        return number + 1


    result = add_one(number)
    return result
plus_one(4)

### Pasando funciones como argumentos a otras funciones
def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)

### Funciones que devuelven otras funciones.
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
hello()

### Las funciones anidadas tienen acceso al ámbito de variables de la función contenedora
def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message")

### Creando decoradores
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper