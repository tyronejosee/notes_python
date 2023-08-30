# Tipos de Datos

Cada valor tiene un tipo de dato, y las variables pueden contener valores. Python es un lenguaje poderosamente compuesto; por lo tanto, no es necesario definir el tipo de variable al declararla. El intérprete enlaza implícitamente el valor a su tipo.

**Sintaxis**:

```python
a = 5
```

No especificamos el tipo de la variable `a`, que tiene el valor cinco de tipo entero (int). El intérprete de Python interpretará automáticamente la variable como un entero.

Podemos verificar el tipo de una variable utilizada en el programa gracias a Python. La función `type()` en Python devuelve el tipo de la variable pasada.

Consideremos la siguiente ilustración al definir y verificar los valores de varios tipos de datos.

**Ejemplo**:

```python
a = 10
b = "Hola Python"
c = 10.5

print(type(a))
print(type(b))
print(type(c))
```

**Salida**:

```bash
<class 'int'>
<class 'str'>
<class 'float'>
```

## Tipos de Datos Estándar

Una variable puede contener una variedad de valores. Por otro lado, la identificación de una persona debe almacenarse como un número entero, mientras que su nombre debe almacenarse como una cadena.

Python especifica el método de almacenamiento para cada uno de los tipos de datos estándar que proporciona. A continuación se presenta una lista de los tipos de datos definidos en Python.

1. Números
2. Tipos de secuencia
3. Booleano
4. Conjunto
5. Diccionario

