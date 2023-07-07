# Funciones Lambda

En este tutorial, estudiaremos las funciones anónimas, comúnmente llamadas funciones lambda. Entenderemos qué son, cómo ejecutarlas y su sintaxis.

# ¿Qué son las Funciones Lambda en Python?

Las funciones lambda en Python son funciones anónimas, lo que implica que no tienen un nombre. La palabra clave `def` se necesita para crear una función típica en Python, como ya sabemos. También podemos usar la palabra clave `lambda` en Python para definir una función sin nombre.

### Sintaxis de la Función Lambda en Python

```python
lambda argumentos: expresión
```

Esta función acepta cualquier cantidad de argumentos pero solo evalúa y devuelve una expresión.

Las funciones lambda se pueden utilizar siempre que se necesiten argumentos de función. Además de otras formas de formulaciones en funciones, tiene una variedad de aplicaciones en ciertos dominios de codificación. Es importante recordar que, según la sintaxis, las funciones lambda están limitadas a una sola instrucción.

### Ejemplo de Función Lambda en Python

A continuación se muestra un ejemplo de una función lambda que suma 4 al número de entrada.

**Código**

```python
# Código para demostrar cómo podemos usar una función lambda
add = lambda num: num + 4
print(add(6))
```

**Salida:**

```bash
10
```

La función lambda es `lambda num: num+4` en el programa dado. El parámetro es `num`, y la ecuación calculada y devuelta es `num + 4`.

No hay una etiqueta para esta función. Genera un objeto de función asociado con el identificador `add`. Ahora podemos referirnos a ella como una función estándar. La declaración lambda, `lambda num: num+4`, es casi lo mismo que:

**Código**

```python
def add(num):
	return num + 4
print(add(6))
```

**Salida:**

```bash
10
```

# ¿Cuál es la Diferencia Entre las Funciones Lambda y def?

Echemos un vistazo a este ejemplo para ver cómo una función definida de manera convencional con `def` difiere de una función definida usando la palabra clave `lambda`. Este programa calcula el recíproco de un número dado:

**Código**

```python
# Código de Python para mostrar el recíproco del número dado para resaltar la diferencia entre def() y lambda().
def reciprocal(num):
	return 1 / num

lambda_reciprocal = lambda num: 1 / num

# Usando la función definida con la palabra clave def
print("Palabra clave def:", reciprocal(6))

# Usando la función definida con la palabra clave lambda
print("Palabra clave lambda:", lambda_reciprocal(6))
```

**Salida:**

```bash
Palabra clave def: 0.16666666666666666
Palabra clave lambda: 0.16666666666666666
```

Las funciones `reciprocal()` y `lambda_reciprocal()` actúan de manera similar y como se esperaba en el escenario anterior. Echemos un vistazo más de cerca al ejemplo anterior:

Ambas devuelven el recíproco de un número dado sin utilizar lambda. Sin embargo, queríamos declarar una función con el nombre `reciprocal` y enviarle un número mientras se ejecutaba `def`. También se requería usar la palabra clave "return" para proporcionar la salida desde donde se invocó la función después de ser ejecutada.

Usando Lambda: En lugar de una instrucción `return`, las definiciones lambda siempre incluyen una instrucción dada como salida. La belleza de las funciones lambda es su conveniencia. No necesitamos asignar una expresión lambda a una variable porque podemos ponerla en cualquier lugar donde se solicite una función.

# Uso de la Función Lambda con filter()

El método `filter()` acepta dos argumentos en Python: una función y un iterable como una lista.

La función se llama para cada elemento de la lista y se devuelve un nuevo iterable o lista que contiene solo aquellos elementos que devuelven True cuando se suministran a la función.

Aquí hay una ilustración simple del uso del método `filter()` para devolver solo los números impares de una lista.

**Código**

```python
# Código para filtrar números impares de una lista dada
lista_ = [34, 12, 64, 55, 75, 13, 63]

lista_impares = list(filter(lambda num: num % 2 != 0, lista_))

print(lista_impares)
```

**Salida:**

```bash
[55, 75, 13, 63]
```

# Uso de la Función Lambda con map()

Se pasa un método y una lista a la función `map()` de Python.

La función se ejecuta para todos los elementos de la lista, y se genera una nueva lista con elementos generados por la función dada para cada elemento.

En este ejemplo, se utiliza el método `map()` para elevar al cuadrado todas las entradas de una lista.

**Código**

```python
# Código para calcular el cuadrado de cada número de una lista utilizando la función "map()"
lista_numeros = [2, 4, 5, 1, 3, 7, 8, 9, 10]

lista_cuadrados = list(map(lambda num: num ** 2, lista_numeros))

print(lista_cuadrados)
```

**Salida:**

```bash
[4, 16, 25, 1, 9, 49, 64, 81, 100]
```

# Uso de la Función Lambda con List Comprehension

Aplicaremos la función lambda combinada con la comprensión de listas y la palabra clave lambda con un bucle `for` en este ejemplo. Intentaremos imprimir el cuadrado de los números en el rango del 0 al 11.

**Código**

```python
# Código para calcular el cuadrado de cada número de una lista utilizando la comprensión de listas
cuadrados = [lambda num=num: num ** 2 for num in range(0, 11)]

for square in cuadrados:
	print(square(), end=" ")
```

**Salida:**

```bash
0 1 4 9 16 25 36 49 64 81 100
```

# Uso de la Función Lambda con if-else

Utilizaremos la función lambda con el bloque if-else.

**Código**

```python
# Código para usar la función lambda con if-else
Minimo = lambda x, y: x if (x < y) else y

print(Minimo(35, 74))
```

**Salida:**

```bash
35
```

# Uso de Lambda con Múltiples Instrucciones

No se permiten múltiples expresiones en las funciones lambda, pero podemos construir 2 o más funciones lambda y luego llamar a la segunda expresión lambda como argumento de la primera. Veamos cómo usar lambda para encontrar el tercer elemento máximo.

**Código**

```python
# Código para imprimir el tercer número máximo de la lista dada utilizando la función lambda
mi_lista = [[3, 5, 8, 6], [23, 54, 12, 87], [1, 2, 4, 12, 5]]

# Ordenar cada sublista de la lista anterior
ordenar_lista = lambda num: (sorted(n) for n in num)

# Obtener el tercer número más grande de la sublista
tercer_mayor = lambda num, func: [l[len(l) - 2] for l in func(num)]
resultado = tercer_mayor(mi_lista, ordenar_lista)

print(resultado)
```

**Salida:**

```bash
[6, 54, 5]
```
