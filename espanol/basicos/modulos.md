# Módulos

En este tutorial, explicaremos cómo construir e importar módulos personalizados en Python. Además, podemos importar o integrar módulos incorporados de Python mediante varios métodos.

## ¿Qué es la Programación Modular?

La programación modular es la práctica de segmentar una tarea de programación única y complicada en sub tareas múltiples, más simples y más fáciles de gestionar. A estas sub tareas las llamamos módulos. Por lo tanto, podemos construir un programa más grande ensamblando diferentes módulos que actúen como bloques de construcción.

La modularización de nuestro código en una aplicación grande tiene muchos beneficios.

- **Simplificación:** Un módulo a menudo se centra en una área relativamente pequeña del problema general en lugar de la tarea completa. Si nos concentramos solo en un módulo, tendremos un problema de diseño más manejable en el que pensar. El desarrollo del programa ahora es más sencillo y menos propenso a errores.
- **Flexibilidad:** Los módulos se utilizan con frecuencia para establecer separaciones conceptuales entre diferentes áreas del problema. Si los módulos están construidos de manera que reduzcan la interconexión, es menos probable que los cambios en un módulo afecten otras partes del programa. (Incluso podríamos ser capaces de editar un módulo sin conocer el programa más allá de él). Esto aumenta la probabilidad de que un grupo de múltiples desarrolladores pueda colaborar en un proyecto grande.
- **Reutilización:** Las funciones creadas en un módulo específico pueden ser fácilmente accedidas por diferentes secciones de la asignación (a través de una API establecida adecuadamente). Como resultado, ya no es necesario duplicar código.
- **Ámbito:** Los módulos a menudo declaran un espacio de nombres distintos para evitar conflictos de identificadores en varias partes de un programa.

En Python, se fomenta la modularización del código mediante el uso de funciones, módulos y paquetes.

## ¿Qué Son los Módulos?

Un documento con definiciones de funciones y varias declaraciones escritas en Python se denomina módulo de Python.

En Python, podemos definir un módulo de una de las 3 formas siguientes:

- Python en sí permite la creación de módulos.
- Similar al módulo de expresiones regulares (re), un módulo puede estar escrito principalmente en lenguaje de programación C y luego ser insertado dinámicamente en tiempo de ejecución.
- Un módulo incorporado, como el módulo itertools, se incluye inherentemente en el intérprete.

Un módulo es un archivo que contiene código de Python, definiciones de funciones, declaraciones o clases. Un archivo example_module.py es un módulo que crearemos y cuyo nombre es example_module.

Utilizamos módulos para dividir programas complicados en piezas más pequeñas y comprensibles. Los módulos también permiten la reutilización de código.

En lugar de duplicar sus definiciones en varias aplicaciones, podemos definir nuestras funciones más utilizadas en un módulo separado y luego importar el módulo completo.

Construyamos un módulo. Guarda el archivo como example_module.py después de ingresar lo siguiente.

**Ejemplo:**

```python
# Aquí, estamos creando un programa simple de Python para mostrar cómo crear un módulo.

# definiendo una función en el módulo para reutilizarla
def square(number):
    # Aquí, la función anterior elevará al cuadrado el número pasado como entrada
    result = number ** 2
    return result # Aquí, estamos devolviendo el resultado de la función
```

Aquí, un módulo llamado example_module contiene la definición de la función square(). La función devuelve el cuadrado de un número dado.

### ¿Cómo Importar Módulos?

En Python, podemos importar funciones de un módulo a nuestro programa, o como decimos, a otro módulo.

Para ello, utilizamos la palabra clave import de Python. En la ventana de Python, agregamos después de la palabra clave import el nombre del módulo que deseamos importar. Importaremos el módulo que definimos anteriormente, example_module.

**Sintaxis:**

```python
import example_module
```

Las funciones que definimos en example_module no se importan de inmediato al programa actual. Aquí solo se importa el nombre del módulo, es decir, example_module.

