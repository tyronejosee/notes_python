# Excepciones

Cuando un programa en Python encuentra un error, detiene la ejecución del resto del programa. Un error en Python puede ser tanto un error en la sintaxis de una expresión como una excepción en Python. Veremos qué es una excepción. Además, veremos la diferencia entre un error de sintaxis y una excepción en este tutorial. A continuación, aprenderemos sobre los bloques try y except, y cómo generar excepciones y hacer afirmaciones. Después de eso, veremos la lista de excepciones en Python.

# ¿Qué es una Excepción?

Una excepción en Python es un incidente que ocurre mientras se ejecuta un programa y provoca que el curso regular de los comandos del programa se vea interrumpido. Cuando el código Python se encuentra con una condición que no puede manejar, genera una excepción. Un objeto en Python que describe un error se llama excepción.

Cuando el código Python genera una excepción, tiene dos opciones: manejar la excepción de inmediato o detenerse y salir.

### Excepciones versus Errores de Sintaxis

Cuando el intérprete identifica una declaración que tiene un error, se producen errores de sintaxis. Considera el siguiente escenario:

**Código**

```bash
# Código Python después de eliminar el error de sintaxis

cadena = "Excepciones en Python"

for c in cadena:

if (c != ' '):

print(c)
```

**Salida:**

```bash
    if (s != o:
              ^
SyntaxError: sintaxis no válida
```

La flecha en la salida muestra dónde el intérprete encontró un error de sintaxis. En este caso, había un paréntesis sin cerrar. Ciérralo y vuelve a ejecutar el programa:

**Código**

```bash
# Código Python después de eliminar el error de sintaxis

cadena = "Excepciones en Python"

for c in cadena:

if (c != ' '):

print(c)
```

**Salida:**

```bash
      2 cadena = "Excepciones en Python"
      4 for c in cadena:
----> 5     if (c != ' '):
      6         print(c)

NameError: name 'o' is not defined
```

Encontramos un error de excepción después de ejecutar este código. Cuando un código Python válido desde el punto de vista sintáctico produce un error, este es el tipo de error que se produce. La última línea de la salida especificó el nombre del código de error de excepción encontrado. En lugar de mostrar solo "error de excepción", Python muestra información sobre el tipo de error de excepción que ocurrió. En este caso, fue un NameError (Error de Nombre). Python incluye varias excepciones integradas. Sin embargo, Python ofrece la capacidad de construir excepciones personalizadas.

# Declaración Try y Except - Capturando Excepciones

En Python, capturamos excepciones y las manejamos utilizando bloques de código try y except. La cláusula try contiene el código que puede generar una excepción, mientras que la cláusula except contiene las líneas de código que manejan la excepción. Veamos si podemos acceder al índice de un arreglo, el cual está fuera del alcance del tamaño del arreglo, y manejamos la excepción resultante.

**Código**

```python
# Código Python para capturar una excepción y manejarla utilizando bloques de código try y except

a = ["Python", "Excepciones", "try y except"]

try:

    # recorriendo los elementos del arreglo a, eligiendo un rango que va más allá del tamaño del arreglo
    for i in range(4):
        print("El índice y el elemento del arreglo son", i, a[i])

    # si ocurre un error en el bloque try, entonces el bloque except será ejecutado por el intérprete de Python
except:
    print("Índice fuera de rango")
```

**Salida:**

```bash
El índice y el elemento del arreglo son 0 Python
El índice y el elemento del arreglo son 1 Excepciones
El índice y el elemento del arreglo son 2 try y except
Índice fuera de rango
```

Los bloques de código que potencialmente pueden generar un error se insertan dentro de la cláusula try en el ejemplo anterior. El valor de i mayor que 2 intenta acceder al elemento de la lista más allá de su tamaño, lo cual no está presente, lo que resulta en una excepción. Luego, la cláusula except captura esta excepción y ejecuta el código sin detenerlo.

# Cómo Generar una Excepción

Si una condición no cumple con nuestros criterios pero es correcta según el intérprete de Python, podemos generar intencionalmente una excepción usando la palabra clave raise. Podemos usar una excepción personalizada en conjunción con la declaración.

Si deseamos usar raise para generar una excepción cuando ocurre una condición dada, podemos hacerlo de la siguiente manera:

**Código**

```python
# Código Python para mostrar cómo generar una excepción en Python

num = [3, 4, 5, 7]

if len(num) > 3:
    raise Exception(f"La longitud de la lista dada debe ser menor o igual a 3 pero es {len(num)}")
```

**Salida:**

```bash
      1 num = [3, 4, 5, 7]
      2 if len(num) > 3:
----> 3     raise Exception( f"La longitud de la lista dada debe ser menor o igual a 3 pero es {len(num)}" )

Exception: La longitud de la lista dada debe ser menor o igual a 3 pero es 4
```

