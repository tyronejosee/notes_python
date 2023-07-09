# Conjuntos

Un conjunto en Python es una colección de elementos desordenados. Cada elemento en el conjunto debe ser único, inmutable y los conjuntos eliminan los elementos duplicados. Los conjuntos son mutables, lo que significa que podemos modificarlos después de su creación.

A diferencia de otras colecciones en Python, los elementos del conjunto no tienen un índice adjunto, es decir, no podemos acceder directamente a ningún elemento del conjunto mediante un índice. Sin embargo, podemos imprimirlos todos juntos o podemos obtener la lista de elementos recorriendo el conjunto.

## Creación de un Conjunto

El conjunto se puede crear encerrando los elementos inmutables separados por comas entre llaves `{}`. Python también proporciona el método set(), que se puede utilizar para crear el conjunto mediante la secuencia pasada.

**Ejemplo:** Usando llaves

```python
Dias = {"Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"}

print(Dias)
print(type(Dias))
print("recorriendo los elementos del conjunto ...")

for i in Dias:
    print(i)
```

**Salida:**

```bash
{'Viernes', 'Martes', 'Lunes', 'Sábado', 'Jueves', 'Domingo', 'Miércoles'}
<class 'set'>
recorriendo los elementos del conjunto ...
Viernes
Martes
Lunes
Sábado
Jueves
Domingo
Miércoles
```

**Ejemplo:** Usando el método set()

```python
Dias = set(["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])

print(Dias)
print(type(Dias))
print("recorriendo los elementos del conjunto ...")

for i in Dias:
    print(i)
```

**Salida:**

```bash
{'Viernes', 'Miércoles', 'Jueves', 'Sábado', 'Lunes', 'Martes', 'Domingo'}
<class 'set'>
recorriendo los elementos del conjunto ...
Viernes
Miércoles
Jueves
Sábado
Lunes
Martes
Domingo
```

Puede contener cualquier tipo de elemento, como enteros, flotantes, tuplas, etc. Pero los elementos mutables (lista, diccionario, conjunto) no pueden ser miembros de un conjunto. Considera el siguiente ejemplo.

**Ejemplo:**

```python
# Creando un conjunto que tiene elementos inmutables
set1 = {1, 2, 3, "JavaTpoint", 20.5, 14}
print(type(set1))

# Creando un conjunto que tiene un elemento mutable
set2 = {1, 2, 3, ["Javatpoint", 4]}
print(type(set2))
```

**Salida:**

```bash
<class 'set'>

Traceback (most recent call last)
<ipython-input-5-9605bb6fbc68> in <module>
      4 
      5 #Creating a set which holds mutable elements
----> 6 set2 = {1,2,3,["Javatpoint",4]}
      7 print(type(set2))

TypeError: unhashable type: 'list'
```

En el código anterior, hemos creado dos conjuntos. El conjunto set1 tiene elementos inmutables y set2 tiene un elemento mutable como lista. Al verificar el tipo de set2, se generó un error, lo que significa que un conjunto solo puede contener elementos inmutables.

Crear un conjunto vacío es un poco diferente porque las llaves {} vacías también se utilizan para crear un diccionario. Por lo tanto, Python proporciona el método set() que se utiliza sin argumentos para crear un conjunto vacío.

**Ejemplo:**

```python
# Las llaves {} vacías crearán un diccionario
set3 = {}
print(type(set3))

# Conjunto vacío usando la función set()
set4 = set()
print(type(set4))
```

**Salida:**

```bash
<class 'dict'>
<class 'set'>
```

Veamos qué sucede si proporcionamos un elemento duplicado al conjunto.

```python
set5 = {1, 2, 4, 4, 5, 8, 9, 9, 10}
print("Conjunto con elementos únicos:", set5)
```

**Salida:**

```bash
Conjunto con elementos únicos: {1, 2, 4, 5, 8, 9, 10}
```

En el código anterior, podemos ver que set5 contenía varios elementos duplicados y al imprimirlo se eliminó la duplicidad del conjunto.

## Agregar Elementos al Conjunto

