# Funciones

En este tutorial se cubrirán los fundamentos de las funciones en Python, incluyendo qué son, su sintaxis, sus partes principales, las palabras clave de retorno y los principales tipos. Además, examinaremos varios ejemplos de definiciones de funciones en Python.

## ¿Qué Son las Funciones?

Una función es una colección de afirmaciones relacionadas que realiza una operación matemática, analítica o evaluativa. Una colección de declaraciones llamadas funciones en Python devuelve la tarea particular. Las funciones en Python son simples de definir y esenciales para la programación de nivel intermedio. Los mismos criterios se aplican a los nombres de las funciones que a los nombres de las variables. El objetivo es agrupar ciertas acciones que se realizan con frecuencia y definir una función. Podemos llamar a la función y reutilizar el código que contiene con diferentes variables en lugar de crear repetidamente el mismo bloque de código para diferentes variables de entrada.

Las funciones definidas por el usuario y las funciones incorporadas son las dos categorías principales de funciones en Python. Ayudan a mantener el programa conciso, único y bien estructurado.

## Ventajas de las Funciones

Las funciones en Python tienen las siguientes ventajas.

- Al incluir funciones, podemos evitar repetir el mismo bloque de código una y otra vez en un programa.
- Las funciones en Python, una vez definidas, se pueden llamar muchas veces y desde cualquier lugar en un programa.
- Si nuestro programa en Python es grande, se puede dividir en varias funciones que son fáciles de rastrear.
- El logro principal de las funciones en Python es que podemos devolver tantas salidas como queramos con diferentes argumentos.

Sin embargo, llamar a las funciones siempre ha sido un inconveniente en un programa de Python.

**Sintaxis:**

```python
# Un ejemplo de función en Python
def nombre_de_funcion(parametros):
    # bloque de código
```

Los siguientes elementos componen la definición de una función, como se muestra arriba.

- El inicio de un encabezado de función se indica mediante una palabra clave llamada def.
- nombre_de_funcion es el nombre de la función que podemos usar para distinguirla de otras. Usaremos este nombre para llamar a la función más adelante en el programa. En Python, los nombres de las funciones deben seguir las mismas reglas que los nombres de las variables.
- Pasamos argumentos a la función definida utilizando parámetros. Sin embargo, son opcionales.
- El encabezado de la función se termina con dos puntos (:).
- Podemos usar una cadena de documentación llamada docstring en forma abreviada para explicar el propósito de la función.
- El cuerpo de la función está compuesto por varias declaraciones válidas de Python. La profundidad de la sangría de todo el bloque de código debe ser la misma (generalmente 4 espacios).
- Podemos usar una expresión de retorno para devolver un valor de una función definida.

### Ejemplo de Una Función Definida por el Usuario

Definiremos una función que, al llamarla, devolverá el cuadrado del número pasado como argumento.

**Ejemplo:**

```python
# Código de ejemplo de una función definida por el usuario en Python
def cuadrado(num):
    """
    Esta función calcula el cuadrado del número.
    """
    return num**2

objeto = cuadrado(6)
print("El cuadrado del número dado es: ", objeto)
```

**Salida:**

```bash
El cuadrado del número dado es:  36
```

## Llamando a Una Función

Una función se define utilizando la palabra clave def y dándole un nombre, especificando los argumentos que deben pasarse a la función y estructurando el bloque de código.

Después de que se haya completado la estructura básica de una función, podemos llamarla desde cualquier parte del programa. A continuación, se muestra un ejemplo de cómo usar la función a_function.

**Ejemplo:**

```python
# Código de ejemplo de cómo llamar a una función en Python

# Definir una función
def a_function(string):
    "Esto imprime el valor de la longitud de la cadena"
    return len(string)

# Llamar a la función que definimos
print("La longitud de la cadena Functions es: ", a_function("Functions"))
print("La longitud de la cadena Python es: ", a_function("Python"))
```

**Salida:**

```bash
La longitud de la cadena Functions es:  9
La longitud de la cadena Python es:  6
```

## Paso por Referencia vs. Paso por Valor

Todos los parámetros en el lenguaje de programación Python se pasan por referencia. Esto indica que si alteramos el valor de un argumento dentro de una función, la función de llamada también reflejará el cambio. Por ejemplo,

**Ejemplo:**

```python
# Código de ejemplo de paso por referencia vs. valor en Python

# Definir la función
def cuadrado(item_list):
    '''''''Esta función encontrará el cuadrado de los elementos en la lista'''
    squares = []
    for l in item_list:
        squares.append(l**2)
    return squares

# Llamar a la función definida
my_list = [17, 52, 8];
my_result = cuadrado(my_list)
print("Los cuadrados de la lista son: ", my_result)
```

**Salida:**

```bash
Los cuadrados de la lista son:  [289, 2704, 64]
```

## Argumentos de Función

Los siguientes son los tipos de argumentos que podemos utilizar para llamar a una función:

1. Argumentos predeterminados
2. Argumentos de palabras clave
3. Argumentos requeridos
4. Argumentos de longitud variable

### 1) Argumentos Predeterminados

Un argumento predeterminado es un tipo de parámetro que toma como entrada un valor predeterminado si no se proporciona ningún valor para el argumento cuando se llama a la función. Los argumentos predeterminados se demuestran en el siguiente ejemplo.

**Ejemplo:**

```python
# Código de Python para demostrar el uso de argumentos predeterminados

# Definir una función
def funcion(n1, n2 = 20):
    print("El número 1 es: ", n1)
    print("El número 2 es: ", n2)

# Llamar a la función y pasar solo un argumento
print("Pasando solo un argumento")
funcion(30)

# Ahora dar dos argumentos a la función
print("Pasando dos argumentos")
funcion(50,30)
```

**Salida:**

```bash
Pasando solo un argumento
El número 1 es:  30
El número 2 es:  20
Pasando dos argumentos
El número 1 es:  50
El número 2 es:

30
```

### 2) Argumentos de Palabras Clave

Los argumentos de una función llamada están vinculados a argumentos de palabras clave. Al invocar una función con argumentos de palabras clave, el usuario puede indicar a qué parámetro corresponde el valor del argumento mirando la etiqueta del parámetro.

Podemos eliminar ciertos argumentos o disponerlos en un orden diferente, ya que el intérprete de Python conectará las palabras clave proporcionadas para vincular los valores con sus parámetros. Otra forma de usar palabras clave para invocar el método de función() es la siguiente:

**Ejemplo:**

```python
# Código de Python para demostrar el uso de argumentos de palabras clave

# Definir una función
def funcion(n1, n2):
    print("El número 1 es: ", n1)
    print("El número 2 es: ", n2)

# Llamar a la función y pasar argumentos sin usar palabras clave
print("Sin usar palabras clave")
funcion(50, 30)

# Llamar a la función y pasar argumentos usando palabras clave
print("Usando palabras clave")
funcion(n2 = 50, n1 = 30)
```

**Salida:**

```bash
Sin usar palabras clave
El número 1 es:  50
El número 2 es:  30
Usando palabras clave
El número 1 es:  30
El número 2 es:  50
```

### 3) Argumentos Requeridos

Los argumentos dados a una función al llamarla en una secuencia posicional predefinida son argumentos requeridos. El número de argumentos requeridos en la llamada al método debe ser igual al número de argumentos proporcionados al definir la función.

Debemos enviar dos argumentos a la función function() en el orden correcto, de lo contrario se producirá un error de sintaxis, como se muestra a continuación.

**Ejemplo:**

```python
# Código de Python para demostrar el uso de argumentos requeridos

# Definir una función
def funcion(n1, n2):
    print("El número 1 es: ", n1)
    print("El número 2 es: ", n2)

# Llamar a la función y pasar dos argumentos en orden incorrecto, necesitamos que num1 sea 20 y num2 sea 30
print("Pasando argumentos en orden incorrecto")
funcion(30, 20)

# Llamar a la función y pasar solo un argumento
print("Pasando solo un argumento")
try:
    funcion(30)
except:
    print("La función necesita dos argumentos posicionales")
```

**Salida:**

```bash
Pasando argumentos en orden incorrecto
El número 1 es:  30
El número 2 es:  20
Pasando solo un argumento
La función necesita dos argumentos posicionales
```

### 4) Argumentos de Longitud Variable

Podemos utilizar caracteres especiales en las funciones de Python para pasar tantos argumentos como queramos en una función. Hay dos tipos de caracteres que podemos utilizar para este propósito:

1. `*args**` - Estos son argumentos sin palabras clave.
2. `*kwargs**` - Estos son argumentos con palabras clave.

Aquí hay un ejemplo para aclarar los argumentos de longitud variable.

**Ejemplo:**

```python
# Código de Python para demostrar el uso de argumentos de longitud variable

# Definir una función
def funcion(*args_list):
    ans = []
    for l in args_list:
        ans.append(l.upper())
    return ans

# Pasar argumentos args
objeto = funcion('Python', 'Functions', 'tutorial')
print(object)

# Definir una función
def funcion(**kargs_list):
    ans = []
    for key, value in kargs_list.items():
        ans.append([key, value])
    return ans

# Pasar argumentos kwargs
objeto = funcion(First = "Python", Second = "Functions", Third = "Tutorial")
print(objeto)
```

**Salida:**

```bash
['PYTHON', 'FUNCTIONS', 'TUTORIAL']
[['First', 'Python'], ['Second', 'Functions'], ['Third', 'Tutorial']]
```

## Declaración de Retorno

Escribimos una declaración de retorno en una función para salir de una función y devolver el valor calculado cuando se llama a una función definida.

**Sintaxis:**

```python
return <expresión que se devolverá como salida>
```

La declaración de retorno, que se proporciona como salida cuando se completa una tarea o función específica, puede tomar la forma de un argumento, una declaración o un valor. Una función declarada devolverá un objeto None si no se escribe una declaración de retorno.