La implementación se detiene y muestra nuestra excepción en la salida, proporcionando indicaciones sobre lo que salió mal.

# Afirmaciones en Python

Cuando terminamos de verificar el programa, una afirmación es una prueba de consistencia que podemos activar o desactivar.

La forma más sencilla de entender una afirmación es compararla con una condición de tipo si-entonces. Si el resultado es falso al evaluar una expresión, se lanza una excepción.

Las afirmaciones se realizan mediante la declaración assert, que se agregó en Python 1.5 como una palabra clave nueva.

Las afirmaciones se utilizan comúnmente al comienzo de una función para verificar la validez de la entrada y al final de la llamada a la función para verificar la validez de la salida.

### La Declaración assert

Cuando Python encuentra una declaración assert, examina la expresión adyacente, preferiblemente verdadera. Si el resultado de la expresión es falso, Python lanza una excepción AssertionError.

**La sintaxis de la cláusula assert es la siguiente:**

1. **assert** Expresión[, Argumento]

Si la afirmación falla, Python utiliza ArgumentException como argumento para AssertionError. Podemos usar la cláusula try-except para capturar y manejar excepciones AssertionError, pero si no lo hacemos, el programa se detendrá y el intérprete de Python generará un seguimiento de pila (traceback).

**Código**

```python
# Programa Python para mostrar cómo usar la palabra clave assert

# definir una función

def raiz_cuadrada(Número):

    assert (Número < 0), "Dame un entero positivo"

    return Número**(1/2)

# Llamando a la función y pasando los valores

print(raiz_cuadrada(36))

print(raiz_cuadrada(-36))
```

**Salida:**

```bash
      7 # Llamando a la función y pasando los valores
----> 8 print(raiz_cuadrada(36))
      9 print(raiz_cuadrada(-36))

AssertionError: Dame un entero positivo
```

# Try con la Cláusula Else

Python también admite la cláusula else, que debe ir después de cada cláusula except, en los bloques try y except. Solo cuando la cláusula try no produce una excepción, el intérprete de Python pasa al bloque else.

Aquí hay un ejemplo de una cláusula try con una cláusula else.

**Código**

```python
# Programa Python para mostrar cómo usar la cláusula else con las cláusulas try y except

# Definir una función que devuelve el recíproco de un número

def recíproco(num1):

    try:

        reci = 1 / num1

    except ZeroDivisionError:

        print("No podemos dividir por cero")

    else:

        print(reci)

# Llamando a la función y pasando valores

recíproco(4)

recíproco(0)
```

**Salida:**

```bash
0.25
No podemos dividir por cero
```

# La Palabra Clave Finally en Python

La palabra clave finally está disponible en Python, y siempre se usa después del bloque try-except. El bloque de código finally siempre se ejecuta después de que el bloque try haya terminado normalmente o después de que el bloque try haya terminado por alguna otra razón.

Aquí hay un ejemplo de la palabra clave finally con las cláusulas try-except:

**Código**

```python
# Código Python para mostrar el uso de la cláusula finally

# Generando una excepción en el bloque try

try:
    div = 4 // 0
    print(div)

# este bloque manejará la excepción generada

except ZeroDivisionError:
    print("Intentando dividir por cero")

# esto siempre se ejecutará sin importar si se genera una excepción o no

finally:
    print('Este es el código de la cláusula finally')
```

**Salida:**

```bash
Intentando dividir por cero
Este es el código de la cláusula finally
```

# Excepciones Definidas por el Usuario

Python también nos permite diseñar nuestras propias excepciones personalizadas al heredar clases de las excepciones incorporadas típicas.

Aquí hay un ejemplo de RuntimeError. En este caso, se crea una clase que deriva de RuntimeError. Una vez que se detecta una excepción, podemos usar esto para mostrar información detallada adicional.

Generamos una excepción definida por el usuario en el bloque try y luego manejamos la excepción en el bloque except. Se crea un ejemplo de la clase EmptyError utilizando la variable var.

**Código**

```python
class EmptyError(RuntimeError):
    def __init__(self, argumento):
        self.argumentos = argumento
```

Una vez que se haya creado la clase anterior, lo siguiente es cómo generar una excepción:

**Código**

```python
var = " "

try:
    raise EmptyError("La variable está vacía")

except (EmptyError, var):
    print(var.argumentos)
```

**Salida:**

```bash
      2 try:
----> 3     raise EmptyError( "La variable está vacía" )
      4 except (EmptyError, var):

EmptyError: La variable está vacía
```

# Lista de Excepciones de Python