Python proporciona el método add() y el método update() que se pueden utilizar para agregar elementos particulares al conjunto. El método add() se utiliza para agregar un solo elemento, mientras que el método update() se utiliza para agregar múltiples elementos al conjunto. Considera el siguiente ejemplo.

**Ejemplo:** Usando el método add()

```python
Meses = set(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"])

print("\\nImprimiendo el conjunto original ...")
print(Meses)
print("\\nAgregando otros meses al conjunto ...")

Meses.add("Julio")
Meses.add("Agosto")

print("\\nImprimiendo el conjunto modificado ...")
print(Meses)
print("\\nRecorriendo los elementos del conjunto ...")

for i in Meses:
    print(i)
```

**Salida:**

```bash
Imprimiendo el conjunto original ...
{'Febrero', 'Mayo', 'Abril', 'Marzo', 'Junio', 'Enero'}

Agregando otros meses al conjunto ...

Imprimiendo el conjunto modificado ...
{'Febrero', 'Julio', 'Mayo', 'Abril', 'Marzo', 'Agosto', 'Junio', 'Enero'}

Recorriendo los elementos del conjunto ...
Febrero
Julio
Mayo
Abril
Marzo
Agosto
Junio
Enero
```

Para agregar más de un elemento al conjunto, Python proporciona el método update(). Acepta un iterable como argumento.

**Ejemplo:** Usando la función update()

```python
Meses = set(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"])

print("\\nImprimiendo el conjunto original ...")
print(Meses)
print("\\nActualizando el conjunto original ...")

Meses.update(["Julio", "Agosto", "Septiembre", "Octubre"])

print("\\nImprimiendo el conjunto modificado ...")
print(Meses)
```

**Salida:**

```bash
Imprimiendo el conjunto original ...
{'Enero', 'Febrero', 'Abril', 'Mayo', 'Junio', 'Marzo'}

Actualizando el conjunto original ...
Imprimiendo el conjunto modificado ...
{'Enero', 'Febrero', 'Abril', 'Agosto', 'Octubre', 'Mayo', 'Junio', 'Julio', 'Septiembre', 'Marzo'}
```

## Eliminación de Elementos del Conjunto

Python proporciona los métodos **discard()** y **remove()** que se pueden utilizar para eliminar elementos del conjunto. La diferencia entre estas funciones es que si se utiliza la función **discard()** y el elemento no existe en el conjunto, el conjunto permanecerá sin cambios, mientras que el método **remove()** generará un error.

**Ejemplo:** Usando el método discard()

```python
meses = set(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"])

print("\\nImprimiendo el conjunto original ...")
print(meses)
print("\\nEliminando algunos meses del conjunto ...")

meses.discard("Enero")
meses.discard("Mayo")

print("\\nImprimiendo el conjunto modificado ...")
print(meses)
print("\\nRecorriendo los elementos del conjunto ...")

for i in meses:
    print(i)
```

**Salida:**

```bash
Imprimiendo el conjunto original ...
{'Febrero', 'Enero', 'Marzo', 'Abril', 'Junio', 'Mayo'}

Eliminando algunos meses del conjunto ...

Imprimiendo el conjunto modificado ...
{'Febrero', 'Marzo', 'Abril', 'Junio'}

Recorriendo los elementos del conjunto ...
Febrero
Marzo
Abril
Junio
```

Python también proporciona el método **remove()** para eliminar un elemento del conjunto. Considera el siguiente ejemplo para eliminar elementos utilizando el método **remove()**.

**Ejemplo:** Usando la función remove()

```python
meses = set(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"])

print("\\nImprimiendo el conjunto original ...")
print(meses)
print("\\nEliminando algunos meses del conjunto ...")

meses.remove("Enero")
meses.remove("Mayo")

print("\\nImprimiendo el conjunto modificado ...")
print(meses)
```

**Salida:**

```bash
Imprimiendo el conjunto original ...
{'Febrero', 'Junio', 'Abril', 'Mayo', 'Enero', 'Marzo'}

Eliminando algunos meses del conjunto ...

Imprimiendo el conjunto modificado ...
{'Febrero', 'Junio', 'Abril', 'Marzo'}
```