Podemos usar el operador punto para utilizar las funciones utilizando el nombre del módulo. Por ejemplo:

**Ejemplo:**

```python
# aquí, llamamos al método square del módulo y pasamos el valor 4
result = example_module.square(4)
print("Utilizando el método square del módulo, el número es:", result)
```

**Salida:**

```bash
Utilizando el método square del módulo, el número es: 16
```

Existen varios módulos estándar para Python. La lista completa de módulos estándar de Python está disponible. La lista se puede ver utilizando el comando help.

Al igual que importamos nuestro módulo, un módulo definido por el usuario, podemos usar una instrucción de importación para importar otros módulos estándar.

Importar un módulo se puede hacer de varias maneras. A continuación se muestra una lista de ellas.

### Declaración de Importación

Usando la palabra clave import de Python y el operador punto, podemos importar un módulo estándar y acceder a las funciones definidas dentro de él. Aquí tienes un ejemplo.

**Ejemplo:**

```python
# Aquí, estamos creando un programa simple de Python para mostrar cómo importar un módulo estándar

# Aquí, estamos importando el módulo math, que es un módulo estándar
import math
print("El valor del número euler es", math.e)
# aquí, estamos imprimiendo el número euler desde el módulo math

```

**Salida:**

```bash
El valor del número euler es 2.718281828459045
```

### Importar y Renombrar

Al importar un módulo, también podemos cambiar su nombre. Aquí tienes un ejemplo para mostrarlo.

**Ejemplo:**

```python
# Aquí, estamos creando un programa simple de Python para mostrar cómo importar un módulo y cambiarle el nombre

# Aquí, estamos importando el módulo math y dándole un nombre diferente
import math as mt # aquí, estamos importando el módulo math como mt
print("El valor del número euler es", mt.e)
# aquí, estamos imprimiendo el número euler desde el módulo math
```

**Salida:**

```bash
El valor del número euler es 2.718281828459045
```

En este programa, el módulo math ahora se llama mt. En algunas situaciones, esto puede ayudarnos a escribir más rápido en caso de que los módulos tengan nombres largos.

Ten en cuenta que ahora el ámbito de nuestro programa no incluye el término math. Por lo tanto, mt.pi es la implementación adecuada del módulo, mientras que math.pi es inválido.

### Declaración from...import

Podemos importar nombres específicos de un módulo sin importar el módulo completo. Aquí tienes un ejemplo.

**Ejemplo:**

```python
# Aquí, estamos creando un programa simple de Python para mostrar cómo importar objetos específicos de un módulo

# Aquí, estamos importando el número euler del módulo math utilizando la palabra clave from
from math import e
# aquí, el valor e representa el número euler

print("El valor del número euler es", e)
```

**Salida:**

```bash
El valor del número euler es 2.718281828459045
```

En este caso, solo se importó la constante e del módulo math.

Evitamos el uso del operador punto (.) en estos casos. De esta manera, podemos importar muchos atributos al mismo tiempo:

**Ejemplo:**

```python
# Aquí, estamos creando un programa simple de Python para mostrar cómo importar varios objetos de un módulo

from math import e, tau

print("El valor de la constante tau es:", tau)
print("El valor del número euler es:", e)
```

**Salida:**

```bash
El valor de la constante tau es: 6.283185307179586
El valor del número euler es: 2.718281828459045
```

### Importar Todos los Nombres - Declaración from import *

Para importar todos los objetos de un módulo dentro del espacio de nombres actual, utiliza el símbolo * y las palabras clave from e import.

**Sintaxis:**

```python
from name_of_module import *
```

Hay ventajas y desventajas en el uso del símbolo *. No se recomienda usarlo a menos que estemos seguros de nuestros requisitos particulares del módulo; de lo contrario, no lo hagas.

Aquí tienes un ejemplo de lo mismo.

**Ejemplo:**