Aquí hay un ejemplo de una declaración de retorno en las funciones de Python.

**Ejemplo:**

```python
# Código de Python para demostrar el uso de declaraciones de retorno

# Definir una función con declaración de retorno
def cuadrado(num):
    return num**2

# Llamar a la función y pasar argumentos.
print("Con declaración de retorno")
print(square(52))

# Definir una función sin declaración de retorno
def cuadrado(num):
    num**2

# Llamar a la función y pasar argumentos.
print("Sin declaración de retorno")
print(square(52))
```

**Salida:**

```bash
Con declaración de retorno
2704
Sin declaración de retorno
None
```

## Las Funciones Anónimas

Estos tipos de funciones en Python son anónimas ya que no las declaramos, como declaramos funciones habituales, usando la palabra clave def. Podemos usar la palabra clave lambda para definir funciones anónimas cortas de una sola salida.

Las expresiones lambda pueden aceptar un número ilimitado de argumentos; sin embargo, solo devuelven un valor como resultado de la función. No pueden tener múltiples expresiones o instrucciones en ellas. Dado que lambda necesita una expresión, no se puede llamar directamente a una función anónima para imprimir.

Las funciones lambda contienen su propio dominio local único, lo que significa que solo pueden hacer referencia a variables en su lista de argumentos y al nombre del dominio global.

Aunque las expresiones lambda parecen ser una representación en una línea de una función, no son como las expresiones en línea en C y C++, que pasan asignaciones de pila de función en ejecución por razones de eficiencia.

**Sintaxis:**

Las funciones lambda tienen una sola línea en su sintaxis:

```python
lambda [argumento1 [,argumento2... .argumenton]] : expresión
```

A continuación se muestra un ejemplo de cómo usar la función lambda:

**Ejemplo:**

```python
# Código de Python para demostrar funciones anónimas

# Definir una función
lambda_ = lambda argumento1, argumento2: argumento1 + argumento2;

# Llamar a la función y pasar valores
print("El valor de la función es: ", lambda_(20, 30))
print("El valor de la función es: ", lambda_(40, 50))
```

**Salida:**

```bash
El valor de la función es:  50
El valor de la función es:  90
```

## Ámbito y Tiempo de Vida de las Variables

El ámbito de una variable se refiere al alcance de un programa donde se declara. Los argumentos y variables de una función no son accesibles fuera de la función definida. Por lo tanto, solo tienen un ámbito local.

El tiempo de vida de una variable en la memoria RAM es cuánto tiempo permanece allí. El tiempo de vida de una función es el mismo que el de sus variables internas. Se eliminan después de salir de la función. En consecuencia, una función no mantiene el valor de una variable de ejecuciones anteriores.

Aquí hay un ejemplo sencillo del ámbito de una variable dentro de una función.

**Ejemplo:**

```python
# Código de Python para demostrar el ámbito y el tiempo de vida de las variables

# Definir una función para imprimir un número.
def numero():
    num = 50
    print("El valor de num dentro de la función: ", num)

num = 10
numero()
print("El valor de num fuera de la función:", num)
```

**Salida:**

```bash
El valor de num dentro de la función:  50
El valor de num fuera de la función: 10
```

Aquí podemos ver que num comienza con un valor de 10. El valor de num fuera de la función se mantuvo intacto, a pesar de que la función numero() cambió el valor de num a 50.

Esto se debe a que la variable interna num de la función es diferente de la variable externa (local a la función). A pesar de tener el mismo nombre de variable, son dos variables separadas con ámbitos separados.

Por otro lado, las variables fuera de la función son accesibles dentro de la función. Estas variables tienen un alcance global. Podemos obtener sus valores dentro de la función pero no podemos modificarlos ni cambiarlos. Si declaramos una variable como global utilizando la palabra clave global, también podemos cambiar el valor de la variable fuera de la función.

## Función Dentro de Otra Función

Las funciones se consideran objetos de primera clase en Python. En un lenguaje de programación, los objetos de primera clase se tratan de la misma manera en cualquier lugar donde se utilicen. Se pueden utilizar en expresiones condicionales, como argumentos y se pueden guardar en estructuras de datos integradas. Un lenguaje de programación se considera que implementa funciones de primera clase si trata a las funciones como objetos de primera clase. Python admite el concepto de funciones de primera clase.

Una función interna o anidada se refiere a una función definida dentro de otra función definida. Las funciones internas pueden acceder a los parámetros del ámbito exterior. Las funciones internas están construidas para protegerse de los cambios que ocurren fuera de la función. Muchos desarrolladores consideran que este proceso es encapsulación.

**Ejemplo:**

```python
# Código de Python para mostrar cómo acceder a las variables de una función anidada

# definir una función anidada
def palabra():
    string = 'Tutorial de funciones de Python'
    x = 5
    def numero():
        print(string)
        print(x)
    
    numero()

palabra()
```

**Salida:**

```bash
Tutorial de funciones de Python
5
```
