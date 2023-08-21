# Diccionarios

Los diccionarios son una estructura de datos útil para almacenar información en Python, ya que son capaces de imitar arreglos de datos del mundo real donde existe un valor determinado para una clave dada.

Los datos se almacenan como pares clave-valor utilizando un diccionario de Python.

- Esta estructura de datos es mutable.
- Los componentes del diccionario están hechos utilizando claves y valores.
- Las claves deben tener solo un componente.
- Los valores pueden ser de cualquier tipo, incluidos enteros, listas y tuplas.

Un diccionario es, en otras palabras, un grupo de pares clave-valor, donde los valores pueden ser cualquier objeto de Python. Las claves, en cambio, son objetos Python inmutables, como cadenas, tuplas o números. Las entradas del diccionario están ordenadas desde la versión de Python 3.7. En Python 3.6 y versiones anteriores, los diccionarios son generalmente desordenados.

## Creación de Diccionarios

Las llaves de llaves (corchetes) son la forma más sencilla de generar un diccionario de Python, aunque también hay otros enfoques posibles. Con muchos pares clave-valor rodeados de llaves y dos puntos que separan cada clave de su valor, se puede construir el diccionario. (:). Lo siguiente muestra la sintaxis para definir el diccionario.

**Sintaxis:**

```python
Diccionario = {"Nombre": "Gayle", "Edad": 25}
```

En el diccionario anterior, las claves "Nombre" y "Edad" son cadenas que pertenecen a la categoría de objeto inmutable.

Veamos un ejemplo para crear un diccionario e imprimir su contenido.

**Ejemplo:**

```python
Empleado = {"Nombre": "Johnny", "Edad": 32, "salario": 26000, "Compañía": "^TCS"}

print(type(Empleado))

print("Imprimiendo datos del Empleado .... ")

print(Empleado)
```

**Salida:**

```python
<class 'dict'>
Imprimiendo datos del Empleado ....
{'Nombre': 'Johnny', 'Edad': 32, 'salario': 26000, 'Compañía': 'TCS'}
```

Python nos proporciona la función incorporada **dict()**, que también se utiliza para crear un diccionario.

Las llaves vacías {} se utilizan para crear un diccionario vacío.

**Ejemplo:**

```python
# Creando un diccionario vacío
Diccionario = {}

print("Diccionario vacío: ")

print(Diccionario)

# Creando un diccionario con el método dict()
Diccionario = dict({1: 'Hcl', 2: 'WIPRO', 3:'Facebook'})

print("\\nCrear un diccionario usando dict(): ")

print(Diccionario)

# Creando un diccionario con cada elemento como par
Diccionario = dict([(4, 'Rinku'), (2, Singh)])

print("\\nDiccionario con cada elemento como par: ")

print(Diccionario)
```

**Salida:**

```python
Diccionario vacío:
{}

Crear un diccionario usando dict():
{1: 'Hcl', 2: 'WIPRO', 3: 'Facebook'}

Diccionario con cada elemento como par:
{4: 'Rinku', 2: 'Singh'}
```

## Acceso a los valores del diccionario

Para acceder a los datos contenidos en listas y tuplas, se ha estudiado la indexación. Las claves del diccionario se pueden utilizar para obtener los valores porque son únicas entre sí. El siguiente método se puede utilizar para acceder a los valores del diccionario.

**Ejemplo:**

```python
Empleado = {"Nombre": "Dev", "Edad": 20, "salario": 45000, "Compañía": "WIPRO"}

print(type(Empleado))

print("Imprimiendo datos del Empleado .... ")

print("Nombre: %s" % Empleado["Nombre"])

print("Edad: %d" % Empleado["Edad"])

print("Salario: %d" % Empleado["salario"])

print("Compañía: %s" % Empleado["Compañía"])
```

**Salida:**

```python
<class 'dict'>
Imprimiendo datos del Empleado ....
Nombre : Dev
Edad : 20
Salario : 45000
Compañía : WIPRO
```

Python nos proporciona una alternativa para usar el método get() para acceder a los valores del diccionario. Esto daría el mismo resultado que el índice.

## Agregando valores al diccionario

El diccionario es un tipo de datos mutable y utilizando las claves adecuadas se pueden cambiar sus valores. Dict[key] = value y el valor pueden modificarse. También se puede actualizar un valor existente utilizando el método update().

