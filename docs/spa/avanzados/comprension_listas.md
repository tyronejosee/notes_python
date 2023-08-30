# Comprensión de Listas

En este tutorial, estamos discutiendo la comprensión de listas en Python. Python es conocido por ayudarnos a producir código elegante, simple de escribir y que se lee casi como inglés. La comprensión de listas es una de las características más distintivas del lenguaje, lo que nos permite desarrollar funcionalidades sofisticadas con solo una línea de código. Por otro lado, muchos programadores de Python luchan por utilizar completamente los aspectos más complejos de la comprensión de listas. A veces, los programadores pueden abusar de ellas, lo que resulta en código menos eficiente y difícil de leer.

**Ejemplo**:

Aquí presentamos un ejemplo básico de comprensión de listas en Python. El código es el siguiente:

```python
Person = ["Piyali", "Hiya", "Rudrashish", "Badsha", "Lipi"]

newlist = [x for x in Person if "i" in x]

print(newlist)
```

**Salida**:

Ahora compilamos el código anterior en Python y, después de una compilación exitosa, lo ejecutamos. Entonces, la salida es la siguiente:

```bash
['Piyali', 'Hiya', 'Rudrashish', 'Lipi']
```

**Sintaxis**:

La sintaxis de la comprensión de listas en Python es la siguiente:

```python
newlist = [expresion for elemento in iterable if condicion == True]
```

Aquí mostramos el uso básico de la comprensión de listas.

**Ejemplo**:

Ahora presentamos ejemplos de código sin utilizar comprensión de listas; ¿cómo podemos elevar al cuadrado cada número de una lista utilizando solo un bucle `for` en Python? El código es el siguiente:

```python
# Usando un bucle `for` para iterar a través de los elementos en la lista
numbers = [3, 5, 1, 7, 3, 9]
num = []

for n in numbers:
    num.append(n**2)

print(num)
```

**Salida**:

Ahora compilamos el código anterior en Python y, después de una compilación exitosa, lo ejecutamos. Entonces, la salida es la siguiente:

```bash
[9, 25, 1, 49, 9, 81]
```

Esto se puede lograr con una sola línea de código utilizando la comprensión de listas.

**Ejemplo**:

Ahora presentamos ejemplos de código de comprensión de listas en Python para elevar al cuadrado cada número de una lista. El código es el siguiente:

```python
# Usando la comprensión de listas para iterar a través de los elementos de la lista
numbers = [3, 5, 1, 7, 3, 9]
num = [n**2 for n in numbers]

print(num)
```

**Salida**:

Ahora compilamos el código anterior en Python y, después de una compilación exitosa, lo ejecutamos. Entonces, la salida es la siguiente:

```bash
[9, 25, 1, 49, 9, 81]
```

## Ventajas de utilizar la comprensión de listas

Hay muchas ventajas o beneficios de utilizar la comprensión de listas en Python. Las ventajas son las siguientes:

**1. Loops y maps**:

Los bucles y los mapas se consideran típicamente más "Pythonic" que la comprensión de listas. Pero en lugar de aceptar esa opinión como verdad absoluta, vale la pena considerar las ventajas de utilizar la comprensión de listas en Python en comparación con las alternativas. Aprenderemos sobre un par de casos en los que las alternativas son opciones preferibles más adelante.

**2. Una sola herramienta para múltiples usos**:

Una de las ventajas esenciales de utilizar la comprensión de listas en Python es que es una sola herramienta que se puede utilizar en diversas situaciones. No necesitamos adoptar un enfoque nuevo para cada caso. La comprensión de listas se puede aprovechar tanto para el mapeo o filtrado como para la generación básica de listas.

**3. No depende de parámetros apropiados**:

La comprensión de listas se considera "Pythonic", ya que Python enfatiza herramientas simples y efectivas que se pueden utilizar en muchas situaciones. Como beneficio adicional, no tendremos que recordar el orden adecuado de los parámetros al usar la comprensión de listas en Python, como lo haríamos al llamar a `map()`.

**4. Fácil de usar**:

La comprensión de listas es más fácil de leer y entender que los bucles, ya que es más declarativa. Con los bucles, debemos centrarnos en cómo se construye exactamente la lista. Debemos crear manualmente una lista vacía, iterar sobre las entradas de la lista y agregar cada una al final de la lista. En cambio, al utilizar la comprensión de listas en Python, podemos centrarnos en lo que queremos poner en la lista y permitir que Python maneje la generación de la lista.