También podemos usar el método **pop()** para eliminar un elemento del conjunto. Por lo general, el método **pop()** siempre eliminará el último elemento, pero como el conjunto no está ordenado, no podemos determinar qué elemento se eliminará del conjunto.

Considera el siguiente ejemplo para eliminar el elemento del conjunto utilizando el método **pop()**.

```python
meses = set(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"])

print("\\nImprimiendo el conjunto original ...")
print(meses)
print("\\nEliminando algunos meses del conjunto ...")

meses.pop()
meses.pop()

print("\\nImprimiendo el conjunto modificado ...")
print(meses)
```

**Salida:**

```bash
Imprimiendo el conjunto original ...
{'Junio', 'Enero', 'Mayo', 'Abril', 'Febrero', 'Marzo'}

Eliminando algunos meses del conjunto ...

Imprimiendo el conjunto modificado ...
{'Mayo', 'Abril', 'Febrero', 'Marzo'}
```

En el código anterior, el último elemento del conjunto **meses** es **Marzo**, pero el método **pop()** eliminó **Junio** y **Enero** porque el conjunto no está ordenado y el método **pop()** no pudo determinar el último elemento del conjunto.

Python proporciona el método **clear()** para eliminar todos los elementos del conjunto.

**Ejemplo:**

```python
meses = set(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"])

print("\\nImprimiendo el conjunto original ...")
print(meses)
print("\\nEliminando todos los elementos del conjunto ...")

meses.clear()

print("\\nImprimiendo el conjunto modificado ...")
print(meses)
```

**Salida:**

```bash
Imprimiendo el conjunto original ...
{'Enero', 'Mayo', 'Junio', 'Abril', 'Marzo', 'Febrero'}

Eliminando todos los elementos del conjunto ...

Imprimiendo el conjunto modificado ...
set()
```

## Diferencia Entre discard() y remove()

A pesar de que los métodos **discard()** y **remove()** realizan la misma tarea, hay una diferencia principal entre ellos.

Si la clave que se va a eliminar del conjunto utilizando discard() no existe en el conjunto, Python no generará un error. El programa mantendrá su flujo de control.

Por otro lado, si el elemento que se va a eliminar del conjunto utilizando remove() no existe en el conjunto, Python generará un error.

**Ejemplo:**

```python
meses = set(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"])

print("\\nImprimiendo el conjunto original ...")
print(meses)
print("\\nEliminando elementos mediante el método discard()...")

meses.discard("Feb")  # no generará un error aunque la clave "feb" no esté disponible en el conjunto

print("\\nImprimiendo el conjunto modificado...")
print(meses)
print("\\nEliminando elementos mediante el método remove()...")

meses.remove("Jan")  # generará un error ya que la clave "jan" no está disponible en el conjunto

print("\\nImprimiendo el conjunto modificado...")
print(meses)
```

**Salida:**

```bash
Imprimiendo el conjunto original ...
{'Marzo', 'Enero', 'Abril', 'Junio', 'Febrero', 'Mayo'}

Eliminando elementos mediante el método discard()...

Imprimiendo el conjunto modificado...
{'Marzo', 'Enero', 'Abril', 'Junio', 'Febrero', 'Mayo'}

Eliminando elementos mediante el método remove()...
Traceback (most recent call last):
  File "set.py", line 9, in <module>
    meses.remove("Jan")
KeyError: 'Jan'
```

## Operaciones con Conjuntos

Es posible realizar operaciones matemáticas con conjuntos, como unión, intersección, diferencia y diferencia simétrica. Python proporciona la capacidad de llevar a cabo estas operaciones mediante operadores o métodos. Describiremos estas operaciones de la siguiente manera.

### Unión de Dos Conjuntos

Para combinar dos o más conjuntos en uno solo en Python, utiliza la función union(). Todas las características distintivas de cada conjunto combinado están presentes en el conjunto final. Como parámetros, se pueden pasar uno o más conjuntos a la función union(). Si hay solo un conjunto, la función devuelve una copia del conjunto suministrado como único parámetro. Si se suministran más de un conjunto como argumento, el método devuelve un nuevo conjunto que contiene todos los elementos diferentes de todos los argumentos.