```python
# Aquí, estamos importando el módulo math completo usando *
from math import *

# Aquí, estamos accediendo a funciones del módulo math sin usar el operador punto
print("Calculando la raíz cuadrada:", sqrt(25))
# aquí, obtenemos el método sqrt y encontramos la raíz cuadrada de 25

print("Calculando la tangente de un ángulo:", tan(pi/6))
# aquí pi también se importa del módulo math
```

**Salida:**

```bash
Calculando la raíz cuadrada: 5.0
Calculando la tangente de un ángulo: 0.5773502691896257
```

## Localización de la Ruta de los Módulos

Cuando importamos un módulo en un programa de Python, el intérprete busca en varios lugares. Si no se encuentra el módulo incorporado, se buscan varios directorios. La lista de directorios se puede acceder mediante sys.path. El intérprete de Python busca el módulo de la siguiente manera:

El módulo se busca inicialmente en el directorio de trabajo actual. Luego, Python busca en cada directorio en el parámetro de shell PYTHONPATH si no se puede encontrar el módulo en el directorio actual. Una lista de carpetas conforma la variable de entorno conocida como PYTHONPATH. Si eso también falla, Python examina el conjunto de carpetas dependiente de la instalación configurado cuando se descarga Python.

Aquí tienes un ejemplo para imprimir la ruta.

**Ejemplo:**

```python
# Aquí, estamos importando el módulo sys
import sys

# Aquí, estamos imprimiendo la ruta utilizando sys.path
print("La ruta del módulo sys en el sistema es:", sys.path)
```

**Salida:**

```bash
La ruta del módulo sys en el sistema es:
['/home/pyodide', '/home/pyodide/lib/Python310.zip', '/lib/Python3.10', '/lib/Python3.10/lib-dynload', '', '/lib/Python3.10/site-packages']
```

## La Función Incorporada dir()

Podemos utilizar el método dir() para identificar los nombres declarados dentro de un módulo.

Por ejemplo, tenemos los siguientes nombres en el módulo estándar str. Para imprimir los nombres, utilizaremos el método dir() de la siguiente manera:

**Ejemplo:**

```python
# Aquí, estamos creando un programa simple de Python para imprimir el directorio de un módulo
print("Lista de funciones:\\n", dir(str), end=", ")
```

**Salida:**

```bash
Lista de funciones:
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

## Espacios de Nombres y Ámbito

Los objetos están representados por nombres o identificadores llamados variables. Un espacio de nombres es un diccionario que contiene los nombres de las variables (claves) y los objetos asociados a ellas (valores).

Una declaración de Python puede acceder a las variables tanto del espacio de nombres local como del global. Cuando hay dos variables con el mismo nombre, una local y otra global, la variable local toma el lugar de la variable global. Hay un espacio de nombres local separado para cada función. La regla de ámbito para los

métodos de clase es la misma que para las funciones regulares. Python determina si los parámetros son locales o globales basándose en predicciones razonables. Cualquier variable a la que se le asigne un valor en un método se considera local.

Por lo tanto, debemos usar la declaración global antes de poder asignar un valor a una variable global dentro de una función. La línea global Var_Name le informa a Python que Var_Name es una variable global. Python deja de buscar la variable dentro del espacio de nombres local.

Por ejemplo, declaramos la variable Number en el espacio de nombres global. Dado que le asignamos un valor a Number dentro de la función, Python considera que Number es una variable local. Si intentamos acceder al valor de la variable local sin declararla global o antes de hacerlo, se producirá un UnboundLocalError.

**Ejemplo:**

```python
Number = 204

def AddNumber():
    # aquí, estamos definiendo una función con el nombre AddNumber

    # Aquí, estamos accediendo al espacio de nombres global
    global Number

    Number = Number + 200

    print("El número es:", Number)
    # aquí, estamos imprimiendo el número después de realizar la suma

AddNumber()
# aquí, estamos llamando a la función

print("El número es:", Number)
```

**Salida:**

```bash
El número es: 404
El número es: 404
```
