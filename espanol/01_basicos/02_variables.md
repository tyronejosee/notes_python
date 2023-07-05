# Variables

Las variables son contenedores para almacenar valores de datos.

## Creación de Variables

Python no tiene un comando para declarar una variable.

Una variable se crea en el momento en que le asignas un valor por primera vez.

#### Ejemplo

```python
x = 5
y = "John"
print(x)
print(y)
```

Las variables no necesitan ser declaradas con ningún *tipo* específico y pueden cambiar de tipo incluso después de haber sido establecidas.

#### Ejemplo

```python
x = 4 # x es de tipo entero (int)
x = "Sally" # x ahora es de tipo cadena (str)
print(x)
```

## Conversión de Tipos

Si deseas especificar el tipo de datos de una variable, puedes hacerlo mediante la conversión de tipos (casting).

#### Ejemplo

```python
x = str(3) # x será '3'
y = int(3) # y será 3
z = float(3) # z será 3.0
```

## Obtener el Tipo

Puedes obtener el tipo de datos de una variable utilizando la función `type()`.

#### Ejemplo

```python
x = 5
y = "John"
print(type(x))
print(type(y))
```

> Aprenderás más sobre tipos de datos y conversión más adelante en este tutorial.
> 

## Comillas Simples o Dobles?

Las variables de tipo cadena pueden declararse utilizando comillas simples o dobles.

#### Ejemplo

```
x = "John"
# es lo mismo que
x = 'John'
```

## Sensible a Mayúsculas y Minúsculas

Los nombres de las variables distinguen entre mayúsculas y minúsculas.

#### Ejemplo

Esto creará dos variables.

```python
a = 4
A = "Sally"
# A no sobrescribirá a
```

## Nombres de Variables

Una variable puede tener un nombre corto (como x e y) o un nombre más descriptivo (age, carname, total_volume). Las reglas para las variables en Python son:

- El nombre de una variable debe comenzar con una letra o el carácter de subrayado (_).
- El nombre de una variable no puede comenzar con un número.
- El nombre de una variable solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _).
- Los nombres de las variables distinguen entre mayúsculas y minúsculas (age, Age y AGE son tres variables diferentes).
- El nombre de una variable no puede ser una palabra clave de Python.

#### Ejemplo

Nombres de variables válidos.

```python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

---

#### Ejemplo

Nombres de variables no válidos.

```python
2myvar = "John"
my-var = "John"
my var = "John"
```

---

> Recuerda que los nombres de variables distinguen entre mayúsculas y minúsculas
> 

## Nombres de Variables con Varias Palabras

Los nombres de variables con más de una palabra pueden ser difíciles de leer.

Existen varias técnicas que puedes utilizar para que sean más legibles.

### Camel Case

Cada palabra, excepto la primera, comienza con una letra mayúscula.

```python
myVariableName = "John"
```

### Pascal Case

Cada palabra comienza con una letra mayúscula.

```python
MyVariableName = "John"
```

### Snake Case

Cada palabra está separada por un guion bajo.

```python
my_variable_name = "John"
```

## Asignar Muchos Valores a Múltiples Variables

Python te permite asignar valores a múltiples variables en una sola línea.

#### Ejemplo

```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```

> **Nota:** Asegúrate de que el número de variables coincida con el número de valores, de lo contrario obtendrás un error.
> 

## Asignar un Único Valor a Múltiples Variables

También puedes asignar el *mismo* valor a múltiples variables en una sola línea.

#### Ejemplo

```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

## Desempaquetar una Colección

Si tienes una colección de valores en una lista, tupla, etc., Python te permite extraer los valores en variables. Esto se llama *desempaquetar*.

#### Ejemplo

Desempaquetar una lista.

```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```

## Variables de Salida

La función `print()` de Python se utiliza a menudo para mostrar variables.

#### Ejemplo

```python
x = "Python es increíble"
print(x)
```

En la función `print()`, puedes mostrar múltiples variables separadas por comas.

#### Ejemplo

```python
x = "Python"
y = "es"
z = "increíble"
print(x, y, z)
```

También puedes utilizar el operador `+` para mostrar múltiples variables.

#### Ejemplo

```python
x = "Python "
y = "es "
z = "increíble"
print(x + y + z)
```

> Observa el espacio después de "Python " y "es ", sin ellos, el resultado sería "Pythonesincreíble".
> 

Para los números, el carácter `+` funciona como un operador matemático.

#### Ejemplo

```python
x = 5
y = 10
print(x + y)
```

En la función `print()`, cuando intentas combinar una cadena y un número con el operador `+`, Python te dará un error.

---

#### Ejemplo

```python
x = 5
y = "John"
print(x + y)
```

---

La mejor manera de mostrar múltiples variables en la función `print()` es separarlas con comas, lo cual incluso admite diferentes tipos de datos.

#### Ejemplo

```python
x = 5
y = "John"
print(x, y)
```

## Variables Globales

Las variables que se crean fuera de una función (como en todos los ejemplos anteriores) se conocen como variables globales.

Las variables globales pueden ser utilizadas por todos, tanto dentro de funciones como fuera de ellas.

#### Ejemplo

Crear una variable fuera de una función y utilizarla dentro de la función

```python
x = "increíble"

def myfunc():
    print("Python es " + x)

myfunc()
```

Si creas una variable con el mismo nombre dentro de una función, esta variable

será local y solo se podrá usar dentro de la función. La variable global con el mismo nombre seguirá siendo global y mantendrá su valor original.

#### Ejemplo

Crear una variable dentro de una función con el mismo nombre que la variable global

```python
x = "increíble"

def myfunc():
    x = "fantástico"
    print("Python es " + x)

myfunc()

print("Python es " + x)
```

## La Palabra Clave global

Normalmente, cuando creas una variable dentro de una función, esa variable es local y solo se puede usar dentro de esa función.

Para crear una variable global dentro de una función, puedes usar la palabra clave `global`.

#### Ejemplo

Si utilizas la palabra clave `global`, la variable pertenece al ámbito global.

```python
def myfunc():
    global x
    x = "fantástico"

myfunc()

print("Python es " + x)
```

Además, utiliza la palabra clave `global` si deseas cambiar una variable global dentro de una función.

#### Ejemplo

Para cambiar el valor de una variable global dentro de una función, haz referencia a la variable utilizando la palabra clave `global`.

```python
x = "increíble"

def myfunc():
    global x
    x = "fantástico"

myfunc()

print("Python es " + x)
```