![python-set.png](Conjuntos%20273ec4d926b94660a32ee7aaeaf2d441/python-set.png)

Considera el siguiente ejemplo para calcular la unión de dos conjuntos.

**Ejemplo:** Utilizando el operador de unión |

```python
Dias1 = {"Lunes", "Martes", "Miércoles", "Jueves", "Domingo"}
Dias2 = {"Viernes", "Sábado", "Domingo"}

print(Dias1 | Dias2)  # imprime la unión de los conjuntos
```

**Salida:**

```bash
{'Martes', 'Domingo', 'Lunes', 'Viernes', 'Jueves', 'Miércoles', 'Sábado'}
```

Python también proporciona el método **union()**, que también se puede utilizar para calcular la unión de dos conjuntos. Considera el siguiente ejemplo.

**Ejemplo:** Utilizando el método union()

```python
Dias1 = {"Lunes", "Martes", "Miércoles", "Jueves"}
Dias2 = {"Viernes", "Sábado", "Domingo"}

print(Dias1.union(Dias2))  # imprime la unión de los conjuntos
```

**Salida:**

```bash
{'Martes', 'Miércoles', 'Viernes', 'Domingo', 'Lunes', 'Jueves', 'Sábado'}
```

Ahora, también podemos realizar la unión de más de dos conjuntos utilizando la función union(), por ejemplo:

**Programa:**

```python
# Crear tres conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
conjunto3 = {3, 4, 5}

# Encontrar los elementos comunes entre los tres conjuntos
elementos_comunes = conjunto1.union(conjunto2, conjunto3)

# Imprimir los elementos comunes
print(elementos_comunes)
```

**Salida:**

```bash
{1, 2, 3, 4, 5}
```

## Intersección de Dos Conjuntos

Para descubrir qué elementos son comunes entre dos o más conjuntos en Python, aplica la función intersection(). Solo se incluyen los elementos que están en todos los conjuntos comparados en el conjunto final. También se pueden utilizar uno o más conjuntos como parámetros de la función intersection(). Si hay solo un conjunto, la función devuelve una copia del conjunto suministrado como único parámetro. Si se suministran múltiples conjuntos como argumentos, el método devuelve un nuevo conjunto que solo contiene los elementos presentes en todos los conjuntos comparados.

La intersección de dos conjuntos se puede realizar mediante el operador **and &** o mediante la función **intersection()**. La intersección de los dos conjuntos se define como el conjunto de elementos que son comunes a ambos conjuntos.

![python-set2.png](Conjuntos%20273ec4d926b94660a32ee7aaeaf2d441/python-set2.png)

**Ejemplo: U**tilizando el operador &

```python
Dias1 = {"Lunes", "Martes", "Miércoles", "Jueves"}

Dias2 = {"Lunes", "Martes", "Domingo", "Viernes"}

print(Dias1 & Dias2)  # imprime la intersección de los dos conjuntos
```

**Salida:**

```bash
{'Martes', 'Lunes'}
```

**Ejemplo: U**tilizando el método intersection()

```python
conjunto1 = {"Devansh", "John", "David", "Martin"}
conjunto2 = {"Steve", "Milan", "David", "Martin"}

print(conjunto1.intersection(conjunto2))  # imprime la intersección de los dos conjuntos
```

**Salida:**

```bash
{'Martin', 'David'}
```

**Ejemplo:**

```python
conjunto1 = {1, 2, 3, 4, 5, 6, 7}
conjunto2 = {1, 2, 20, 32, 5, 9}
conjunto3 = conjunto1.intersection(conjunto2)

print(conjunto3)
```

**Salida:**

```bash
{1, 2, 5}
```

De manera similar a la función de unión, también podemos realizar la intersección de más de dos

conjuntos al mismo tiempo.

Por ejemplo:

**Programa:**

```python
# Crear tres conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
conjunto3 = {3, 4, 5}

# Encontrar los elementos comunes entre los tres conjuntos
elementos_comunes = conjunto1.intersection(conjunto2, conjunto3)

# Imprimir los elementos comunes
print(elementos_comunes)
```