> Nota: El valor se actualiza si el par clave-valor ya está presente en el diccionario. De lo contrario, se agregan nuevas claves al diccionario.
> 

Veamos un ejemplo para actualizar los valores del diccionario.

**Ejemplo:**

```python
# Creando un diccionario vacío
Diccionario = {}

print("Diccionario vacío: ")

print(Diccionario)

# Agregando elementos al diccionario uno por uno

Diccionario[0] = 'Peter'

Diccionario[2] = 'Joseph'

Diccionario[3] = 'Ricky'

print("\\nDiccionario después de agregar 3 elementos: ")

print(Diccionario)

# Agregando un conjunto de valores con una sola clave
# Emp_ages no existe en el diccionario

Diccionario['Emp_ages'] = 20, 33, 24

print("\\nDiccionario después de agregar 3 elementos: ")

print(Diccionario)

# Actualizando el valor de una clave existente

Diccionario[3] = 'JavaTpoint'

print("\\nValor de clave actualizado: ")

print(Diccionario)
```

**Salida:**

```python
Diccionario vacío:
{}

Diccionario después de agregar 3 elementos:
{0: 'Peter', 2: 'Joseph', 3: 'Ricky'}

Diccionario después de agregar 3 elementos:
{0: 'Peter', 2: 'Joseph', 3: 'Ricky', 'Emp_ages': (20, 33, 24)}

Valor de clave actualizado:
{0: 'Peter', 2: 'Joseph', 3: 'JavaTpoint', 'Emp_ages': (20, 33, 24)}
```

**Ejemplo:**

```python
Empleado = {"Nombre": "Dev", "Edad": 20, "

salario": 45000, "Compañía": "WIPRO"}

print(type(Empleado))

print("Imprimiendo datos del Empleado .... ")

print(Empleado)

print("Ingrese los detalles del nuevo empleado....");

Empleado["Nombre"] = input("Nombre: ");

Empleado["Edad"] = int(input("Edad: "));

Empleado["salario"] = int(input("Salario: "));

Empleado["Compañía"] = input("Compañía: ");

print("Imprimiendo los nuevos datos");

print(Empleado)
```

**Salida:**

```python
<class 'dict'>
Imprimiendo datos del Empleado ....
Empleado = {"Nombre": "Dev", "Edad": 20, "salario": 45000, "Compañía": "WIPRO"} Ingrese los detalles del nuevo empleado....
Nombre: Sunny
Edad: 38
Salario: 39000
Compañía:Hcl
Imprimiendo los nuevos datos
{'Nombre': 'Sunny', 'Edad': 38, 'salario': 39000, 'Compañía': 'Hcl'}
```

## Eliminando elementos con la palabra clave "del"

Los elementos del diccionario se pueden eliminar utilizando la palabra clave **del** de la siguiente manera:

**Ejemplo:**

```python
Empleado = {"Nombre": "David", "Edad": 30, "salario": 55000, "Compañía": "WIPRO"}

print(type(Empleado))

print("Imprimiendo datos del Empleado .... ")

print(Empleado)

print("Eliminando algunos de los datos del empleado")

del Empleado["Nombre"]

del Empleado["Compañía"]

print("Imprimiendo la información modificada")

print(Empleado)

print("Eliminando el diccionario: Empleado");

del Empleado

print("Intentemos imprimirlo de nuevo");

print(Empleado)
```

**Salida:**

```python
<class 'dict'>
Imprimiendo datos del Empleado ....
{'Nombre': 'David', 'Edad': 30, 'salario': 55000, 'Compañía': 'WIPRO'}
Eliminando algunos de los datos del empleado
Imprimiendo la información modificada
{'Edad': 30, 'salario': 55000}
Eliminando el diccionario: Empleado
Intentemos imprimirlo de nuevo
NameError: name 'Empleado' is not defined.
```

La última instrucción de impresión en el código anterior generó un error porque intentamos imprimir el diccionario Empleado que ya fue eliminado.

## Eliminando Elementos con el Método "pop()"

Un diccionario es un grupo de pares clave-valor en Python. Puede recuperar, insertar y eliminar elementos utilizando este tipo de datos desordenado y mutable mediante el uso de sus claves. El método pop() es una de las formas de eliminar elementos de un diccionario de Python. En esta publicación, hablaremos sobre cómo eliminar elementos de un diccionario de Python utilizando el método pop().

