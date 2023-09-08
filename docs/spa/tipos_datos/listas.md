# Listas

En Python, la secuencia de varios tipos de datos se almacena en una lista. Una lista es una colección de diferentes tipos de valores o elementos. Dado que las listas en Python son mutables, podemos cambiar sus elementos después de crearlas. La coma (,) y los corchetes cuadrados [encerrar los elementos de la lista] sirven como separadores.

Aunque seis tipos de datos de Python pueden contener secuencias, la Lista es la forma más común y confiable. Una lista, un tipo de dato de secuencia, se utiliza para almacenar la colección de datos. Las tuplas y las cadenas de texto son dos formatos de datos similares para secuencias.

Las listas escritas en Python son idénticas a los arrays escalados dinámicamente definidos en otros lenguajes, como ArrayList en Java y Vector en C++. Una lista es una colección de elementos separados por comas y denotados por el símbolo [].

## Declaración de Lista

**Ejemplo**:

```python
# una lista simple

lista1 = [1, 2, "Python", "Programa", 15.9]
lista2 = ["Amy", "Ryan", "Henry", "Emma"]

# imprimir la lista

print(lista1)
print(lista2)

# imprimir el tipo de lista

print(type(lista1))
print(type(lista2))
```

**Salida**:

```python
[1, 2, 'Python', 'Programa', 15.9]
['Amy', 'Ryan', 'Henry', 'Emma']
< class ' list ' >
< class ' list ' >
```

## Características de las Listas

Las características de la lista son las siguientes:

- Las listas están ordenadas.
- Se puede acceder al elemento de la lista mediante el índice.
- El tipo mutable de la lista es...
- Las listas son tipos de datos modificables.
- Se pueden almacenar varios elementos diferentes en una lista.

### Comprobación de Lista Ordenada

**Ejemplo**:

```python
# ejemplo

a = [1, 2, "Ram", 3.50, "Rahul", 5, 6]
b = [1, 2, 5, "Ram", 3.50, "Rahul", 6]
a == b
```

**Salida**:

```python
False
```

Los componentes idénticos se encontraban en las dos listas, pero la segunda lista cambió la posición del quinto componente, lo que va en contra del orden previsto de las listas. Se devuelve False cuando se comparan las dos listas.

**Ejemplo**:

```python
# ejemplo

a = [1, 2, "Ram", 3.50, "Rahul", 5, 6]
b = [1, 2, "Ram", 3.50, "Rahul", 5, 6]
a == b
```

**Salida**:

```python
True
```

Las listas preservan la estructura de los componentes. Debido a esto, es una colección ordenada de elementos.

Vamos a examinar con más detalle el ejemplo de lista.

**Ejemplo**:

```python
# ejemplo de lista en detalle

empleado = ["John", 102, "USA"]
Dep1 = ["CS", 10]
Dep2 = ["IT", 11]
HOD_CS = [10, "Sr. Holding"]
HOD_IT = [11, "Sr. Bewon"]

print("imprimiendo datos del empleado...")
print(" Nombre : %s, ID: %d, País: %s" % (empleado[0], empleado[1], empleado[2]))
print("imprimiendo departamentos...")
print("Departamento 1:\\nNombre: %s, ID: %d\\nDepartamento 2:\\nNombre: %s, ID: %s" % (Dep1[0], Dep2[1], Dep2[0], Dep2[1]))
print("Detalles del jefe de departamento...")
print("Jefe de CS: %s, ID: %d" % (HOD_CS[1], HOD_CS[0]))
print("Jefe de IT: %s, ID: %d" % (HOD_IT[1], HOD_IT[0]))
print(type(empleado), type(Dep1), type(Dep2), type(HOD_CS), type(HOD_IT))
```

**Salida**:

```python
imprimiendo datos del empleado...
Nombre : John, ID: 102, País: USA
imprimiendo departamentos...
Departamento 1:
Nombre: CS, ID: 11
Departamento 2:
Nombre: IT, ID: 11
Detalles del jefe de departamento...
Jefe de CS: Sr. Holding, ID: 10
Jefe de IT: Sr. Bewon, ID: 11
<class ' list '> <class ' list '> <class ' list '> <class ' list '> <class ' list '>
```

En la ilustración anterior, imprimimos los detalles específicos del empleado y del departamento a partir de las listas que hemos creado. Para comprender mejor el concepto de la lista, revisa el código anterior.

## Indexación y división de listas

El procedimiento de indexación se lleva a cabo de manera similar al procesamiento de cadenas de texto. El operador de segmento [] se puede usar para acceder a los componentes de la lista.

El índice varía de 0 a longitud - 1. El índice 0 es donde se almacena el primer elemento de la lista; el índice 1 es donde se almacena el segundo elemento, y así sucesivamente.

Podemos obtener la sublista de la lista utilizando la siguiente sintaxis.

```python
lista_variable(inicio:fin:paso)
```

- El inicio indica la posición del registro inicial de la lista.
- El fin indica la última posición del registro de la lista.
- Con un valor para inicio, el paso se utiliza para saltar el enésimo elemento: stop.

El parámetro de inicio es el índice inicial, el parámetro de paso es el índice final y el valor del parámetro de fin es el número de elementos que se "saltan". El valor predeterminado para el paso es uno sin un valor específico. Dentro de la Sublista resultante, estarán disponibles los elementos desde el inicio del registro, pero no el que tiene el fin de archivo. El primer elemento de una lista tiene un índice de cero.

**Ejemplo**:

```python
lista = [1, 2, 3, 4, 5, 6, 7]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Dividiendo los elementos

print(lista[0:6])

# Por defecto, el valor del índice es 0, así que comienza desde el primer elemento y va hasta el índice -1.

print(lista[:])
print(lista[2:5])
print(lista[1:6:2])
```

**Salida**:

```python
1
2
3
4
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[3, 4, 5]
[2, 4, 6]
```

A diferencia de otros lenguajes de programación, Python también te permite usar la indexación negativa. Los índices negativos se cuentan desde la derecha. El índice -1 representa el último elemento en el lado derecho de la lista, seguido del índice -2 para el siguiente miembro a la izquierda, y así sucesivamente, hasta llegar al último elemento a la izquierda.

Echemos un vistazo al siguiente ejemplo, donde utilizaremos la indexación negativa para acceder a los elementos de la lista.

**Ejemplo**:

```python
# ejemplo de indexación negativa

lista = [1, 2, 3, 4, 5]

print(lista[-1])
print(lista[-3:])
print(lista[:-1])
print(lista[-3:-1])
```

**Salida**:

```python
5
[3, 4, 5]
[1, 2, 3, 4]
[3, 4]
```

La indexación negativa nos permite obtener un elemento, como se mencionó anteriormente. El primer print devuelve el elemento más a la derecha de la lista. El segundo print devuelve la sublista, y así sucesivamente.

## Actualización de Valores de la Lista

Debido a su mutabilidad y a la capacidad del operador de segmento y asignación para actualizar sus valores, las listas son la estructura de datos más versátil en Python. Los métodos append() e insert() de Python también pueden agregar valores a una lista.

Considera el siguiente ejemplo para actualizar los valores dentro de la lista.

**Ejemplo**:

```python
# actualizando valores de lista

lista = [1, 2, 3, 4, 5, 6]

print(lista)

# Asignará el valor al segundo índice

lista[2] = 10

print(lista)

# Agregando varios elementos

lista[1:3] = [89, 78]

print(lista)

# Agregará el valor al final de la lista

lista[-1] = 25

print(lista)
```

**Salida**:

```python
[1, 2, 3, 4, 5, 6]
[1, 2, 10, 4, 5, 6]
[1, 89, 78, 4, 5, 6]
[1, 89, 78, 4, 5, 25]
```

