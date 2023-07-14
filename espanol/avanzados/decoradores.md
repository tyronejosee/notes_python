# Decoradores

Los decoradores son una de las herramientas más útiles y poderosas de Python. Se utilizan para modificar el comportamiento de una función. Los decoradores brindan la flexibilidad de envolver otra función para expandir el funcionamiento de la función envuelta sin modificarla permanentemente.

> En los decoradores, las funciones se pasan como argumento a otra función y luego se llaman dentro de la función envolvente.
> 

También se conoce como **metaprogramación**, donde una parte del programa intenta cambiar otra parte del programa en tiempo de compilación.

Antes de comprender el **decorador**, debemos conocer algunos conceptos importantes de Python.

## ¿Qué Son las funciones?

Python tiene una característica muy interesante, que es que todo se trata como un objeto, incluso las clases o cualquier variable que definamos en Python también se asume como un objeto. Las funciones son objetos de primera clase en Python porque pueden hacer referencia, pasarse a una variable y devolverse desde otras funciones también. A continuación se muestra un ejemplo:

**Ejemplo:**

```python
def func1(msg): # aquí creamos una función y pasamos el parámetro
    print(msg)

func1("Hola, bienvenido a la función") # aquí imprimimos los datos de la función 1
func2 = func1 # aquí copiamos los datos de la función 1 en la función 2
func2("Hola, bienvenido a la función") # aquí imprimimos los datos de la función 2
```

**Salida:**

```bash
Hola, bienvenido a la función
Hola, bienvenido a la función
```

En el programa anterior, cuando ejecutamos el código, da la misma salida para ambas funciones. La función **func2** se refiere a la función **func1** y actúa como una función. Debemos comprender los siguientes conceptos de la función:

- La función se puede hacer referencia y pasar a una variable, y también se puede devolver desde otras funciones.
- Las funciones se pueden declarar dentro de otra función y pasarse como argumento a otra función.

## Función Interna

Python proporciona la capacidad de definir una función dentro de otra función. Este tipo de funciones se llaman funciones internas. Considera el siguiente ejemplo:

**Ejemplo:**

```python
def func(): # aquí creamos una función y pasamos el parámetro
    print("Estamos en la primera función") # aquí imprimimos los datos de la función
    def func1(): # aquí creamos una función y pasamos el parámetro
        print("Esta es la primera función secundaria") # aquí imprimimos los datos de la función 1
    def func2(): # aquí creamos una función y pasamos el parámetro
        print("Esta es la segunda función secundaria") # aquí imprimimos los datos de la función # 2
    func1()
    func2()

func()
```

**Salida:**

```bash
Estamos en la primera función
Esta es la primera función secundaria
Esta es la segunda función secundaria
```

En el programa anterior, no importa cómo se declaren las funciones secundarias. La ejecución de la función secundaria afecta la salida. Estas funciones secundarias están localmente vinculadas con **func()**, por lo que no se pueden llamar por separado.

Una función que acepta otra función como argumento también se llama **función de orden superior**.

**Ejemplo:**

```python
def add(x): # aquí creamos una función add y pasamos el parámetro
    return x + 1 # aquí devolvemos el valor pasado sumándole 1

def sub(x): # aquí creamos una función sub y pasamos el parámetro
    return x - 1 # aquí devolvemos el valor pasado restando 1

def operator(func, x): # aquí creamos una función y pasamos el parámetro
    temp = func(x)
    return temp

print(operator(sub, 10)) # aquí imprimimos la operación de sustracción con 10
print(operator(add, 20)) # aquí imprimimos la operación de suma con 20
```

**Salida:**

```bash
9
21
```

En el programa anterior, hemos pasado la función `sub()` y la función `add()` como argumento en la función **operator()**.

Una función puede devolver otra función.

**Ejemplo:**

```python
def hello(): # aquí creamos una función llamada hello
    def hi(): # aquí creamos una función llamada hi
        print("Hola") # aquí imprimimos la salida de la función
    return hi # aquí devolvemos la salida de la función

new = hello()
new()
```

**Salida:**

```bash
Hola
```

En el programa anterior, la función `hi()` está anidada dentro de la función `hello()`. Se devolverá cada vez que llamemos a `hi()`.

### Decorando Funciones con Parámetros

Veamos un ejemplo para comprender la función decoradora con parámetros:

**Ejemplo:**