**Salida:**

```bash
{3}
```

## El Método intersection_update()

El método **intersection_update()** elimina los elementos del conjunto original que no están presentes en ambos conjuntos (en todos los conjuntos si se especifica más de uno).

El método **intersection_update()** es diferente del método intersection() ya que modifica el conjunto original eliminando los elementos no deseados, mientras que el método intersection() devuelve un nuevo conjunto.

**Ejemplo:**

```python
a = {"Devansh", "bob", "castle"}
b = {"castle", "dude", "emyway"}
c = {"fuson", "gaurav", "castle"}

a.intersection_update(b, c)

print(a)
```

**Salida:**

```bash
{'castle'}
```

## Diferencia Entre Dos Conjuntos

La diferencia entre dos conjuntos se puede calcular utilizando el operador de sustracción (-) o el método **difference()**. Supongamos que hay dos conjuntos A y B, y la diferencia A-B denota que se obtendrá el conjunto resultante que contiene los elementos de A que no están presentes en el conjunto B.

![python-set3.png](Conjuntos%20273ec4d926b94660a32ee7aaeaf2d441/python-set3.png)

Considera el siguiente ejemplo.

**Ejemplo:** Utilizando el operador de sustracción (-)

```python
Dias1 = {"Lunes", "Martes", "Miércoles", "Jueves"}
Dias2 = {"Lunes", "Martes", "Domingo"}

print(Dias1 - Dias2)  # se imprimirá {"Miércoles", "Jueves"}
```

**Salida:**

```bash
{'Jueves', 'Miércoles'}
```

**Ejemplo:** Utilizando el método difference()

```python
Dias1 = {"Lunes", "Martes", "Miércoles", "Jueves"}
Dias2 = {"Lunes", "Martes", "Domingo"}

print(Dias1.difference(Dias2))  # imprime la diferencia de los dos conjuntos, Dias1 y Dias2
```

**Salida:**

```bash
{'Jueves', 'Miércoles'}
```

## Diferencia Simétrica de Dos Conjuntos

En Python, la diferencia simétrica entre set1 y set2 es el conjunto de elementos que están presentes en uno u otro conjunto, pero no en ambos conjuntos. En otras palabras, son los elementos que están en set1 o set2, pero no en su intersección.

La diferencia simétrica de dos conjuntos se puede calcular utilizando el método symmetric_difference() de Python. Este método devuelve un nuevo conjunto que contiene todos los elementos que están en uno u otro conjunto, pero no en ambos. Considera el siguiente ejemplo:

![python-set4.png](Conjuntos%20273ec4d926b94660a32ee7aaeaf2d441/python-set4.png)

**Ejemplo:** Utilizando el operador ^

```python
a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 9, 8, 10}
c = a ^ b

print(c)
```

**Salida:**

```bash
{3, 4, 5, 6, 8, 9, 10}
```

**Ejemplo:** Utilizando el método symmetric_difference()

```python
a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 9, 8, 10}
c = a.symmetric_difference(b)

print(c)
```

**Salida:**

```bash
{3, 4, 5, 6, 8, 9, 10}
```

## Comparación de Conjuntos

En Python, puedes comparar conjuntos para verificar si son iguales, si un conjunto es un subconjunto o un superconjunto de otro, o si dos conjuntos tienen elementos en común.

Aquí están los operadores de comparación de conjuntos disponibles en Python:

- `==`: verifica si dos conjuntos tienen los mismos elementos, sin importar su orden.
- `!=`: verifica si dos conjuntos no son iguales.
- `<`: verifica si el conjunto de la izquierda es un subconjunto estricto del conjunto de la derecha (es decir, todos los elementos en el conjunto de la izquierda también están en el conjunto de la derecha, pero el conjunto de la derecha tiene elementos adicionales).
- `<=`: verifica si el conjunto de la izquierda es un subconjunto del conjunto de la derecha (es decir, todos los elementos en el conjunto de la izquierda también están en el conjunto de la derecha).
- `>`: verifica si el conjunto de la izquierda es un superconjunto estricto del conjunto de la derecha (es decir, todos los elementos en el conjunto de la derecha también están en el conjunto de la izquierda, pero el conjunto de la izquierda tiene elementos adicionales).
- `>=`: verifica si el conjunto de la izquierda es un superconjunto del conjunto de la derecha (es decir, todos los elementos en el conjunto de la derecha también están en el conjunto de la izquierda).

