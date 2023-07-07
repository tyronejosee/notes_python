# Tuplas

Una tupla en Python es un grupo de elementos separados por comas. El indexado, los objetos anidados y las repeticiones de una tupla son similares a los de una lista; sin embargo, a diferencia de una lista, una tupla es inmutable.

La distinción entre ambas es que mientras podemos editar el contenido de una lista, no podemos modificar los elementos de una tupla una vez que han sido asignados.

**Ejemplo**

```python
("Suzuki", "Audi", "BMW", "Skoda") es una tupla.
```

### Características de las Tuplas

- Las tuplas son un tipo de dato inmutable, lo que significa que una vez que se han creado, sus elementos no pueden cambiarse.
- Dado que las tuplas son secuencias ordenadas, cada elemento tiene un orden específico que nunca cambiará.

### Creación de Tuplas

Para crear una tupla, todos los objetos (o "elementos") deben estar encerrados entre paréntesis (), separados por comas. Aunque no es necesario incluir paréntesis, se recomienda hacerlo.

Una tupla puede contener cualquier número de elementos, incluidos elementos con diferentes tipos de datos (diccionario, cadena, número decimal, lista, etc.).

**Código**

```python
# Programa de Python para mostrar cómo crear una tupla

# Crear una tupla vacía
tupla_vacia = ()
print("Tupla vacía:", tupla_vacia)

# Crear una tupla con enteros
tupla_enteros = (4, 6, 8, 10, 12, 14)
print("Tupla con enteros:", tupla_enteros)

# Crear una tupla con objetos de diferentes tipos de datos
tupla_mixta = (4, "Python", 9.3)
print("Tupla con diferentes tipos de datos:", tupla_mixta)

# Crear una tupla anidada
tupla_anidada = ("Python", {4: 5, 6: 2, 8: 2}, (5, 3, 5, 6))
print("Una tupla anidada:", tupla_anidada)
```

**Salida**

```bash
Tupla vacía: ()
Tupla con enteros: (4, 6, 8, 10, 12, 14)
Tupla con diferentes tipos de datos: (4, 'Python', 9.3)
Una tupla anidada: ('Python', {4: 5, 6: 2, 8: 2}, (5, 3, 5, 6))
```

Las tuplas se pueden construir sin utilizar paréntesis. Esto se conoce como empaquetado triple.

**Código**

```python
# Programa de Python para crear una tupla sin utilizar paréntesis

# Crear una tupla
tupla_ = 4, 5.7, "Tuplas", ["Python", "Tuplas"]

# Mostrar la tupla creada
print(tupla_)

# Comprobar el tipo de datos del objeto tupla_
print(type(tupla_))

# Intentar modificar la tupla_
try:
    tupla_[1] = 4.2
except:
    print(TypeError)
```

**Salida**

```bash
(4, 5.7, 'Tuplas', ['Python', 'Tuplas'])
<class 'tuple'>
<class 'TypeError'>
```

La construcción de una tupla a partir de un solo elemento puede ser confusa.

Simplemente agregar paréntesis alrededor del elemento no es suficiente. Para que sea reconocido como una tupla, el elemento debe ir seguido de una coma.

**Código**

```python
# Programa de Python para mostrar cómo crear una tupla con un solo elemento
tupla_individual = ("Tupla")
print(type(tupla_individual))

# Crear una tupla que tenga solo un elemento
tupla_individual = ("Tupla",)
print(type(tupla_individual))

# Crear una tupla sin paréntesis
tupla_individual = "Tupla",
print(type(tupla_individual))
```

**Salida**

```bash
<class 'str'>
<class 'tuple'>
<class 'tuple'>
```

# Acceso a los Elementos de una Tupla

Podemos acceder a los objetos de una tupla de varias formas.

- **Indexación**

Para acceder a un objeto de una tupla, podemos utilizar el operador de indexación [], donde la indexación en la tupla comienza desde 0.

Una tupla con 5 elementos tendrá índices que van desde 0 hasta 4. Se generará un IndexError si intentamos acceder a un índice de la tupla que está fuera del rango de índices de la tupla. En este caso, un índice mayor que 4 estará fuera de rango.

No podemos dar un índice de un tipo de dato flotante u otros tipos porque el índice en Python debe ser un número entero. Aparecerá un TypeError como resultado si proporcionamos un índice flotante.

El siguiente ejemplo ilustra cómo se realiza la indexación en tuplas anidadas para acceder a los elementos.

**Código**