El valor asociado a una clave específica en un diccionario se elimina utilizando el método pop(), que luego devuelve el valor. El único argumento necesario es la clave del elemento que se va a eliminar. El método pop() se puede utilizar de las siguientes formas:

**Ejemplo:**

```python
# Método del diccionario

Diccionario1 = {1: 'JavaTpoint', 2: 'Educational', 3: 'Website'}

# Eliminando una clave usando el método pop()
clave_eliminada = Diccionario1.pop(2)

print(Diccionario1)
```

**Salida:**

```python
{1: 'JavaTpoint', 3: 'Website'}
```

Además, Python ofrece las funciones incorporadas popitem() y clear() para eliminar elementos del diccionario. A diferencia del método clear(), que elimina todos los elementos de todo el diccionario, popitem() elimina cualquier elemento de un diccionario.

## Iterando el Diccionario

Un diccionario se puede recorrer utilizando un bucle for de la siguiente manera:

**Ejemplo:**

```python
# Bucle for para imprimir todas las claves de un diccionario

Empleado = {"Nombre": "John", "Edad": 29, "salario": 25000, "Compañía": "WIPRO"}

for x in Empleado:
    print(x)
```

**Salida:**

```python
Nombre
Edad
salario
Compañía
```

**Ejemplo:**

```python
# Bucle for para imprimir todos los valores del diccionario

Empleado = {"Nombre": "John", "Edad": 29, "salario": 25000, "Compañía": "WIPRO"}

for x in Empleado:
    print(Empleado[x])
```

**Salida:**

```python
John
29
25000
WIPRO
```

**Ejemplo:**

```python
# Bucle for para imprimir los valores del diccionario utilizando el método values()

Empleado = {"Nombre": "John", "Edad": 29, "salario": 25000, "Compañía": "WIPRO"}

for x in Empleado.values():
    print(x)
```

**Salida:**

```python
John
29
25000
WIPRO
```

**Ejemplo:**

```python
# Bucle for para imprimir los elementos del diccionario utilizando el método items()

Empleado = {"Nombre": "John", "Edad": 29, "salario": 25000, "Compañía": "WIPRO"}

for x in Empleado.items():
    print(x)
```

**Salida:**

```python
('Nombre', 'John')
('Edad', 29)
('salario', 25000)
('Compañía', 'WIPRO')
```

## Propiedades de las Claves del Diccionario

1. En el diccionario, no podemos almacenar múltiples valores para las mismas claves. Si pasamos más de un valor para una sola clave, entonces se considera que el último valor asignado es el valor de la clave.

**Ejemplo:**

```python
Empleado = {"Nombre": "John", "Edad": 29, "salario": 25000, "Compañía": "WIPRO", "Nombre": "John"}

for x, y in Empleado.items():
    print(x, y)
```

**Salida:**

```python
Nombre John
Edad 29
salario 25000
Compañía WIPRO
```

1. La clave no puede pertenecer a ningún objeto mutable en Python. Se pueden utilizar números, cadenas o tuplas como clave, pero objetos mutables como listas no se pueden utilizar como clave en un diccionario.

**Ejemplo:**

```python
Empleado = {"Nombre": "John", "Edad": 29, "salario": 25000, "Compañ

ía": "WIPRO", [100,201,301]: "ID de Departamento"}

for x, y in Empleado.items():
    print(x, y)
```

**Salida:**

```python
Traceback (most recent call last):
  File "dictionary.py", line 1, in
    Empleado = {"Nombre": "John", "Edad": 29, "salario":25000,"Compañía":"WIPRO",[100,201,301]:"Department ID"}
TypeError: unhashable type: 'list'
```

## Funciones Incorporadas del Diccionario

Una función es un método que se puede utilizar en una construcción para obtener un valor. Además, la construcción no se altera. Unas pocas de las funciones de Python se pueden combinar con un diccionario de Python.

A continuación se presentan los métodos incorporados del diccionario de Python, junto con una breve descripción.

- **len()**

La función len() devuelve la longitud del diccionario de Python. La cadena se alarga por cada par clave-valor.

**Ejemplo:**

```python
diccionario = {1: "Ayan", 2: "Bunny", 3: "Ram", 4: "Bheem"}

len(diccionario)
```