**Ejemplo:**

```python
Days1 = {"Lunes", "Martes", "Miércoles", "Jueves"}
Days2 = {"Lunes", "Martes"}
Days3 = {"Lunes", "Martes", "Viernes"}

# Days1 es un superconjunto de Days2, por lo tanto, imprimirá True.
print(Days1 > Days2)

# imprime False ya que Days1 no es un subconjunto de Days2.
print(Days1 < Days2)

# imprime False ya que Days2 y Days3 no son equivalentes.
print(Days2 == Days3)
```

**Salida:**

```bash
True
False
False
```

## Conjuntos Inmutables (Frozensets)

En Python, un conjunto inmutable (frozenset) es una versión inmutable del tipo de dato de conjunto incorporado. Es similar a un conjunto, pero su contenido no puede cambiarse una vez que se crea un conjunto inmutable.

Los objetos de conjuntos inmutables son colecciones desordenadas de elementos únicos, al igual que los conjuntos. Se pueden utilizar de la misma manera que los conjuntos, excepto que no se pueden modificar. Debido a que son inmutables, los objetos de conjuntos inmutables se pueden utilizar como elementos de otros conjuntos o como claves de diccionario, mientras que los conjuntos estándar no pueden.

Una de las principales ventajas de utilizar objetos de conjuntos inmutables es que son hashables, lo que significa que se pueden utilizar como claves en diccionarios o como elementos de otros conjuntos. Su contenido no puede cambiar, por lo que sus valores hash permanecen constantes. Los conjuntos estándar no son hashables porque se pueden modificar, por lo que sus valores hash pueden cambiar.

Los objetos de conjuntos inmutables admiten muchas de las mismas operaciones que los conjuntos, como unión, intersección, diferencia y diferencia simétrica. También admiten operaciones que no modifican el conjunto inmutable, como len(), min(), max() y in.

**Considera el siguiente ejemplo para crear un frozenset.**

```python
Frozenset = frozenset([1, 2, 3, 4, 5])

print(type(Frozenset))
print("\\nImprimiendo el contenido del frozenset...")

for i in Frozenset:
    print(i)

Frozenset.add(6)  # da un error ya que no se puede cambiar el contenido del frozenset después de su creación
```

**Salida:**

```bash
<class 'frozenset'>

Imprimiendo el contenido del frozenset...
1
2
3
4
5
Traceback (most recent call last):
  File "set.py", line 6, in <module>
    Frozenset.add(6)  # da un error ya que no se puede cambiar el contenido del frozenset después de su creación
AttributeError: 'frozenset' object has no attribute 'add'
```

## Frozenset Para Diccionarios

Si pasamos un diccionario como secuencia dentro del método frozenset(), tomará solo las claves del diccionario y devolverá un frozenset que contiene las claves del diccionario como sus elementos.

**Ejemplo:**

```python
Diccionario = {"Nombre": "John", "País": "EE. UU.", "ID": 101}

print(type(Diccionario))

Frozenset = frozenset(Diccionario)  # Frozenset contendrá las claves del diccionario

print(type(Frozenset))

for i in Frozenset:
    print(i)
```

**Salida:**

```bash
<class 'dict'>
<class 'frozenset'>
Nombre
País
ID
```

### Ejemplo de Programación con Conjuntos

**Ejemplo:** Escribe un programa para eliminar un número dado del conjunto.

```python
my_set = {1, 2, 3, 4, 5, 6, 12, 24}
n = int(input("Ingresa el número que deseas eliminar: "))
my_set.discard(n)

print("Después de eliminar:", my_set)
```

**Salida:**

```bash
Ingresa el número que deseas eliminar: 12
Después de eliminar: {1, 2, 3, 4, 5, 6, 24}
```

**Ejemplo:** Escribe un programa para agregar múltiples elementos al conjunto.