```python
# Programa de Python para mostrar cómo acceder a los elementos de una tupla

# Crear una tupla
tupla_ = ("Python", "Tupla", "Ordenada", "Colección")
print(tupla_[0])
print(tupla_[1])

# Intentar acceder a un elemento con un índice mayor que la longitud de la tupla
try:
    print(tupla_[5])
except Exception as e:
    print(e)

# intentar acceder a elementos a través de un índice de tipo de datos flotante
try:
    print(tupla_[1.0])
except Exception as e:
    print(e)

# Crear una tupla anidada
tupla_anidada = ("Tupla", [4, 6, 2, 6], (6, 2, 6, 7))

# Acceder al índice de una tupla anidada
print(tupla_anidada[0][3])
print(tupla_anidada[1][1])
```

**Salida:**

```bash
Python
Tupla
tuple index out of range
tuple indices must be integers or slices, not float
l
6
```

- **Indexación Negativa**

Los objetos de secuencia de Python admiten la indexación negativa.

El último elemento de la colección se representa con -1, el penúltimo elemento con -2 y así sucesivamente.

**Código**

```python
# Programa de Python para mostrar cómo funciona la indexación negativa en tuplas

# Crear una tupla
tuple_ = ("Python", "Tupla", "Ordenada", "Inmutable")

# Imprimir elementos utilizando índices negativos
print("Elemento en el índice -1:", tuple_[-1])
print("Elementos entre los índices -4 y -1:", tuple_[-4:-1])
```

**Salida:**

```bash
Elemento en el índice -1: Inmutable
Elementos entre los índices -4 y -1: ('Python', 'Tupla', 'Ordenada')
```

# Segmentación

En Python, la segmentación de tuplas es una práctica común y el método más popular para que los programadores manejen problemas prácticos. Piense en una tupla de Python. Para acceder a una variedad de elementos en una tupla, debemos segmentarla. Una forma sencilla de hacerlo es utilizar el colon como operador de segmentación (:).

Podemos utilizar el operador de segmentación, dos puntos (:), para acceder a un rango de elementos de una tupla.

**Código**

```python
# Programa de Python para mostrar cómo funciona la segmentación en tuplas de Python

# Crear una tupla
tupla_ = ("Python", "Tupla", "Ordenada", "Inmutable", "Colección", "Objetos")

# Utilizar la segmentación para acceder a elementos de la tupla
print("Elementos entre los índices 1 y 3:", tuple_[1:3])

# Utilizar indexación negativa en la segmentación
print("Elementos entre los índices 0 y -4:", tuple_[:-4])

# Imprimir toda la tupla utilizando los valores de inicio y fin por defecto.
print("Tupla completa:", tuple_[:])
```

**Salida**

```bash
Elementos entre los índices 1 y 3: ('Tupla', 'Ordenada')
Elementos entre los índices 0 y -4: ('Python', 'Tupla')
Tupla completa: ('Python', 'Tupla', 'Ordenada', 'Inmutable', 'Colección', 'Objetos')
```

# Eliminación de una Tupla

No se pueden alterar los componentes de una tupla, como se mencionó anteriormente. Como resultado, no podemos deshacernos o eliminar los componentes de una tupla.

Sin embargo, una tupla se puede eliminar por completo con la palabra clave `del`.

**Código**

```python
# Programa de Python para mostrar cómo eliminar elementos de una tupla de Python

# Crear una tupla
tupla_ = ("Python", "Tupla", "Ordenada", "Inmutable", "Colección", "Objetos")

# Eliminar un elemento específico de la tupla
try:
    del tuple_[3]
    print(tuple_)
except Exception as e:
    print(e)

# Eliminar la variable de la memoria global del programa
del tuple_

# Intentar acceder a la tupla después de eliminarla
try:
    print(tuple_)
except Exception as e:
    print(e)
```

**Salida**

```bash
'tuple' object does not support item deletion
name 'tuple_' is not defined
```

# Repetición de Tuplas

**Código**

```python
# Programa de Python para mostrar la repetición en tuplas

tupla_ = ('Python', "Tuplas")
print("Tupla original:", tuple_)

# Repetir los elementos de la tupla
tupla_ = tupla_ * 3
print("Nueva tupla:", tupla_)
```

**Salida**

```bash
Tupla original: ('Python', 'Tuplas')
Nueva tupla: ('Python', 'Tuplas', 'Python', 'Tuplas', 'Python', 'Tuplas')
```

# Métodos de Tuplas

Las tuplas de Python son una colección de objetos inmutables similares a las listas. Python ofrece algunas formas de trabajar con tuplas. Estos dos enfoques se cubrirán en detalle en este artículo con la ayuda de algunos ejemplos.

A continuación se muestran ejemplos de estos métodos.

- Método `count()`

El método `count()` de las tuplas devuelve el número de veces que aparece el elemento especificado en la tupla.

**Código**