![https://static.javatpoint.com/python/images/python-data-types.png](https://static.javatpoint.com/python/images/python-data-types.png)

Los tipos de datos se discutirán brevemente en esta sección del tutorial. Hablaremos exhaustivamente sobre cada uno de ellos más adelante en este tutorial.

### Números

Los valores numéricos se almacenan en números. Los valores enteros, de punto flotante y complejos pertenecen al tipo de datos Numbers de Python. Python ofrece la función `type()` para determinar el tipo de una variable. La función `isinstance()` se utiliza para comprobar si un objeto pertenece a una clase específica.

Cuando se asigna un número a una variable, Python genera objetos de tipo Number.

**Ejemplo**:

```python
a = 5
print("El tipo de a es", type(a))

b = 40.5
print("El tipo de b es", type(b))

c = 1+3j
print("El tipo de c es", type(c))
print("c es un número complejo", isinstance(1+3j, complex))
```

**Salida**:

```bash
El tipo de a es <class 'int'>
El tipo de b es <class 'float'>
El tipo de c es <class 'complex'>
c es un número complejo: True
```

Python admite tres tipos de datos numéricos:

- **Int**: Puede ser cualquier número entero de cualquier longitud, como 10, 2, 29, -20, -150, etc. En Python, un entero puede tener la longitud que desees. Su valor pertenece al tipo `int`.
- **Float**: Almacena números de punto flotante como 1.9, 9.902, 15.2, etc. Puede ser preciso hasta 15 decimales.
- **Complejo**: Un número complejo contiene un par ordenado, es decir, x + yi, donde x e y representan las partes reales e imaginarias respectivamente. Los números complejos son como 2.14j, 2.0 + 2.3j, etc.

### Tipos de Secuencia

### Cadena (String)

La secuencia de caracteres entre comillas se puede utilizar para describir una cadena. Una cadena se puede definir en Python utilizando comillas simples, dobles o triples.

El manejo de cadenas en Python es una tarea sencilla ya que Python proporciona funciones y operadores incorporados para realizar tareas con cadenas.

Cuando trabajamos con cadenas, la operación `"hola" + "python"` devuelve `"hola python"`, y el operador `+` se utiliza para concatenar dos cadenas.

Como la operación `"Python" * 2` devuelve `"PythonPython"`, el operador `*` se refiere como operador de repetición.

El siguiente ejemplo muestra el uso de cadenas.

**Ejemplo**:

```python
cadena = "cadena usando comillas dobles"
print(cadena)

s = '''Una cadena
de varias líneas'''
print(s)
```

**Salida**:

```bash
cadena usando comillas dobles
Una cadena
de varias líneas
```

Veamos la siguiente ilustración sobre el manejo de cadenas.

**Ejemplo**:

```python
str1 = 'hola javatpoint' # cadena str1
str2 = ' cómo estás' # cadena str2

print (str1[0:2]) # imprimiendo los dos primeros caracteres usando el operador de división
print (str1[4]) # imprimiendo el cuarto carácter de la cadena
print (str1 * 2) # imprimiendo la cadena dos veces
print (str1 + str2) # imprimiendo la concatenación de str1 y str2
```

**Salida**:

```bash
ho
a
hola javatpointhola javatpoint
hola javatpoint cómo estás
```

### Lista (List)

Las listas en Python son similares a los arrays en C, pero las listas pueden contener datos de diferentes tipos. Los elementos almacenados en la lista se separan con comas (,) y están encerrados entre corchetes [].

Para acceder a los datos de la lista, podemos usar los operadores de división [:]. Al igual que funcionan con las cadenas, la lista se maneja mediante el operador de concatenación (+) y el operador de repetición (*).

**Ejemplo**:

```python
lista1 = [1, "hola", "Python", 2]

# Verificando el tipo de lista dada
print(type(lista1))

# Imprimiendo la lista1
print(lista1)

# División de la lista
print(lista1[3:])

# División de la lista
print(lista1[0:2])

# Concatenación de lista usando el operador +
print(lista1 + lista1)

# Repetición de lista usando el operador *
print(lista1 * 3)
```

**Salida**:

```bash
<class 'list'>
[1, 'hola', 'Python', 2]
[2]
[1, 'hola']
[1, 'hola', 'Python', 2, 1, 'hola', 'Python', 2]
[1, 'hola', 'Python', 2, 1, 'hola', 'Python', 2, 1, 'hola', 'Python', 2]
```

### Tupla (Tuple)

En muchos sentidos, una tupla es como una lista. Las tuplas, al igual que las listas, también contienen una colección de elementos de diferentes tipos de datos. Los elementos de la tupla se separan con un espacio en paréntesis ().

Debido a que no podemos alterar el tamaño o el valor de los elementos en una tupla, es una estructura de datos de solo lectura.

**Ejemplo**:

```python
tupla = ("hola", "Python", 2)

# Verificando el tipo de tupla
print(type(tupla))

# Imprimiendo la tupla
print(tupla)

# División de la tupla
print(tupla[1:])
print(tupla[0:1])

# Concatenación de tupla usando el operador +
print(tupla + tupla)

# Repetición de tupla usando el operador *
print(tupla * 3)

# Agregando un valor a la tupla. Esto generará un error.
tupla[2] = "hola"
```

**Salida**:

```bash
<class 'tuple'>
('hola', 'Python', 2)
('Python', 2)
('hola',)
('hola', 'Python', 2, 'hola', 'Python', 2)
('hola', 'Python', 2, 'hola', 'Python', 2, 'hola', 'Python', 2)

Traceback (most recent call last):
  File "main.py", line 14, in <module>
    tupla[2] = "hola";
TypeError: 'tuple' object does not support item assignment
```

### Diccionario (Dictionary)

Un diccionario es un conjunto de pares clave-valor organizados sin ningún orden en particular. Almacena un valor específico para cada clave, similar a un array asociativo o una tabla hash. El valor es cualquier objeto de Python, mientras que la clave puede contener cualquier tipo de dato primitivo.

Los elementos del diccionario se separan con comas (,) y se encierran entre llaves {}.

**Ejemplo**:

```python
d = {1: 'Jimmy', 2: 'Alex', 3: 'John', 4: 'Mike'}

# Imprimiendo el diccionario
print(d)

# Accediendo al valor mediante las claves
print("El primer nombre es " + d[1])
print("El cuarto nombre es " + d[4])

# Imprimiendo las claves del diccionario
print(d.keys())

# Imprimiendo los valores del diccionario
print(d.values())
```

**Salida**:

```bash
{1: 'Jimmy', 2: 'Alex', 3: 'John', 4: 'Mike'}
El primer nombre es Jimmy
El cuarto nombre es Mike
dict_keys([1, 2, 3, 4])
dict_values(['Jimmy', 'Alex', 'John', 'Mike'])
```

### Booleano (Boolean)

Verdadero (True) y Falso (False) son los dos valores predeterminados para el tipo de datos Booleano. Estos valores se utilizan para evaluar la veracidad o falsedad de una afirmación dada. Esto se indica en la clase Booleana. Falso se puede representar con el 0 o la letra "F", mientras que Verdadero se puede representar con cualquier valor que no sea cero.

**Ejemplo**:

```python
# Programa de Python para verificar el tipo booleano
print(type(True))
print(type(False))
print(false)
```

**Salida**:

```bash
<class 'bool'>
<class 'bool'>
NameError: name 'false' is not defined
```

### Conjunto (Set)

El tipo de datos de conjunto de Python es una colección no ordenada. Es iterable, mutable (puede cambiar después de su creación) y tiene elementos únicos. Los elementos de un conjunto no tienen un orden establecido; puede devolver los elementos en un orden modificado. Para crear el conjunto se pasa una secuencia de elementos entre llaves {} y separados por comas, o se utiliza la función incorporada `set()`. Puede contener diferentes tipos de valores.

**Ejemplo**:

```python
# Creando un conjunto vacío
conjunto1 = set()

conjunto2 = {'James', 2, 3, 'Python'}

# Imprimiendo el valor del conjunto
print(conjunto2)

# Agregando un elemento al conjunto
conjunto2.add(10)
print(conjunto2)

# Eliminando un elemento del conjunto
conjunto2.remove(2)
print(conjunto2)
```

**Salida**:

```bash
{3, 'Python', 'James', 2}
{'Python', 'James', 3, 2, 10}
{'Python', 'James', 3, 10}
```

Con esto, hemos cubierto los diferentes tipos de datos en Python y cómo se utilizan. Cada tipo de dato tiene sus propias características y utilidades específicas en la programación. Puedes utilizar estos tipos de datos para realizar cálculos, almacenar información y manipular datos de diversas formas en tus programas de Python.