```python
set1 = set([1, 2, 4, "John", "CS"])
set1.update(["Apple", "Mango", "Grapes"])

print(set1)
```

**Salida:**

```bash
{1, 2, 4, 'Apple', 'John', 'CS', 'Mango', 'Grapes'}
```

**Ejemplo:** Escribe un programa para encontrar la unión entre dos conjuntos.

```python
set1 = set(["Peter", "Joseph", 65, 59, 96])
set2 = set(["Peter", 1, 2, "Joseph"])
set3 = set1.union(set2)

print(set3)
```

**Salida:**

```bash
{96, 65, 2, 'Joseph', 1, 'Peter', 59}
```

**Ejemplo:** Escribe un programa para encontrar la intersección entre dos conjuntos.

```python
set1 = {23, 44, 56, 67, 90, 45, "Javatpoint"}
set2 = {13, 23, 56, 76, "Sachin"}
set3 = set1.intersection(set2)

print(set3)
```

**Salida:**

```bash
{56, 23}
```

**Ejemplo:** Escribe un programa para agregar un elemento al frozenset.

```python
set1 = {23, 44, 56, 67, 90, 45, "Javatpoint"}
set2 = {13, 23, 56, 76, "Sachin"}
set3 = set1.intersection(set2)

print(set3)
```

**Salida:**

```bash
TypeError: 'frozenset' object does not support item assignment
```

El código anterior genera un error porque los frozensets son inmutables y no se pueden cambiar después de su creación.

**Ejemplo:** Escribe un programa para encontrar el issuperset, issubset y superset.

```python
set1 = set(["Peter", "James", "Camroon", "Ricky", "Donald"])
set2 = set(["Camroon", "Washington", "Peter"])
set3 = set(["Peter"])
issubset = set1 >= set2

print(issubset)

issuperset = set1 <= set2

print(issuperset)

issubset = set3 <= set2

print(issubset)

issuperset = set2 >= set3

print(issuperset)
```

**Salida:**

```bash
False
False
True
True
```

## Métodos Integrados de Conjuntos

Python contiene los siguientes métodos que se pueden utilizar con conjuntos.

| SN | Método | Descripción |
| --- | --- | --- |
| 1 | add() | Añade un elemento al conjunto. No tiene efecto si el elemento ya está presente en el conjunto. |
| 2 | clear() | Elimina todos los elementos del conjunto. |
| 3 | copy() | Devuelve una copia superficial del conjunto. |
| 4 | difference_update(....) | Modifica este conjunto eliminando todos los elementos que también están presentes en los conjuntos especificados. |
| 5 | discard() | Elimina el elemento especificado del conjunto. |
| 6 | intersection() | Devuelve un nuevo conjunto que contiene solo los elementos comunes de ambos conjuntos (todos los conjuntos si se especifican más de dos). |
| 7 | intersection_update(....) | Elimina los elementos del conjunto original que no están presentes en ambos conjuntos (todos los conjuntos si se especifica más de uno). |
| 8 | isdisjoint(....) | Devuelve True si dos conjuntos no tienen intersección. |
| 9 | issubset(....) | Indica si otro conjunto contiene a este conjunto. |
| 10 | issuperset(....) | Indica si este conjunto contiene a otro conjunto. |
| 11 | pop() | Elimina y devuelve un elemento arbitrario del conjunto que es el último elemento del conjunto. Genera un KeyError si el conjunto está vacío. |
| 12 | remove() | Elimina un elemento de un conjunto; debe ser un miembro. Si el elemento no es un miembro, genera un KeyError. |
| 13 | symmetric_difference(....) | Devuelve la diferencia simétrica entre dos conjuntos como un nuevo conjunto. |
| 14 | symmetric_difference_update(....) | Actualiza un conjunto con la diferencia simétrica entre sí mismo y otro conjunto. |
| 15 | union(....) | Devuelve la unión de los conjuntos como un nuevo conjunto (es decir, todos los elementos que están en cualquiera de los conjuntos). |
| 16 | update() | Actualiza un conjunto con la unión de sí mismo y otros conjuntos. |