Los elementos de la lista también se pueden eliminar utilizando la palabra clave **del**. Python también nos proporciona el método **remove()** si no sabemos qué elemento se va a eliminar de la lista.

Considera el siguiente ejemplo para eliminar elementos de la lista.

**Ejemplo**:

```python
lista = [1, 2, 3, 4, 5, 6]

print(lista)

# Eliminará el valor del segundo índice

del lista[2]

print(lista)

# Eliminará los elementos de la lista que tienen índices 1 y 2

del lista[1:3]

print(lista)

# Eliminará el valor del último índice de la lista

del lista[-1]

print(lista)
```

**Salida**:

```python
[1, 2, 3, 4, 5, 6]
[1, 2, 4, 5, 6]
[1, 5, 6]
[1, 5]
```

## Operaciones con Listas

Los operadores de concatenación (+) y repetición (*) funcionan de la misma manera que con las cadenas de texto. Las diferentes operaciones con listas son:

1. Repetición
2. Concatenación
3. Longitud
4. Iteración
5. Pertinencia (Membresía)

Veamos cómo responde la lista a varios operadores.

### 1. Repetición

El operador de repetición permite que los elementos de la lista se repitan varias veces.

**Ejemplo**:

```python
# repetición de una lista

# declarando la lista

lista1 = [12, 14, 16, 18, 20]

# operador de repetición *

l = lista1 * 2

print(l)
```

**Salida**:

```python
[12, 14, 16, 18, 20, 12, 14, 16, 18, 20]
```

### 2. Concatenación

Concatena dos listas mencionadas a ambos lados del operador.

**Ejemplo**:

```python
# concatenación de dos listas

# declarando las listas

lista1 = [12, 14, 16, 18, 20]

lista2 = [9, 10, 32, 54, 86]

# operador de concatenación +

l = lista1 + lista2

print(l)
```

**Salida**:

```python
[12, 14, 16, 18, 20, 9, 10, 32, 54, 86]
```

### 3. Longitud

Se utiliza para obtener la longitud de la lista.

**Ejemplo**:

```python
# tamaño de la lista

# declarando la lista

lista1 = [12, 14, 16, 18, 20, 23, 27, 39, 40]

# encontrar la longitud de la lista

len(lista1)
```

**Salida**:

```python
9
```

### 4. Iteración

El bucle for se utiliza para iterar sobre los elementos de la lista.

**Ejemplo**:

```python
# iteración de la lista

# declarando la lista

lista1 = [12, 14, 16, 39, 40]

# iterando

for i in lista1:
    print(i)
```

**Salida**:

```python
12
14
16
39
40
```

### 5. Pertinencia (Membresía)

Devuelve verdadero (True) si un elemento específico existe en una lista determinada, de lo contrario, devuelve falso (False).

**Ejemplo**:

```python
# pertenencia en la lista

# declarando la lista

lista1 = [100, 200, 300, 400, 500]

# se imprimirá verdadero (True) si el valor existe

# y falso (False) si no

print(600 in lista1)
print(700 in lista1)
print(1040 in lista1)
print(300 in lista1)
print(100 in lista1)
print(500 in lista1)
```

**Salida**:

```python
False
False
False
True
True
True
```

## Iterando una Lista

Una lista puede iterarse utilizando un bucle for-in. Una lista simple que contiene cuatro cadenas, se puede iterar de la siguiente manera.

**Ejemplo**:

```python
# iterando una lista

lista = ["John", "David", "James", "Jonathan"]

for i in lista:
    # La variable i iterará sobre los elementos de la lista y contendrá cada elemento en cada iteración.
    print(i)
```

**Salida**:

```python
John
David
James
Jonathan
```

## Añadiendo Elementos a la Lista

La función append() en Python puede agregar un nuevo elemento a la lista. Además, la función append() puede añadir elementos al final de la lista.

