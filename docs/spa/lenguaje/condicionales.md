# Condicionales

# Sentencias If-else

La toma de decisiones es el aspecto más importante de casi todos los lenguajes de programación. Como su nombre indica, la toma de decisiones nos permite ejecutar un bloque de código particular para una decisión específica. Aquí, las decisiones se toman en función de la validez de condiciones particulares. La comprobación de condiciones es el fundamento de la toma de decisiones.

En Python, la toma de decisiones se realiza mediante las siguientes sentencias:

| Sentencia | Descripción |
| --- | --- |
| Sentencia If | La sentencia if se utiliza para probar una condición específica. Si la condición es verdadera, se ejecutará un bloque de código (bloque if). |
| Sentencia If - else | La sentencia if-else es similar a la sentencia if, excepto que también proporciona un bloque de código para el caso falso de la condición que se va a comprobar. Si la condición proporcionada en la sentencia if es falsa, entonces se ejecutará la sentencia else. |
| Sentencia if anidada | Las sentencias if anidadas nos permiten utilizar una sentencia if-else dentro de una sentencia if externa. |

# Sangría en Python

Para facilitar la programación y lograr la simplicidad, Python no permite el uso de paréntesis para el código a nivel de bloque. En Python, se utiliza la sangría para declarar un bloque. Si dos declaraciones tienen el mismo nivel de sangría, entonces forman parte del mismo bloque.

Generalmente, se proporcionan cuatro espacios para sangrar las declaraciones, que es una cantidad típica de sangría en Python.

La sangría es la parte más utilizada del lenguaje Python, ya que declara el bloque de código. Todas las declaraciones de un bloque tienen la misma sangría. Veremos cómo se realiza la sangría real en la toma de decisiones y otras cosas en Python.

# La sentencia if

La sentencia if se utiliza para probar una condición particular y, si la condición es verdadera, ejecuta un bloque de código conocido como bloque if. La condición de la sentencia if puede ser cualquier expresión lógica válida que pueda evaluarse como verdadera o falsa.

!https://static.javatpoint.com/python/images/python-if-statement.png

La sintaxis de la sentencia if es la siguiente:

```python
if expresión:
    sentencia
```

**Ejemplo 1:**

```python
# Programa Python simple para entender la sentencia if

num = int(input("Ingrese el número:"))

# Aquí, tomamos un número entero y tomamos la entrada dinámicamente

if num % 2 == 0:

# Aquí, verificamos la condición. Si la condición es verdadera, entraremos al bloque

    print("El número dado es un número par")
```

**Salida:**

```
Ingrese el número: 10
El número dado es un número par
```

**Ejemplo 2:** Programa para imprimir el mayor de tres números.

```python
# Programa Python simple para imprimir el mayor de tres números.

a = int(input("Ingrese a: "))

b = int(input("Ingrese b: "))

c = int(input("Ingrese c: "))

if a > b and a > c:

# Aquí, verificamos la condición. Si la condición es verdadera, entraremos al bloque

    print("Delos tres números dados, a es el mayor")

if b > a and b > c:

# Aquí, verificamos la condición. Si la condición es verdadera, entraremos al bloque

    print("Delos tres números dados, b es el mayor")

if c > a and c > b:

# Aquí, verificamos la condición. Si la condición es verdadera, entraremos al bloque

    print("Delos tres números dados, c es el mayor")
```

**Salida:**

```
Ingrese a: 100
Ingrese b: 120
Ingrese c: 130
Delos tres números dados, c es el mayor
```

# La sentencia if-else

La sentencia if-else proporciona un bloque else combinado con la sentencia if que se ejecuta en el caso falso de la condición.

Si la condición es verdadera, entonces se ejecutará el bloque if. De lo contrario, se ejecutará el bloque else.

!https://static.javatpoint.com/python/images/python-if-else-statement.png

La sintaxis de la sentencia if-else es la siguiente:

```python
if condición:
    # bloque de sentencias if
else:
    # otro bloque de sentencias (bloque else)
```

**Ejemplo 1:** Programa para comprobar si una persona es elegible para votar o no.

```python
# Programa Python simple para comprobar si una persona es elegible para votar o no.

edad = int(input("Ingrese su edad: "))

# Aquí, tomamos un número entero y tomamos la entrada dinámicamente

if edad >= 18:

# Aquí, verificamos la condición. Si la condición es verdadera, entraremos al bloque

    print("¡Eres elegible para votar!")

else:

    print("¡Lo siento! ¡Tendrás que esperar!")
```

**Salida:**

```
Ingrese su edad: 90
Eres elegible para votar!
```

**Ejemplo 2:** Programa para comprobar si un número es par o no.

```python
# Programa Python simple para comprobar si un número es par o no.

num = int(input("Ingrese el número: "))

# Aquí, tomamos un número entero y tomamos la entrada dinámicamente

if num % 2 == 0:

# Aquí, verificamos la condición. Si la condición es verdadera, entraremos al bloque

    print("El número dado es un número par")

else:

    print("El número dado es un número impar")
```

**Salida:**

```
Ingrese el número: 10
El número dado es un número par
```

# La sentencia elif

La sentencia elif nos permite comprobar múltiples condiciones y ejecutar el bloque de sentencias específico dependiendo de la condición verdadera entre ellas. Podemos tener cualquier cantidad de sentencias elif en nuestro programa, según nuestras necesidades. Sin embargo, el uso de elif es opcional.

La sentencia elif funciona como una sentencia if-else-if en C. Debe ser seguida por una sentencia if.

La sintaxis de la sentencia elif es la siguiente:

```python
if expresión 1:
    # bloque de sentencias
elif expresión 2:
    # bloque de sentencias

elif expresión 3:
    # bloque de sentencias
else:
    # bloque de sentencias
```

!https://static.javatpoint.com/python/images/python-elif-statement.png

**Ejemplo 1:**

```python
# Programa Python simple para entender la sentencia elif

numero = int(input("Ingrese el número: "))

# Aquí, tomamos un número entero y tomamos la entrada dinámicamente

if numero == 10:

# Aquí, verificamos la condición. Si la condición es verdadera, entraremos al bloque

    print("El número dado es igual a 10")

elif numero == 50:

# Aquí, verificamos la condición. Si la condición es verdadera, entraremos al bloque

    print("El número dado es igual a 50")

elif numero == 100:

# Aquí, verificamos la condición. Si la condición es verdadera, entraremos al bloque

    print("El número dado es igual a 100")

else:

    print("El número dado no es igual a 10, 50 o 100")
```

**Salida:**

```bash
Ingrese el número: 15
El número dado no es igual a 10, 50 o 100
```

**Ejemplo 2:**

```python
# Programa Python simple para entender la sentencia elif

marcas = int(input("Ingrese las marcas: "))

# Aquí, tomamos las marcas como un número entero y tomamos la entrada dinámicamente

if marcas > 85 and marcas <= 100:

# Aquí, verificamos la condición. Si la condición es verdadera, entraremos al bloque

    print("¡Felicidades! ¡Obtuviste la calificación A ...")

elif marcas > 60 and marcas <= 85:

# Aquí, verificamos la condición. Si la condición es verdadera, entraremos al bloque

    print("Obtuviste la calificación B + ...")

elif marcas > 40 and marcas <= 60:

# Aquí, verificamos la condición. Si la condición es verdadera, entraremos al bloque

    print("Obtuviste la calificación B ...")

elif (marcas > 30 and marcas <= 40):

# Aquí, verificamos la condición. Si la condición es verdadera, entraremos al bloque

    print("Obtuviste la calificación C ...")

else:

    print("¿Lo siento, has reprobado?")
```

**Salida:**

```bash
Ingrese las marcas: 89
¡Felicidades! ¡Obtuviste la calificación A ...
```
