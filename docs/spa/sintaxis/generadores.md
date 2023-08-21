# Generadores

## ¿Qué es Un Generador?

Los generadores en Python son capacidades que devuelven un objeto iterable y se utilizan para crear iteradores. Recorren simultáneamente todos los elementos. Un generador también puede ser una expresión con una sintaxis similar a la comprensión de listas de Python.

Crear una iteración en Python puede ser bastante complejo; necesitamos implementar los métodos `__iter__()` y `__next__()` para llevar un seguimiento de los estados internos.

Crear iteradores puede ser un proceso largo. Es por eso que el generador juega un papel esencial en simplificar este proceso. Si no se encuentra ningún valor en la iteración, se lanza la excepción **StopIteration**.

## ¿Cómo Crear Una Función Generadora?

En Python, crear un generador no es difícil en absoluto. Es similar a la función típica definida por la palabra clave `def`, pero en lugar de `return`, utiliza la palabra clave `yield`. También podemos decir que si el cuerpo de cualquier función contiene una instrucción `yield`, automáticamente se convierte en una función generadora.

**Ejemplo:**

```python
def simple():
    for i in range(10):
        if i % 2 == 0:
            yield i

# Llamada sucesiva a la función utilizando un bucle for
for i in simple():
    print(i)
```

**Salida:**

```bash
0
2
4
6
8
```

### yield vs. return

La instrucción `yield` es responsable de controlar el flujo de la función generadora. Al guardar todos los estados y ceder el control al llamador, se detiene la ejecución de la función. Luego, se reanuda la ejecución cuando se llama a la función generadora de manera progresiva. En la función generadora, podemos utilizar varias instrucciones `yield`.

La instrucción `return`, en cambio, devuelve un valor y termina toda la función. Solo se puede usar una única instrucción `return` en la función.

### Usando múltiples declaraciones yield

Podemos usar múltiples declaraciones `yield` en la función generadora.

**Ejemplo:**

```python
def multiple_yield():
    str1 = "Primer String"
    yield str1

    str2 = "Segundo string"
    yield str2

    str3 = "Tercer String"
    yield str3

obj = multiple_yield()
print(next(obj))
print(next(obj))
print(next(obj))
```

**Salida:**

```bash
Primer String
Segundo string
Tercer String
```

### Diferencias Entre Una Función Generadora y Una Función Normal

1. Una función normal contiene solo una instrucción `return`, mientras que una función generadora puede contener una o más instrucciones `yield`.
2. Cuando se llaman a las funciones generadoras, se detienen inmediatamente y se le devuelve el control al llamador. Los estados de las variables locales se conservan entre las llamadas.
3. La excepción `StopIteration` se lanza automáticamente cuando la función termina.

## Expresiones Generadoras

Podemos crear fácilmente una expresión generadora sin utilizar una función definida por el usuario. Es similar a la función lambda, que crea una función anónima. Una función generadora anónima se crea mediante las expresiones generadoras.

La representación de una expresión generadora se asemeja a la comprensión de listas de Python. La única diferencia es que los paréntesis redondos se utilizan en lugar de corchetes cuadrados. La expresión generadora solo calcula un elemento a la vez, mientras que la comprensión de listas calcula la lista completa.

**Ejemplo:**

```python
lista = [1, 2, 3, 4, 5, 6, 7]

# Comprensión de listas
z = [x**3 for x in lista]

# Expresión generadora
a = (x**3 for x in lista)

print(a)
print(z)
```

**Salida:**

```bash
<generator object <genexpr> at 0x01BA3CD8>
[1, 8, 27, 64, 125, 216, 343]
```

En el programa anterior, la comprensión de listas devuelve la lista de cubos de los elementos, mientras que la expresión generadora devuelve una referencia del valor calculado. En lugar de aplicar un bucle `for`, también podemos llamar a `next()` en el objeto generador.

**Ejemplo:**

```python
lista = [1, 2, 3, 4, 5, 6]

z = (x**3 for x in lista)

print(next(z))
print(next(z))
print(next(z))
print(next(z))
```

**Salida:**

```bash
1
8
27
64
```

**Nota:** Cuando llamamos a `next()`, Python llama a `__next__()` en la función a la que se lo hemos pasado como parámetro.

En el programa anterior, hemos utilizado la función `next()`, que devuelve el siguiente elemento de la lista.

**Ejemplo:** Escribir un programa para imprimir la tabla del número dado utilizando el generador.

```python
def table(n):
    for i in range(1, 11):
        yield n * i

for i in table(15):
    print(i)
```

**Salida:**

```bash
15
30
45
60
75
90
105
120
135
150
```

En el ejemplo anterior, una función generadora se itera utilizando un bucle `for`.

## Ventajas de los Generadores

Hay varias ventajas de los generadores. Algunas de ellas son las siguientes:

### 1. Fáciles de Implementar

Los generadores son fáciles de implementar en comparación con los iteradores. En el iterador, tenemos que implementar las funciones `__iter__()` y `__next__()`.

### 2. Eficientes en el Uso de Memoria

Para muchas secuencias, los generadores utilizan la memoria de manera eficiente. La función generadora calcula el valor y suspende su ejecución, mientras que la función normal devuelve una secuencia de la lista, lo que primero crea toda la secuencia en la memoria antes de devolver el resultado. Se reanuda la función para la llamada progresiva. Un generador de sucesión infinita es un gran ejemplo de optimización de memoria.

**Ejemplo:**

```python
import sys

# Comprensión de listas
nums_squared_list = [i * 2 for i in range(1000)]
print(sys.getsizeof("Memoria en Bytes:", nums_squared_list))

# Expresión generadora
nums_squared_gc = (i ** 2 for i in range(1000))
print(sys.getsizeof("Memoria en Bytes:", nums_squared_gc))
```

**Salida:**

```bash
Memoria en Bytes: 4508
Memoria en Bytes: 56
```

Podemos observar en la salida anterior que la comprensión de listas está utilizando 4508 bytes de memoria, mientras que la expresión generadora está utilizando solo 56 bytes de memoria. Esto significa que los objetos generadores son mucho más eficientes que la compresión de listas.

### 3. Creación de Conductos con Generadores

El conducto de información brinda la facilidad de procesar grandes conjuntos de datos o flujos de información sin utilizar memoria adicional de la computadora.

Imaginemos que tenemos un archivo de registro de un restaurante famoso. El archivo de registro tiene una columna (cuarto segmento) que registra la cantidad de hamburguesas vendidas cada hora y queremos totalizarlo para obtener la cantidad total de hamburguesas vendidas en 4 años. En ese caso, el generador puede crear un conducto utilizando una serie de operaciones.

**Ejemplo:**

```python
with open('sells.log') as file:
    burger_col = (line[3] for line in file)
    per_hour = (int(x) for x in burger_col if x != 'N/A')
    print("Total de hamburguesas vendidas =", sum(per_hour))
```

### 4. Generar Secuencias Infinitas

Los generadores pueden generar elementos infinitos. Las secuencias infinitas no pueden caber en la memoria y, como los generadores producen solo un elemento a la vez.

**Ejemplo:**

```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
    print(i)
```

**Salida:**

```python
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
.........
..........
315
316
317
Traceback (most recent call last):
  File "C:\\Users\\DEVANSH SHARMA\\Desktop\\generator.py", line 33, in <module>
    print(i)
KeyboardInterrupt
```