Considera el siguiente ejemplo, donde tomamos los elementos de la lista del usuario e imprimimos la lista en la consola.

**Ejemplo**:

```python
# Declarando una lista vacía

l = []

# El número de elementos será ingresado por el usuario

n = int(input("Ingresa el número de elementos en la lista: "))

# Bucle for para tomar la entrada del usuario

for i in range(0, n):

    # El elemento es tomado del usuario y añadido a la lista como un elemento

    l.append(input("Ingresa el elemento: "))

print("Imprimiendo los elementos de la lista...")

# Bucle de recorrido para imprimir los elementos de la lista

for i in l:
    print(i, end=" ")
```

**Salida**:

```python
Ingresa el número de elementos en la lista: 10
Ingresa el elemento: 32
Ingresa el elemento: 56
Ingresa el elemento: 81
Ingresa el elemento: 2
Ingresa el elemento: 34
Ingresa el elemento: 65
Ingresa el elemento: 9
Ingresa el elemento: 66
Ingresa el elemento: 12
Ingresa el elemento: 18
Imprimiendo los elementos de la lista...
32 56 81 2 34 65 9 66 12 18
```

## Eliminando Elementos de la Lista

La función remove() en Python puede eliminar un elemento de la lista. Para entender este concepto, veamos el siguiente ejemplo.

**Ejemplo**:

```python
lista = [0, 1, 2, 3, 4]

print("Imprimiendo la lista original: ")

for i in lista:
    print(i, end=" ")

lista.remove(2)

print("\\nImprimiendo la lista después de eliminar el primer elemento...")

for i in lista:
    print(i, end=" ")
```

**Salida**:

```python
Imprimiendo la lista original:
0 1 2 3 4
Imprimiendo la lista después de eliminar el primer elemento...
0 1 3 4
```

## Funciones Integradas de Listas

Python proporciona las siguientes funciones integradas, que se pueden utilizar con listas.

1. len()
2. max()
3. min()

### len()

Se utiliza para calcular la longitud de la lista.

**Ejemplo**:

```python
# tamaño de la lista

# declarando la lista

lista1 = [12, 16, 18, 20, 39, 40]

# encontrar la longitud de la lista

len(lista1)
```

**Salida**:

```python
6
```

### max()

Devuelve el elemento máximo de la lista.

**Ejemplo**:

```python
# máximo de la lista

lista1 = [103, 675, 321, 782, 200]

# elemento más grande en la lista

print(max(lista1))
```

**Salida**:

```python
782
```

### min( )

Devuelve el elemento mínimo de la lista.

**Ejemplo**:

```python
# mínimo de la lista

lista1 = [103, 675, 321, 782, 200]

# elemento más pequeño en la lista

print(min(lista1))
```

**Salida**:

```python
103
```

Echemos un vistazo a algunos ejemplos de listas.

**Ejemplo 1**: Crear un programa para eliminar los elementos duplicados de una lista.

```python
lista1 = [1, 2, 2, 3, 55, 98, 65, 65, 13, 29]

# Declarar una lista vacía que almacenará los valores únicos

lista2 = []

for i in lista1:
    if i not in lista2:
        lista2.append(i)

print(lista2)
```

**Salida**:

```python
[1, 2, 3, 55, 98, 65, 13, 29]
```

**Ejemplo 2:** Crear un programa para calcular la suma de los elementos de una lista.

```python
lista1 = [3, 4, 5, 9, 10, 12, 24]

suma = 0

for i in lista1:
    suma = suma + i

print("La suma es:", suma)
```

**Salida**:

```python
La suma es: 67
```

**Ejemplo 3**: Crear un programa para encontrar los elementos comunes entre dos listas.

```python
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [7, 8, 9, 2, 10]

for x in lista1:
    for y in lista2:
        if x == y:
            print("El elemento común es:", x)
```

**Salida**:

```python
El elemento común es: 2
```