**Salida:**

```python
4
```

- **any()**

Al igual que hace con listas y tuplas, el método any() devuelve True si realmente hay una clave de diccionario que tiene una expresión booleana que se evalúa como True.

**Ejemplo:**

```python
diccionario = {1: "Ayan", 2: "Bunny", 3: "Ram", 4: "Bheem"}

any({'':'','':'','3':''})
```

**Salida:**

```python
True
```

- **all()**

A diferencia del método any(), all() solo devuelve True si cada una de las claves del diccionario contiene un valor booleano True.

**Ejemplo:**

```python
diccionario = {1: "Ayan", 2: "Bunny", 3: "Ram", 4: "Bheem"}

all({1:'',2:'','':''})
```

**Salida:**

```python
False
```

- **sorted()**

Al igual que hace con listas y tuplas, el método sorted() devuelve una serie ordenada de las claves del diccionario. La clasificación ascendente no afecta al diccionario de Python original.

**Ejemplo:**

```python
diccionario = {7: "Ayan", 5: "Bunny", 8: "Ram", 1: "Bheem"}

sorted(diccionario)
```

**Salida:**

```python
[1, 5, 7, 8]
```

## Métodos Incorporados del Diccionario

A continuación se presentan los métodos incorporados del diccionario de Python junto con la descripción y el código.

- **clear()**

Se utiliza principalmente para eliminar todos los elementos del diccionario.

**Ejemplo:**

```python
# Métodos del diccionario

diccionario = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}

# Método clear()

diccionario.clear()

print(diccionario)
```

**Salida:**

```python
{ }
```

- **copy()**

Devuelve una copia superficial del diccionario que se crea.

**Ejemplo:**

```python
# Métodos del diccionario

diccionario = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}

# Método copy()

dic_demo = diccionario.copy()

print(dic_demo)
```

**Salida:**

```python
{1: 'Hcl', 2: 'WIPRO', 3: 'Facebook', 4: 'Amazon', 5: 'Flipkart'}
```

- **pop()**

Principalmente elimina el elemento utilizando la clave definida.

**Ejemplo:**

```python
# Métodos del diccionario

diccionario = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}

# Método pop()

dic_demo = diccionario.copy()

x = dic_demo.pop(1)

print(x)
```

**Salida:**

```python
{2: 'WIPRO', 3: 'Facebook', 4: 'Amazon', 5: 'Flipkart'}
```

- **popitem()**

Elimina el par clave-valor más reciente ingresado

**Ejemplo:**

```python
# Métodos del diccionario

diccionario = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}

# Método popitem()

dic_demo.popitem()

print(dic_demo)
```

**Salida:**

```python
{1: 'Hcl', 2: 'WIPRO', 3: 'Facebook'}
```

- **keys()**

Devuelve todas las claves del diccionario.

**Ejemplo:**

```python
# Métodos del diccionario

diccionario = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}

# Método keys()

print(dic_demo.keys())
```

**Salida:**

```python
dict_keys([1, 2, 3, 4, 5])
```

- **items()**

Devuelve todos los pares clave-valor como una tupla.

**Ejemplo:**

```python
# Métodos del diccionario

diccionario = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}

# Método items()

print(dic_demo.items())
```

**Salida:**

```python
dict_items([(1, 'Hcl'), (2, 'WIPRO'), (3, 'Facebook'), (4, 'Amazon'), (5, 'Flipkart')])
```

- **get()**

Se utiliza para obtener el valor especificado para la clave pasada.

**Ejemplo:**

```python
# Métodos del diccionario

diccionario = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}

# Método get()

print(dic_demo.get(3))
```

**Salida:**

```python
Facebook
```

- **update()**

Principalmente actualiza todo el diccionario añadiendo el par clave-valor de dict2 a este diccionario.

**Ejemplo:**

```python
# Métodos del diccionario

diccionario = {1: "H

cl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}

# Método update()

dic2 = {6: "Apple"}

diccionario.update(dic2)

print(diccionario)
```

**Salida:**

```python
{1: 'Hcl', 2: 'WIPRO', 3: 'Facebook', 4: 'Amazon', 5: 'Flipkart', 6: 'Apple'}
```

Estos son algunos de los métodos y funciones útiles que puedes utilizar con diccionarios en Python.