```python
def divide(x, y): # aquí creamos una función y pasamos los parámetros
    print(x / y) # aquí imprimimos el resultado de la expresión

def outer_div(func): # aquí creamos una función y pasamos el parámetro
    def inner(x, y): # aquí creamos una función y pasamos los parámetros
        if x < y:
            x, y = y, x
        return func(x, y) # aquí devolvemos una función con algunos parámetros pasados
    return inner

divide1 = outer_div(divide)
divide1(2, 4)
```

**Salida:**

```bash
2.0
```

### Decorador Sintáctico

En el programa anterior, hemos decorado `out_div()`, que es un poco voluminoso. En lugar de usar el método anterior, Python permite **usar el decorador de manera más fácil con el símbolo @**. A veces se llama sintaxis "pie”.

**Ejemplo:**

```python
def outer_div(func): # aquí creamos una función y pasamos el parámetro
    def inner(x, y): # aquí creamos una función y pasamos los parámetros
        if x < y:
            x, y = y, x
        return func(x, y) # aquí devolvemos la función con los parámetros
    return inner

# Aquí abajo está la sintaxis del generador
@outer_div
def divide(x, y): # aquí creamos una función y pasamos los parámetros
    print(x / y)
```

**Salida:**

```bash
2.0
```

### Reutilización del Decorador

También podemos

reutilizar el decorador llamando de nuevo a esa función decoradora. Creemos un decorador en su propio módulo que se puede utilizar en muchas otras funciones. Creamos un archivo llamado `mod_decorator.py` con el siguiente código:

**Ejemplo:**

```python
def do_twice(func): # aquí creamos una función y pasamos el parámetro
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
```

Podemos importar mod_decorator.py en otro archivo.

**Ejemplo:**

```python
from decorator import do_twice

@do_twice
def say_hello():
    print("Hola ahí")

say_hello()
```

**Salida:**

```bash
Hola ahí
Hola ahí
```

### Decorador de Python con Argumentos

Queremos pasar algunos argumentos en la función. Hagámoslo en el siguiente código:

**Ejemplo:**

```python
from decorator import do_twice

@do_twice
def display(name):
    print(f"Hola {name}")

display()
```

**Salida:**

```bash
TypeError: display() missing 1 required positional argument: 'name'
```

Como se puede ver, la función no aceptó el argumento. Ejecutar este código genera un error. Podemos solucionar este error usando ***args** y ****kwargs** en la función interna del decorador. Modifiquemos **decorator.py** de la siguiente manera:

**Ejemplo:**

```python
def do_twice(func):
    def wrapper_function(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_function
```

Ahora **wrapper_function()** puede aceptar cualquier número de argumentos y pasarlos a la función.

**Ejemplo:**

```python
from decorator import do_twice

@do_twice
def display(name):
    print(f"Hola {name}")

display("John")
```

**Salida:**

```bash
Hola John
Hola John
```

### Devolver Valores de Funciones Decoradas

Podemos controlar el tipo de retorno de la función decorada. El ejemplo se muestra a continuación:

```python
from decorator import do_twice

@do_twice
def return_greeting(name):
    print("Hemos creado un saludo")
    return f"Hola {name}"

hi_adam = return_greeting("Adam")
```

**Salida:**

```bash
Hemos creado un saludo
Hemos creado un saludo
```

## Decoradores Elegantes

Entendamos los decoradores elegantes mediante el siguiente tema:

### Decoradores de Clase

Python proporciona dos formas de decorar una clase. En primer lugar, podemos decorar el método dentro de una clase; existen decoradores incorporados como **@classmethod, @staticmethod** y **@property** en Python. Los decoradores **@classmethod** y **@staticmethod** definen métodos dentro de una clase que no están conectados a ninguna otra instancia de la clase. El **@property** se utiliza generalmente para modificar los métodos get y set de los atributos de una clase. Entendámoslo mediante el siguiente ejemplo:

**Ejemplo 1:**

**decorador @property** - Al usarlo, podemos utilizar la función de clase como un atributo. Considera el siguiente código:

```python
class Student: # aquí creamos una clase llamada Estudiante
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @property
    def display(self):
        return self.name + " obtuvo una calificación de " + self.grade

stu = Student("John", "B")
print("Nombre del estudiante:", stu.name)
print("Calificación del estudiante:", stu.grade)
print(stu.display)
```

**Salida:**

```bash
Nombre del estudiante: John
Calificación del estudiante: B
John obtuvo una calificación de B
```

**Ejemplo 2:**

