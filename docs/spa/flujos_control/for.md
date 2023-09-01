# Bucles for

Python es un lenguaje de programación fuerte y universalmente aplicable diseñado para ser fácil de comprender y ejecutar. Es de acceso gratuito porque es de código abierto. En este tutorial, aprenderemos cómo usar los bucles "for" en Python, una de las instrucciones de bucle más fundamentales en la programación en Python.

## Introducción al Bucle "for"

Python utiliza frecuentemente el bucle "for" para iterar sobre objetos iterables como listas, tuplas y cadenas. El bucle "for" se utiliza cuando se necesita recorrer una serie de elementos, y se utiliza para repetir un fragmento de código un número determinado de veces. El bucle "for" suele aplicarse a un objeto iterable, como una lista o la capacidad incorporada de rango. En Python, la instrucción "for" ejecuta el bloque de código cada vez que atraviesa una serie de elementos. Por otro lado, el bucle "while" se utiliza cuando se necesita verificar una condición después de cada repetición, o cuando un fragmento de código debe repetirse indefinidamente. La instrucción "for" se opone a este tipo de bucle.

**Sintaxis**:

```python
for valor in secuencia:
    {cuerpo del bucle}
```

El valor es el parámetro que determina el valor del elemento dentro de la secuencia iterable en cada iteración. Cuando una secuencia contiene declaraciones de expresiones, estas se procesan primero. A continuación, se asigna el primer elemento de la secuencia a la variable de iteración "valor". A partir de ese momento, se ejecuta el bloque planificado. Cada elemento de la secuencia se asigna a "valor" durante el bloque de declaraciones hasta que se complete la secuencia en su totalidad. El contenido del bucle se distingue del resto del programa mediante la sangría.

**Ejemplo**:

```python
# Código para encontrar la suma de los cuadrados de cada elemento de la lista usando un bucle "for"

# creando una lista de números
numeros = [3, 5, 23, 6, 5, 1, 2, 9, 8]

# inicializando una variable que almacenará la suma
suma = 0

# usando un bucle "for" para iterar sobre la lista
for num in numeros:
    suma = suma + num ** 2

print("La suma de los cuadrados es:", suma)
```

**Salida**:

```python
La suma de los cuadrados es: 774
```

## La Función range()

Dado que la capacidad "range" aparece tan frecuentemente en los bucles "for", podríamos erróneamente pensar que "range" es parte de la sintaxis del bucle "for". No lo es: es un método incorporado en Python que cumple con el requisito de proporcionar una serie para que la expresión del bucle "for" se ejecute siguiendo un patrón específico (generalmente números enteros en serie). Principalmente, pueden actuar directamente sobre secuencias, por lo que el conteo no es necesario. Este es un constructo típico para principiantes si provienen de un lenguaje con una sintaxis de bucle distinta:

**Ejemplo**:

```python
mi_lista = [3, 5, 6, 8, 4]

for variable_de_iteracion in range(len(mi_lista)):
    mi_lista.append(mi_lista[variable_de_iteracion] + 2)

print(mi_lista)
```

**Salida**:

```python
[3, 5, 6, 8, 4, 5, 7, 8, 10, 6]
```

## Iterar Usando el Índice de una Secuencia

Otra forma de iterar a través de cada elemento es usar un desplazamiento de índice dentro de la secuencia. Aquí tienes una ilustración sencilla:

**Ejemplo**:

```python
# Código para encontrar la suma de los cuadrados de cada elemento de la lista usando un bucle "for"

# crear una lista de números
numeros = [3, 5, 23, 6, 5, 1, 2, 9, 8]

# inicializar una variable que almacenará la suma
suma_total = 0

# usar un bucle "for" para iterar sobre la lista
for num in range(len(numeros)):
    suma_total = suma_total + numeros[num] ** 2

print("La suma de los cuadrados es:", suma_total)
```

**Salida**:

```python
La suma de los cuadrados es: 774
```

La función len() se utilizó de manera que devuelve el número completo de elementos en la lista o tupla, y la capacidad implícita range(), que devuelve la secuencia específica sobre la que se enfoca, fue útil aquí.

## Uso de la Instrucción "else" con el bucle "for"

En Python, es posible combinar una expresión de bucle con una expresión "else".

La cláusula "else" se ejecuta después de que el bucle haya terminado de iterar sobre la lista.

El siguiente ejemplo demuestra cómo extraer las calificaciones de los estudiantes de un registro combinando una expresión "for" con una cláusula "else".

**Ejemplo**:

```python
# Código para imprimir las calificaciones de un estudiante desde el registro

nombre_estudiante_1 = 'Itika'
nombre_estudiante_2 = 'Parker'

# Creación de un diccionario con los registros de los estudiantes
registros = {'Itika': 90, 'Arshia': 92, 'Peter': 46}

def calificaciones(nombre_estudiante):
    for estudiante in registros:  # El bucle "for" iterará sobre las claves del diccionario
        if estudiante == nombre_estudiante:
            return registros[estudiante]
            break
    else:
        return f'No hay ningún estudiante con el nombre {nombre_estudiante} en los registros'

# Llamamos a la función calificaciones() con los nombres de dos estudiantes

print(f"Las calificaciones de {nombre_estudiante_1} son: ", calificaciones(nombre_estudiante_1))

print(f"Las calificaciones de {nombre_estudiante_2} son: ", calificaciones(nombre_estudiante_2))
```

**Salida**:

```python
Las calificaciones de Itika son:  90
Las calificaciones de Parker son:  No hay ningún estudiante con el nombre Parker en los registros
```

## Bucles Anidados

Si tenemos una parte de contenido que necesitamos ejecutar varias veces y, después, otra parte de contenido dentro de ese script que necesitamos ejecutar varias veces B, utilizamos un "bucle anidado". Python usa ampliamente esto al trabajar con iterables en las listas.

**Ejemplo**:

```python
import random

numeros = []

for val in range(0, 11):
    numeros.append(random.randint(0, 11))

for num in range(0, 11):
    for i in numeros:
        if num == i:
            print(num, end=" ")
```

**Salida:**

```python
0 2 4 5 6 7 8 8 9 10
```
