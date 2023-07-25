# Variables

Una variable es un nombre que se utiliza para referirse a una ubicación de memoria. En Python, una variable también se conoce como un identificador y se utiliza para almacenar valores.

En Python, no es necesario especificar el tipo de variable porque Python es un lenguaje inferencial y lo suficientemente inteligente para obtener el tipo de variable.

Los nombres de las variables pueden ser un grupo de letras y dígitos, pero deben comenzar con una letra o un guión bajo.

Se recomienda utilizar letras minúsculas para el nombre de las variables. "Rahul" y "rahul" son dos variables diferentes.

## Nomenclatura de Identificadores

Las variables son un ejemplo de identificadores. Un identificador se utiliza para identificar los literales utilizados en el programa. Las reglas para nombrar un identificador son las siguientes:

- El primer carácter de la variable debe ser una letra o un guión bajo (_).
- Todos los caracteres, excepto el primer carácter, pueden ser letras en minúscula (a-z), letras en mayúscula (A-Z), guiones bajos o dígitos (0-9).
- El nombre del identificador no debe contener espacios en blanco ni caracteres especiales (!, @, #, %, ^, &, *).
- El nombre del identificador no debe ser similar a ninguna palabra clave definida en el lenguaje.
- Los nombres de los identificadores distinguen entre mayúsculas y minúsculas; por ejemplo, "mi nombre" y "MyName" no son lo mismo.
- Ejemplos de identificadores válidos: a123, _n, n_9, etc.
- Ejemplos de identificadores no válidos: 1a, n%4, n 9, etc.

## Declaración de Variables y Asignación de Valores

Python no nos obliga a declarar una variable antes de usarla en la aplicación. Nos permite crear una variable en el momento necesario.

No es necesario declarar explícitamente una variable en Python. Cuando asignamos un valor a una variable, esa variable se declara automáticamente.

El operador igual (=) se utiliza para asignar un valor a una variable.

## Referencias de Objetos

Es necesario entender cómo funciona el intérprete de Python cuando declaramos una variable. El proceso de tratamiento de variables es algo diferente de muchos otros lenguajes de programación.

Python es un lenguaje de programación altamente orientado a objetos; por eso, cada elemento de datos pertenece a un tipo específico de clase.

**Ejemplo:**

```python
print("John")
```

**Salida:**

```bash
John
```

El objeto de Python crea un objeto entero y lo muestra en la consola. En la declaración de impresión anterior, hemos creado un objeto de cadena. Verifiquemos su tipo usando la función integrada de Python **type()**.

**Ejemplo:**

```python
type("John")
```

**Salida:**

```bash
<class 'str'>
```

En Python, las variables son un nombre simbólico que es una referencia o un puntero a un objeto. Las variables se utilizan para denotar objetos por ese nombre.

**Ejemplo:**

```python
a = 50
```

![https://static.javatpoint.com/python/images/python-variables.png](https://static.javatpoint.com/python/images/python-variables.png)

En la imagen anterior, la variable **a** se refiere a un objeto entero.

Supongamos que asignamos el valor entero 50 a una nueva variable b.

**Ejemplo:**

```python
a = 50
b = a
```

![https://static.javatpoint.com/python/images/python-variables2.png](https://static.javatpoint.com/python/images/python-variables2.png)

La variable b se refiere al mismo objeto al que apunta a porque Python no crea otro objeto.

Asignemos un nuevo valor a b. Ahora ambas variables se referirán a diferentes objetos.

**Ejemplo:**

```python
a = 50
b = 100
```

![https://static.javatpoint.com/python/images/python-variables3.png](https://static.javatpoint.com/python/images/python-variables3.png)

Python gestiona la memoria de manera eficiente si asignamos la misma variable a dos valores diferentes.

## Identidad de Objeto

En Python, cada objeto creado se identifica de manera única. Python garantiza que no habrá dos objetos con el mismo identificador. La función incorporada **id()** se utiliza para identificar el identificador del objeto. Consideremos el siguiente ejemplo.

```python
a = 50

b = a

print(id(a))

print(id(b))

# Reasignar la variable a

a = 500

print(id(a))
```

**Salida:**

```bash
140734982691168
140734982691168
2822056960944
```

Asignamos **b = a, a** y **b** apuntan al mismo objeto. Cuando lo verificamos mediante la función **id()**, devuelve el mismo número. Luego, reasignamos **a** a 500; luego se refiere al nuevo identificador de objeto.

## Nombres de Variables

Ya hemos discutido cómo declarar una variable válida. Los nombres de las variables pueden tener cualquier longitud y pueden tener mayúsculas, minúsculas (de A a Z, de a a z), el dígito (0-9) y el guión bajo (_). Consideremos el siguiente ejemplo de nombres de variables válidos.

**Ejemplo:**

```python
nombre = "Devansh"

edad = 20

calificaciones = 80.50

print(nombre)

print(edad)

print(calificaciones)
```

**Salida:**

```bash
Devansh
20
80.5
```

Consideremos el siguiente nombre de variables válido.

**Ejemplo:**

```python
nombre = "A"

Nombre = "B"

naMe = "C"

NAME = "D"

n_a_m_e = "E"

_name = "F"

name_ = "G"

_name_ = "H"

na56me = "I"

print(nombre,Nombre,naMe,NAME,n_a_m_e, NAME, n_a_m_e, _name,

name_,_name, na56me)
```

**Salida:**

```bash
A B C D E D E F G F I
```

En el ejemplo anterior, hemos declarado algunos nombres de variables válidos como nombre, *name*, etc. Pero no se recomienda porque cuando intentamos leer el código, puede generar confusión. El nombre de la variable debe ser descriptivo para hacer que el código sea más legible.

Los nombres de palabras clave de varias palabras se pueden crear utilizando los siguientes métodos.

- **Camel Case -** En Camel Case, cada palabra o abreviatura en el medio comienza con una letra mayúscula. No hay intervención de espacios en blanco. Por ejemplo - nameOfStudent, valueOfVaraible, etc.
- **Pascal Case -** Es igual que Camel Case, pero aquí la primera palabra también es mayúscula. Por ejemplo - NameOfStudent, etc.
- **Snake Case -** En Snake Case, las palabras están separadas por guiones bajos. Por ejemplo - name_of_student, etc.

## Asignación Múltiple

Python nos permite asignar un valor a varias variables en una sola declaración, lo que también se conoce como asignaciones múltiples.

Podemos aplicar asignaciones múltiples de dos maneras, ya sea asignando un solo valor a varias variables o asignando varios valores a varias variables. Consideremos el siguiente ejemplo.

### 1. Asignar un Solo Valor a Varias Variables

**Ejemplo:**

```bash
x=y=z=50

print(x)

print(y)

print(z)
```

**Salida:**

```bash
50
50
50
```

### 2. Asignación de múltiples valores a varias variables

**Ejemplo:**

```bash
a,b,c=5,10,15

print a

print b

print c
```

**Salida:**

```bash
5
10
15
```

Los valores se asignarán en el orden en que aparecen las variables.

## Tipos de Variables

Hay dos tipos de variables en Python: variables locales y variables globales. Veamos las siguientes variables.

### Variable Local

Las variables locales son las variables que se declaran dentro de la función y tienen ámbito dentro de la función. Veamos el siguiente ejemplo.

**Ejemplo:**

```python
# Declarando una función

def suma():

# Definición de variables locales. Tienen alcance solo dentro de la función

a = 20

b = 30

c = a + b

print("La suma es:", c)

# Llamando a una función

suma()
```

**Salida:**

```bash
La suma es: 50
```

**Explicación:**

En el código anterior, declaramos una función llamada **suma()** y asignamos algunas variables dentro de la función. Estas variables se referirán como las **variables locales** que solo tienen alcance dentro de la función. Si intentamos usarlas fuera de la función, obtendremos un siguiente error.

**Ejemplo:**

```python
suma()

# Acceso a variable local fuera de la función

print(a)
```

**Salida:**

```bash
La suma es: 50
    print(a)
NameError: name 'a' is not defined
```

Intentamos usar una variable local fuera de su alcance; arrojó el error **NameError**.

### Variables Globales

Las variables globales se pueden utilizar en todo el programa, y su alcance es en todo el programa. Podemos usar variables globales dentro o fuera de la función.

Una variable declarada fuera de la función es la variable global de forma predeterminada. Python proporciona la palabra clave **global** para usar la variable global dentro de la función. Si no usamos la palabra clave **global**, la función la trata como una variable local. Veamos el siguiente ejemplo.

**Ejemplo:**

```python
# Declarar una variable y inicializarla

x = 101

# Variable global en la función

def funcionPrincipal():

# imprimiendo una variable global

global x

print(x)

# modificar una variable global

x = 'Bienvenido a Javatpoint'

print(x)

funcionPrincipal()

print(x)
```

**Salida:**

```bash
101
Bienvenido a Javatpoint
Bienvenido a Javatpoint
```

**Explicación:**

En el código anterior, declaramos una variable global **x** y le asignamos un valor. A continuación, definimos una función y accedimos a la variable declarada utilizando la palabra clave **global** dentro de la función. Ahora podemos modificar su valor. Luego, asignamos un nuevo valor de cadena a la variable **x**.

Ahora, llamamos a la función y procedimos a imprimir **x**. Imprimió el valor recién asignado de **x**.

## Eliminar una Variable

Podemos eliminar la variable utilizando la palabra clave **del**. La sintaxis se muestra a continuación.

**Sintaxis:**

```python

del <nombre_variable>
```

En el siguiente ejemplo, creamos una variable x y le asignamos un valor. Eliminamos la variable x y la imprimimos, obtenemos el error **"variable x no está definida"**. La variable x ya no se usará en el futuro.

**Ejemplo:**

```python
# Asignando un valor a x

x = 6

print(x)

# eliminando una variable.

del x

print(x)
```

**Salida:**

```bash
6
Traceback (most recent call last):
  File "C:/Users/DEVANSH SHARMA/PycharmProjects/Hello/multiprocessing.py", line 389, in
    print(x)
NameError: name 'x' is not defined
```

## Valor Máximo Posible de un Entero

A diferencia de otros lenguajes de programación, Python no tiene tipos de datos long int o float. Trata todos los valores enteros como un tipo de dato **int**. Aquí surge la pregunta. ¿Cuál es el valor máximo posible que puede contener la variable en Python? Consideremos el siguiente ejemplo.

**Ejemplo:**

```python
# Un programa de Python para demostrar que podemos almacenar

# números grandes en Python

a = 10000000000000000000000000000000000000000000

a = a + 1

print(type(a))

print (a)
```

**Salida:**

```bash
<class 'int'>
10000000000000000000000000000000000000000001
```

Como podemos ver en el ejemplo anterior, asignamos un valor entero grande a la variable **x** y verificamos su tipo. Imprimió **class <int>** no **long int**. Por lo tanto, no hay limitación del número por bits y podemos expandirlo al límite de nuestra memoria.

Python no tiene un tipo de dato especial para almacenar números más grandes.

### Imprimir Variables Individuales y Múltiples

Podemos imprimir varias variables en una sola instrucción de impresión. A continuación se presentan ejemplos de impresión de valores individuales y múltiples.

**Ejemplo: Impresión de variable individual:**

```python
# imprimir un solo valor

a = 5

print(a)

print((a))
```

**Salida:**

```bash
5
5
```

**Ejemplo: Impresión de varias variables:**

```python
a = 5

b = 6

# imprimir múltiples variables

print(a,b)

# separar las variables por la coma

Print(1, 2, 3, 4, 5, 6, 7, 8)
```

**Salida:**

```bash
5 6
1 2 3 4 5 6 7 8
```