```python
# Crear tuplas
T1 = (0, 1, 5, 6, 7, 2, 2, 4, 2, 3, 2, 3, 1, 3, 2)
T2 = ('python', 'java', 'python', 'Tpoint', 'python', 'java')

# Contar la aparición de 3
res = T1.count(2)
print('Conteo de 2 en T1:', res)

# Contar la aparición de java
res = T2.count('java')
print('Conteo de Java en T2:', res)
```

**Salida**

```bash
Conteo de 2 en T1: 5
Conteo de Java en T2: 2
```

## Método index()

El método `index()` devuelve la primera aparición del elemento solicitado de la tupla.

**Parámetros:**

- Elemento a buscar.
- begin (opcional): el índice utilizado como punto de partida para la búsqueda.
- final (opcional): el último índice hasta el cual se realiza la búsqueda.

**Código**

```python
# Crear tuplas
Datos_tupla = (0, 1, 2, 3, 2, 3, 1, 3, 2)

# Obtener el índice de 3
res = Datos_tupla.index(3)
print('Primera aparición de 1 es', res)

# Obtener el índice de 3 después del cuarto
res = Datos_tupla.index(3, 4)
print('Primera aparición de 1 después del cuarto índice es:', res)
```

**Salida**

```bash
Primera aparición de 1 es 2
Primera aparición de 1 después del cuarto índice es: 6
```

# Prueba de Pertenencia a una Tupla

Utilizando la palabra clave `in`, podemos determinar si un elemento está presente en la tupla dada o no.

**Código**

```python
# Programa de Python para mostrar cómo realizar una prueba de pertenencia en tuplas

# Crear una tupla
tuple_ = ("Python", "Tupla", "Ordenada", "Inmutable", "Colección", "Ordenada")

# Operador in
print('Tupla' in tuple_)
print('Items' in tuple_)

# Operador not in
print('Inmutable' not in tuple_)
print('Items' not in tuple_)
```

**Salida**

```bash
True
False
False
True
```

# Iterar a Través de una Tupla

Podemos utilizar un bucle `for` para iterar a través de cada elemento de una tupla.

**Código**

```python
# Programa de Python para mostrar cómo iterar sobre los elementos de una tupla

# Crear una tupla
tupla_ = ("Python", "Tupla", "Ordenada", "Inmutable")

# Iterar sobre los elementos de la tupla utilizando un bucle for
for item in tuple_:
    print(item)
```

**Salida**

```bash
Python
Tupla
Ordenada
Inmutable
```

# Cambiando una Tupla

Las tuplas, a diferencia de las listas, son objetos inmutables.

Esto significa que no podemos cambiar los elementos de una tupla una vez que han sido definidos. Sin embargo, los elementos anidados de un elemento pueden cambiarse si el propio elemento es un tipo de datos modificable como una lista.

Una tupla se puede asignar a varios valores (reasignación).

**Código**

```python
# Programa de Python para mostrar que las tuplas de Python son objetos inmutables

# Crear una tupla
tupla_ = ("Python", "Tupla", "Ordenada", "Inmutable", [1, 2, 3, 4])

# Intentar cambiar el elemento en el índice 2
try:
    tupla_[2] = "Items"
    print(tupla_)
except Exception as e:
    print(e)

# Pero dentro de una tupla, podemos cambiar los elementos de un objeto mutable
tupla_[-1][2] = 10
print(tupla_)

# Cambiar toda la tupla
tupla_ = ("Python", "Items")
print(tupla_)
```

**Salida**

```bash
'tuple' object does not support item assignment
('Python', 'Tupla', 'Ordenada', 'Inmutable', [1, 2, 10, 4])
('Python', 'Items')
```

Para combinar múltiples tuplas, podemos utilizar el operador `+`. A esto se le llama concatenación.

También podemos repetir los elementos de una tupla un número específico de veces utilizando el operador `*`. Esto ya se muestra arriba.

Los resultados de las operaciones `+` y `*` son nuevas tuplas.

**Código**

```python
# Programa de Python para mostrar cómo concatenar tuplas

# Crear una tupla
tupla_ = ("Python", "Tupla", "Ordenada", "Inmutable")

# Agregar una tupla a la tupla_
print(tupla_ + (4, 5, 6))
```

**Salida**

```bash
('Python', 'Tupla', 'Ordenada', 'Inmutable', 4, 5, 6)
```

# Ventajas de las Tuplas en Comparación con las Listas

- Las tuplas tardan menos que las listas.
- El código está protegido contra cambios accidentales gracias a las tuplas. Si un programa requiere que los datos no cambien, es mejor almacenarlos en **"tuplas"** en lugar de **"listas"**.
- Si una tupla incluye valores inmutables como cadenas, números u otra tupla, se puede utilizar como clave de un diccionario. Como las **"listas"** son mutables, no se pueden utilizar como claves de diccionario.
