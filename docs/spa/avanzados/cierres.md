# Cierres

Un lenguaje como Python tiene abundantes conceptos interesantes que están destinados a facilitar el trabajo de los programadores.

En este tutorial, aprenderemos sobre los cierres en Python. Pero antes de eso, repasemos las funciones anidadas y veamos cómo pueden actuar como un requisito previo para comprender este tema.

## Programa 1

El programa que se muestra a continuación ilustra el concepto de funciones anidadas y variables no locales.

**Ejemplo**:

```python
# Función externa
def function_1(txt):
    # Función interna
    def function_2():
        print(txt)

    function_2()

function_1('Python en JavaTpoint')
```

**Salida**:

```bash
Python en JavaTpoint
```

**Explicación**:

Vamos a entender qué hemos hecho en este programa:

1. Hemos creado la función function_1 que toma el parámetro txt y dentro de esta función hemos creado otra función que imprime el valor de txt.
2. Como se puede ver, se llama a 'function_2' en el programa anterior y luego hemos pasado un valor de cadena en la función_1.
3. Al ejecutar este programa, se muestra la salida deseada.

## Programa 2

Ahora, veamos cómo los cierres pueden ayudar a simplificar nuestro trabajo y mejorar nuestro programa.

**Ejemplo**:

```python
# Función externa
def function_1(txt):
    # Función interna
    def function_2():
        print(txt)

    return function_2()

function_3 = function_1('Aprendamos un lenguaje de programación.')

function_3()
```

**Salida**:

```bash
Aprendamos un lenguaje de programación.
```

**Explicación**:

Vamos a entender qué hemos hecho en este programa:

1. Hemos creado la función function_1 que toma el parámetro txt y dentro de esta función hemos creado otra función que imprime el valor de txt.
2. Como se puede ver, el valor de 'function_2' se devuelve en el programa anterior y luego hemos pasado un valor de cadena en la función_1 y lo hemos asignado a function_3.
3. Al ejecutar este programa, se muestra la salida deseada.

**Observación**:

Basándonos en la observación anterior, podemos concluir que:

1. Con la ayuda de los cierres, podemos invocar funciones que están fuera del ámbito en Python.
2. Podemos decir que un cierre es un objeto de función que recuerda los valores presentes en el ámbito cerrado.
3. Es un registro en el que cada variable de una función se asigna con el valor o la referencia al nombre cuando se creó el cierre.
4. Actúa como una ayuda para obtener o acceder a las variables con la ayuda de copias de cierre.

**Cuándo Podemos Usar un Cierre**:

Podemos usar un cierre en las siguientes condiciones:

1. Un programa debe tener una función anidada.
2. La función debe hacer referencia a un valor en la función encerrada.
3. La función encerradora debe devolver la función anidada.

**Algunas Características Adicionales**:

Las características de los cierres son:

1. Los cierres proporcionan una especie de ocultación de datos en nuestro programa, por lo que podemos evitar el uso de variables globales.
2. Es una opción eficiente cuando no tenemos demasiadas funciones en nuestro programa.

## Programa 3

Finalmente, echemos un vistazo a otro programa interesante que utiliza un cierre. El programa muestra la situación en la que podemos usar un cierre en lugar de una clase.

**Ejemplo**:

```python
def add_num(n):
    def addition(x):
        return x + n

    return addition

add_2 = add_num(2)
add_8 = add_num(8)

print(add_2(4))
print(add_2(8))
print(add_8(add_2(7)))
```

**Salida**:

```bash
6
10
17
```

**Explicación**:

Vamos a entender qué hemos hecho en el programa anterior:

1. La función que hemos creado es add_num y dentro de ella hay otra función llamada addition.
2. Esta función debe devolver el valor x + n.
3. En el siguiente conjunto de declaraciones, hemos utilizado diferentes formas de sumar dos números.
4. Al ejecutar el programa, se muestra el resultado requerido.