**decorador @staticmethod** - El **@staticmethod** se utiliza para definir un método estático en la clase. Se llama utilizando el nombre de la clase y también mediante una instancia de la clase.

**Ejemplo:**

```python
class Person: # aquí creamos una clase llamada Estudiante
    @staticmethod
    def hello(): # aquí definimos una función llamada hello
        print("Hola Peter")

per = Person()
per.hello()
Person.hello()
```

**Salida:**

```bash
Hola Peter
Hola Peter
```

### Clase Singleton

Una clase singleton solo tiene una instancia. Hay muchos singletons en Python, como True, None, etc.

### Anidación de Decoradores

Podemos usar múltiples decoradores apilándolos uno encima del otro. Considera el siguiente ejemplo:

**Ejemplo:**

```python
@function1
@function2
def function(name):
    print(f"{name}")
```

En el código anterior, hemos utilizado el decorador anidado apilándolos uno encima del otro.

### Decorador con Argumentos

Siempre es útil pasar argumentos en un decorador. El decorador puede ejecutarse varias veces según el valor dado del argumento. Consideremos el siguiente ejemplo:

**Ejemplo:**

```python
import functools # aquí estamos importando functools a nuestro programa

def repeat(num): # aquí estamos definiendo una función repeat y pasando un parámetro
    def decorator_repeat(func): # aquí estamos definiendo una función y pasando un parámetro
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num): # aquí estamos inicializando un bucle for y repitiendo num veces
                value = func(*args, **kwargs)
            return value # aquí estamos devolviendo el valor
        return wrapper # aquí estamos devolviendo la clase wrapper
    return decorator_repeat

# Aquí estamos pasando num como un argumento que repite la función print
@repeat(num=5)
def function1(name):
    print(f"{name}")
```

**Salida:**

```bash
JavatPoint
JavatPoint
JavatPoint
JavatPoint
JavatPoint
```

En el ejemplo anterior, **@repeat** se refiere a un objeto de función que se puede llamar en otra función. **@repeat(num = 5)** devolverá una función que actúa como decorador.

El código anterior puede parecer complejo, pero es el patrón de decorador más comúnmente utilizado, donde hemos utilizado una definición adicional **def** que maneja los argumentos del decorador.

> **Nota:** El decorador con argumento no se utiliza con frecuencia en la programación, pero proporciona flexibilidad. Se puede usar con o sin argumentos.
> 

### Decoradores con Estado

Los decoradores con estado se utilizan para realizar un seguimiento del estado del decorador. Consideremos el ejemplo en el que creamos un decorador que cuenta cuántas veces se ha llamado la función.

**Ejemplo:**

```python
import functools # aquí estamos importando functools a nuestro programa

def count_function(func): # aquí estamos definiendo una función y pasando el parámetro func
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Llamada {wrapper_count_calls.num_calls} de {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls # aquí estamos devolviendo la llamada del decorador

@count_function
def say_hello(): # aquí estamos definiendo una función y pasando el parámetro
    print("Di Hola")

say_hello()
say_hello()
```

**Salida:**

```bash
Llamada 1 de 'say_hello'
Di Hola
Llamada 2 de 'say_hello'
Di Hola
```

En el programa anterior, el estado representa el número de llamadas de la función almacenado en **.num_calls** en la función envolvente. Cuando llamamos a **say_hello()**, se mostrará el número de llamada de la función.

### Clases como Decoradores

Las clases son la mejor manera de mantener el estado. En esta sección, aprenderemos cómo usar una clase como decorador. Aquí crearemos una clase que contiene **init()** y toma **func** como argumento. La clase debe ser invocable para que pueda sustituir a la función decorada.

Para hacer que una clase sea invocable, implementamos el método especial **call()**.

**Ejemplo:**

```python
import functools # aquí estamos importando functools a nuestro programa

class Count_Calls: # aquí estamos creando una clase para obtener el recuento de llamadas
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Llamada {self.num_calls} de {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@Count_Calls
def say_hello(): # aquí estamos definiendo una función y pasando el parámetro
    print("Di Hola")

say_hello()
say_hello()
say_hello()
```

**Salida:**

```bash
Llamada 1 de 'say_hello'
Di Hola
Llamada 2 de 'say_hello'
Di Hola
Llamada 3 de 'say_hello'
Di Hola
```

El método `__init__()` almacena una referencia a la función y puede realizar cualquier otra inicialización necesaria.