**Ejemplo**:

```python
# Importar el módulo para hacer un seguimiento del tiempo
import time

# Definir la función para ejecutar un bucle `for`
def for_loop(num):
    l = []
    for i in range(num):
        l.append(i + 10)
    return l

# Definir la función para ejecutar la comprensión de listas
def list_comprehension(num):
    return [i + 10 for i in range(num)]

# Dar valores a las funciones

# Calcular el tiempo tomado por el bucle `for`
start = time.time()
for_loop(10000000)
end = time.time()
print('Tiempo tomado por el bucle `for`:', (end - start))

# Calcular el tiempo tomado por la comprensión de listas
start = time.time()
list_comprehension(10000000)
end = time.time()
print('Tiempo tomado por la comprensión de listas:', (end - start))
```

**Salida**:

Ahora compilamos el código anterior en Python y, después de una compilación exitosa, lo ejecutamos. Entonces, la salida es la siguiente:

```bash
Tiempo tomado por el bucle `for`: 7.005999803543091
Tiempo tomado por la comprensión de listas: 2.822999954223633
```

## Uso de la Comprensión de Listas para Iterar a Través de una Cadena de Caracteres

La comprensión de listas también se puede utilizar en el caso de cadenas de caracteres,

ya que son iterables.

**Ejemplo**:

Ahora presentamos ejemplos de uso de la comprensión de listas en Python para iterar una cadena de caracteres dada en el código. El código es el siguiente:

```python
letters = [alpha for alpha in 'javatpoint']

print(letters)
```

**Salida**:

```bash
['j', 'a', 'v', 'a', 't', 'p', 'o', 'i', 'n', 't']
```

## Uso de Condiciones en la Comprensión de Listas

Las declaraciones condicionales se pueden utilizar en la comprensión de listas para modificar listas existentes (u otras tuplas). Crearemos una lista con operadores matemáticos, números y un rango de valores.

**Ejemplo**:

```python
number_list = [num for num in range(30) if num % 2 != 0]

print(number_list)
```

**Salida**:

Ahora compilamos el código anterior en Python y, después de una compilación exitosa, lo ejecutamos. Entonces, la salida es la siguiente:

```
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
```

## Suma de Elementos Impares a la Lista

Aquí sumamos los elementos impares de la lista dada. Es un ejemplo de comprensión de listas en Python. El código es el siguiente:

**Ejemplo**:

```python
def Sum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum

List = [47, 69, 73, 97, 105, 845, 307]

newList = [Sum(i) for i in List if i & 1]

print(newList)
```

**Salida**:

Ahora compilamos el código anterior en Python y, después de una compilación exitosa, lo ejecutamos. Entonces, la salida es la siguiente:

```
[11, 15, 10, 16, 6, 17, 10]
```

## Comprensiones de Listas Anidadas

Las comprensiones de listas anidadas son similares a los bucles `for` anidados, ya que son una comprensión de lista dentro de otra comprensión de lista. El programa que implementa el bucle anidado es el siguiente:

**Ejemplo**:

```python
nested_list = []

for _ in range(3):
    # Agregar una sublista vacía dentro de la lista
    nested_list.append([])
    for __ in range(5):
        nested_list[_].append(__ + _)

print(nested_list)
```

**Salida**:

Ahora compilamos el código anterior en Python y, después de una compilación exitosa, lo ejecutamos. Entonces, la salida es la siguiente:

```bash
[[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
```

El mismo resultado se puede lograr con menos líneas de código utilizando comprensiones de listas anidadas.

**Ejemplo**:

El código para la comprensión de listas anidadas es el siguiente:

```python
# Comprensión de listas anidadas
nested_list = [[_ + __ for _ in range(5)] for __ in range(3)]

print(nested_list)
```

**Salida**:

Ahora compilamos el código anterior en Python y, después de una compilación exitosa, lo ejecutamos. Entonces, la salida es la siguiente:

```bash
[[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
```

La comprensión de listas es una herramienta poderosa para describir y crear nuevas listas basadas en las existentes. En general, la comprensión de listas es más ligera y más fácil de usar que las funciones tradicionales de construcción de listas y los bucles. Para proporcionar un código fácil de usar, debemos evitar escribir códigos extensos para las comprensiones de listas. Cada interpretación de la lista u otras iterables se puede rehacer en un bucle `for`, pero no todos los bucles `for` se pueden rehacer en el marco de la comprensión de listas.