Aquí está la lista completa de excepciones integradas en Python.

| Núm. | Nombre de la Excepción | Descripción de la Excepción |
| --- | --- | --- |
| 1 | Exception | Todas las excepciones en Python tienen una clase base. |
| 2 | StopIteration | Si el método next() devuelve nulo para un iterador, se genera esta excepción. |
| 3 | SystemExit | El procedimiento sys.exit() levanta este valor. |
| 4 | StandardError | Excluyendo StopIteration y SystemExit, esta es la clase base de todas las excepciones integradas en Python. |
| 5 | ArithmeticError | Todos los errores de cálculo matemático pertenecen a esta clase base. |
| 6 | OverflowError | Se genera esta excepción cuando una operación supera el límite máximo del tipo de dato numérico. |
| 7 | FloatingPointError | Si falla una operación de punto flotante, se levanta esta excepción. |
| 8 | ZeroDivisionError | Para todos los tipos de datos numéricos, se genera su valor cuando se intenta dividir un número por cero. |
| 9 | AssertionError | Si falla la declaración Assert, se levanta esta excepción. |
| 10 | AttributeError | Se genera esta excepción si falla la referencia a una variable o al asignarle un valor. |
| 11 | EOFError | Cuando se alcanza el final del archivo y el intérprete no recibe ningún valor de entrada mediante las funciones raw_input() o input(), se genera esta excepción. |
| 12 | ImportError | Se genera esta excepción si falla el uso de la palabra clave import para importar un módulo. |
| 13 | KeyboardInterrupt | Si el usuario interrumpe la ejecución de un programa, generalmente al presionar Ctrl+C, se genera esta excepción. |
| 14 | LookupError | LookupErrorBase es la clase base para todos los errores de búsqueda. |
| 15 | IndexError | Se genera esta excepción cuando el índice al que se intenta acceder no se encuentra. |
| 16 | KeyError | Cuando la clave dada no se encuentra en el diccionario donde se busca, se genera esta excepción. |
| 17 | NameError | Se genera esta excepción cuando una variable no se encuentra ni en el ámbito local ni en el global. |
| 18 | UnboundLocalError | Se genera esta excepción cuando intentamos acceder a una variable local dentro de una función y la variable no ha sido asignada con ningún valor. |
| 19 | EnvironmentError | Todas las excepciones que surgen fuera del entorno de Python tienen esta clase base. |
| 20 | IOError | Si falla una acción de entrada o salida, como al usar el comando print o la función open() para acceder a un archivo que no existe, se genera esta excepción. |
| 22 | SyntaxError | Se genera esta excepción siempre que ocurre un error de sintaxis en nuestro programa. |
| 23 | IndentationError | Se genera esta excepción cuando hacemos una indentación incorrecta. |
| 24 | SystemExit | Se genera esta excepción cuando se utiliza el método sys.exit() para terminar el intérprete de Python. El analizador se detiene si la situación no se aborda dentro del código. |
| 25 | TypeError | Se genera esta excepción siempre que se intenta ejecutar una acción o función incompatible con el tipo de dato. |
| 26 | ValueError | Se genera esta excepción si los parámetros para un método integrado de un tipo de dato particular son del tipo correcto pero tienen valores incorrectos. |
| 27 | RuntimeError | Se genera esta excepción cuando no se puede clasificar un error que ocurrió durante la ejecución del programa. |
| 28 | NotImplementedError | Si una función abstracta que el usuario debe definir en una clase heredada no está definida, se genera esta excepción. |

# Resumen

Aprendimos acerca de diferentes métodos para generar, capturar y manejar excepciones en Python después de comprender la distinción entre errores de sintaxis y excepciones. Aprendimos sobre estas cláusulas en este tutorial:

- Podemos generar una excepción en cualquier línea de código usando la palabra clave "raise".
- Utilizando la palabra clave "assert", podemos verificar si se cumple una condición específica y generar una excepción si no se cumple.
- Todas las declaraciones se ejecutan en la cláusula "try" hasta que se encuentra una excepción.
- Las excepciones de la cláusula "try" se detectan y manejan usando la función "except".
- Si no se generan excepciones en el bloque de código "try", podemos escribir código que se ejecutará en el bloque de código "else".

Aquí está la sintaxis de las cláusulas try, except, else y finally.

**Sintaxis:**

```bash
try:
# Bloque de código
# Estas declaraciones son aquellas que posiblemente puedan tener algún error

except:
# Este bloque es opcional.
# Si el bloque try encuentra una excepción, este bloque la manejará.

else:
# Si no hay excepciones, este bloque de código será ejecutado por el intérprete de Python

finally:
# El intérprete de Python siempre ejecutará este código.
```
