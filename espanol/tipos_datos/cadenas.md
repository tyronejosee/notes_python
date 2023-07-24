# Cadenas

Hasta ahora, hemos discutido los números como los tipos de datos estándar en Python. En esta sección del tutorial, discutiremos el tipo de dato más popular en Python, es decir, la cadena (string).

Una cadena en Python es una colección de caracteres rodeada por comillas simples, comillas dobles o comillas triples. La computadora no entiende los caracteres; internamente, almacena los caracteres manipulados como combinación de 0's y 1's.

Cada carácter está codificado en el conjunto de caracteres ASCII o Unicode. Por lo tanto, podemos decir que las cadenas de Python también se denominan colecciones de caracteres Unicode.

En Python, las cadenas se pueden crear encerrando el carácter o la secuencia de caracteres entre comillas. Python nos permite usar comillas simples, comillas dobles o comillas triples para crear la cadena.

Considera el siguiente ejemplo en Python para crear una cadena.

**Sintaxis:**

```python
str = "Hola Python!"
```

Aquí, si verificamos el tipo de la variable **str** usando un script de Python

```python
print(type(str)), entonces imprimirá una cadena (str).
```

En Python, las cadenas se tratan como secuencias de caracteres, lo que significa que Python no admite el tipo de dato de carácter; en cambio, un solo carácter escrito como 'p' se trata como una cadena de longitud 1.

## Creación de Cadenas

Podemos crear una cadena encerrando los caracteres entre comillas simples o comillas dobles. Python también proporciona comillas triples para representar la cadena, pero generalmente se usa para cadenas multilinea o **docstrings**.

```python
# Usando comillas simples
str1 = 'Hola Python'
print(str1)

# Usando comillas dobles
str2 = "Hola Python"
print(str2)

# Usando comillas triples
str3 = '''''Las comillas triples se utilizan generalmente para
representar cadenas multilínea o
docstrings'''
print(str3)
```

**Salida:**

```bash
Hola Python
Hola Python
Las comillas triples se utilizan generalmente para
representar cadenas multilínea o
docstrings
```

## Indexación y división de cadenas

Al igual que en otros lenguajes, la indexación de las cadenas de Python comienza desde 0. Por ejemplo, la cadena "HELLO" se indexa como se muestra en la siguiente figura.

![https://static.javatpoint.com/python/images/strings-indexing-and-splitting.png](https://static.javatpoint.com/python/images/strings-indexing-and-splitting.png)

**Ejemplo:**

```python
str = "HELLO"

print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])

# Devuelve IndexError porque el índice 6 no existe
print(str[6])
```

**Salida:**

```bash
H
E
L
L
O
IndexError: string index out of range
```

Como se muestra en Python, el operador de segmento [] se utiliza para acceder a los caracteres individuales de la cadena. Sin embargo, podemos usar el operador : (dos puntos) en Python para acceder a la subcadena de la cadena dada. Considera el siguiente ejemplo.

![https://static.javatpoint.com/python/images/strings-indexing-and-splitting2.png](https://static.javatpoint.com/python/images/strings-indexing-and-splitting2.png)

Aquí, debemos notar que el rango superior dado en el operador de segmento siempre es exclusivo, es decir, si se da str = 'HELLO', entonces str[1:3] incluirá siempre str[1] = 'E', str[2] = 'L' y nada más.

**Ejemplo:**

```python
# Cadena dada
str = "JAVATPOINT"

# Desde el índice 0 hasta el final
print(str[0:])

# Desde el índice 1 hasta el índice 4
print(str[1:5])

# Desde el índice 2 hasta el índice 3
print(str[2:4])

# Desde el índice 0 hasta el índice 2
print(str[:3])

# Desde el índice 4 hasta el índice 6
print(str[4:7])
```

**Salida:**

```bash
JAVATPOINT
AVAT
VA
JAV
TPO
```

Podemos hacer el corte negativo en la cadena; comienza desde el carácter más a la derecha, que se indica como -1. El segundo índice más a la derecha indica -2, y así sucesivamente. Considera la siguiente imagen.

![https://static.javatpoint.com/python/images/strings-indexing-and-splitting3.png](https://static.javatpoint.com/python/images/strings-indexing-and-splitting3.png)

**Ejemplo:**

```python
str = 'JAVATPOINT'

print(str[-1])
print(str[-3])
print(str[-2:])
print(str[-4:-1])
print(str[-7:-2])

# Invirtiendo la cadena dada
print(str[::-1])

print(str[-12])
```

**Salida:**

```bash
T
I
NT
OIN
ATPOI
TNIOPTAVAJ
IndexError: string index out of range
```

## Reasignación de Cadenas

Actualizar el contenido de las cadenas es tan fácil como asignarlo a una nueva cadena. El objeto de cadena no admite la asignación de elementos, es decir, una cadena solo se puede reemplazar con una nueva cadena, ya que su contenido no se puede reemplazar parcialmente. Las cadenas son inmutables en Python.

**Ejemplo:**

```python
str = "HELLO"

str[0] = "h"

print(str)
```

**Salida:**

```bash
Traceback (most recent call last):
  File "12.py", line 2, in <module>
    str[0] = "h";
TypeError: 'str' object does not support item assignment
```

Sin embargo, en el ejemplo 1, la cadena **str** puede asignarse completamente a un nuevo contenido como se especifica en el siguiente ejemplo.

**Ejemplo:**

```python
str = "HELLO"

print(str)

str = "hello"

print(str)
```

**Salida:**

```bash
HELLO
hello
```

## Eliminando la Cadena

Como sabemos, las cadenas son inmutables. No podemos eliminar o eliminar caracteres de la cadena. Pero podemos eliminar toda la cadena usando la palabra clave **del**.

**Ejemplo:**

```python
str = "JAVATPOINT"

del str[1]
```

**Salida:**

```bash
TypeError: el objeto 'str' no admite eliminación de elementos
```

Ahora, estamos eliminando toda la cadena.

**Ejemplo:**

```python
str1 = "JAVATPOINT"

del str1

print(str1)
```

**Salida:**

```bash
NameError: el nombre 'str1' no está definido
```

## Operadores de Cadenas

| Operador | Descripción |
| --- | --- |
| + | Es conocido como operador de concatenación, se utiliza para unir las cadenas dadas a ambos lados del operador. |
| * | Es conocido como operador de repetición. Concatena múltiples copias de la misma cadena. |
| [] | Es conocido como operador de segmento. Se utiliza para acceder a las subcadenas de una cadena específica. |
| [:] | Es conocido como operador de segmento de rango. Se utiliza para acceder a los caracteres del rango especificado. |
| in | Es conocido como operador de pertenencia. Devuelve verdadero si una subcadena específica está presente en la cadena especificada. |
| not in | También es un operador de pertenencia y hace lo contrario de "in". Devuelve verdadero si una subcadena específica no está presente en la cadena especificada. |
| r/R | Se utiliza para especificar una cadena sin procesar. Las cadenas sin procesar se usan en casos donde necesitamos imprimir el significado real de los caracteres de escape, como "C://python". Para definir una cadena como una cadena sin procesar, el carácter r o R va seguido de la cadena. |
| % | Se utiliza para realizar el formateo de cadenas. Utiliza los especificadores de formato utilizados en programación C como %d o %f para mapear sus valores en Python. Discutiremos cómo se realiza el formateo en Python. |

**Ejemplo:**

Considera el siguiente ejemplo para entender el uso real de los operadores de Python.

```python
str = "Hola"
str1 = " mundo"

print(str * 3)  # imprime HolaHolaHola
print(str + str1)  # imprime Hola mundo
print(str[4])  # imprime o
print(str[2:4])  # imprime ll
print('w' in str)  # imprime False, ya que w no está presente en str
print('wo' not in str1)  # imprime False, ya que wo está presente en str1.
print(r'C://python37')  # imprime C://python37 tal y como está escrito
print("La cadena str : %s" % (str))  # imprime La cadena str : Hola
```

**Salida:**

```bash
HolaHolaHola
Hola mundo
o
ll
False
False
C://python37
La cadena str : Hola
```

## Formateo de Cadenas

### Secuencia de Escape

Supongamos que necesitamos escribir el siguiente texto: "Ellos dijeron, 'Hola, ¿qué está pasando?'" - esta declaración puede ser escrita usando comillas simples o comillas dobles, pero generará un **SyntaxError** ya que contiene tanto comillas simples como comillas dobles.

**Ejemplo:**

Consideremos el siguiente ejemplo para entender el uso real de los operadores de Python.

```python
str = "Ellos dijeron, \\"Hola, ¿qué está pasando?\\""

print(str)
```

**Salida:**

```bash
SyntaxError: sintaxis no válida
```

Podemos utilizar comillas triples para solucionar este problema, pero Python proporciona la secuencia de escape.

El símbolo de barra invertida (\) denota la secuencia de escape. La barra invertida puede ir seguida de un carácter especial y se interpreta de manera diferente. Las comillas simples dentro de la cadena deben ser escapadas. Podemos aplicar lo mismo a las comillas dobles.

**Ejemplo:**

```python
# usando comillas triples
print('''Ellos dijeron, "¿Qué hay?"''')

# escapando comillas simples
print('Ellos dijeron, "¿Qué está pasando?"')

# escapando comillas dobles
print("Ellos dijeron, \\"¿Qué está pasando?\\"")
```

**Salida:**

```bash
Ellos dijeron, "¿Qué hay?"
Ellos dijeron, "¿Qué está pasando?"
Ellos dijeron, "¿Qué está pasando?"
```

La lista de secuencias de escape se proporciona a continuación:

| Núm. | Secuencia de Escape | Descripción | Ejemplo |
| --- | --- | --- | --- |
| 1. | \newline | Ignora el salto de línea. | print("Python1 \ |
| Python2 \ |  |  |  |
| Python3")Salida: |  |  |  |

Python1 Python2 Python3 |
| 2. | \\ | Barra invertida | print("\\")Salida:

\ |
| 3. | \' | Comillas simples | print('\'')Salida:

' |
| 4. | \\" | Comillas dobles | print("\"")Salida:

" |
| 5. | \a | Timbre ASCII | print("\a") |
| 6. | \b | Retroceso ASCII (BS) | print("Hola \b Mundo")Salida:

Hola Mundo |
| 7. | \f | Avance de página ASCII | print("Hola \f Mundo!")
Hola  Mundo! |
| 8. | \n | Salto de línea ASCII | print("Hola \n Mundo!")Salida:

Hola
Mundo! |
| 9. | \r | Retorno de carro ASCII (CR) | print("Hola \r Mundo!")Salida:

Mundo! |
| 10. | \t | Tabulación horizontal ASCII | print("Hola \t Mundo!")Salida:

Hola 	 Mundo! |
| 11. | \v | Tabulación vertical ASCII | print("Hola \v Mundo!")Salida:

Hola
Mundo! |
| 12. | \ooo | Carácter con valor octal | print("\110\145\154\154\157")

Salida:

Hello |
| 13 | \xHH | Carácter con valor hexadecimal | print("\x48\x65\x6c\x6c\x6f")Salida:

Hello |

Aquí tienes un ejemplo sencillo de secuencia de escape:

```python
print("C:\\\\Users\\\\DEVANSH SHARMA\\\\Python32\\\\Lib")

print("This is the \\n multiline quotes")

print("This is \\x48\\x45\\x58 representation")
```

**Salida:**

```bash
C:\\Users\\DEVANSH SHARMA\\Python32\\Lib
This is the
 multiline quotes
This is HEX representation
```

Podemos ignorar la secuencia de escape de la cadena dada utilizando una cadena cruda (raw string). Podemos hacer esto escribiendo **r** o **R** delante de la cadena. Considera el siguiente ejemplo:

```python
print(r"C:\\\\Users\\\\DEVANSH SHARMA\\\\Python32")
```

**Salida:**

```bash
C:\\\\Users\\\\DEVANSH SHARMA\\\\Python32
```

## El método format()

El método **format()** es el método más flexible y útil para formatear cadenas. Las llaves {} se utilizan como marcadores de posición en la cadena y se reemplazan por los argumentos del método **format()**. Veamos un ejemplo:

```python
# Usando llaves

print("{} y {} son los mejores amigos".format("Devansh", "Abhishek"))

# Argumentos posicionales

print("{1} y {0} son los mejores jugadores".format("Virat", "Rohit"))

# Argumentos por palabras clave

print("{a}, {b}, {c}".format(a="James", b="Peter", c="Ricky"))
```

**Salida:**

```bash
Devansh y Abhishek son los mejores amigos
Rohit y Virat son los mejores jugadores
James, Peter, Ricky
```

## Formateo de cadenas utilizando el operador %

Python nos permite utilizar los especificadores de formato utilizados en la instrucción printf de C. Los especificadores de formato en Python se tratan de la misma manera que en C. Sin embargo, Python proporciona un operador adicional %, que se utiliza como una interfaz entre los especificadores de formato y sus valores. En otras palabras, podemos decir que vincula los especificadores de formato a los valores.

**Ejemplo:**

```python
Integer = 10;
Float = 1.290
String = "Devansh"

print("Hola, soy un entero... Mi valor es %d\\nHola, soy un flotante... Mi valor es %f\\nHola, soy una cadena... Mi valor es %s" % (Integer, Float, String))
```

**Salida:**

```bash
Hola, soy un entero... Mi valor es 10
Hola, soy un flotante... Mi valor es 1.290000
Hola, soy una cadena... Mi valor es Devansh
```

## Funciones de Cadenas

Python proporciona varias funciones incorporadas que se utilizan para el manejo de cadenas. A continuación, se presentan algunas de las funciones de cadenas más comunes junto con sus descripciones:

| Método | Descripción |
| --- | --- |
| capitalize() | Capitaliza el primer carácter de la cadena. Esta función está en desuso en Python 3. |
| casefold() | Devuelve una versión de la cadena adecuada para comparaciones sin distinción entre mayúsculas y minúsculas. |
| center(width[, fillchar]) | Devuelve una cadena con espacios rellenados, donde la cadena original está centrada con un número igual de espacios a la izquierda y a la derecha. |
| count(sub[, start[, end]]) | Cuenta el número de ocurrencias de una subcadena en una cadena entre los índices de inicio y fin. |
| decode(encoding='UTF8', errors='strict') | Decodifica la cadena usando el códec registrado para la codificación. |
| encode(encoding='UTF8', errors='strict') | Codifica la cadena usando el códec registrado para la codificación. La codificación predeterminada es 'utf-8'. |
| endswith(suffix[, start[, end]]) | Devuelve un valor booleano si la cadena termina con el sufijo dado entre los índices de inicio y fin. |
| expandtabs(tabsize=8) | Define las tabulaciones en la cadena como múltiples espacios. El valor predeterminado es 8 espacios. |
| find(sub[, start[, end]]) | Devuelve el índice donde se encuentra la subcadena en la cadena entre los índices de inicio y fin. Si no se encuentra la subcadena, devuelve -1. |
| format(*args, **kwargs) | Devuelve una versión formateada de la cadena usando los valores pasados como argumentos. |
| index(sub[, start[, end]]) | Devuelve el índice donde se encuentra la subcadena en la cadena entre los índices de inicio y fin. Si no se encuentra la subcadena, genera una excepción. Funciona de manera similar al método find(). |
| isalnum() | Devuelve True si todos los caracteres de la cadena son alfanuméricos, es decir, letras o números, y si hay al menos un carácter. De lo contrario, devuelve False. |
| isalpha() | Devuelve True si todos los caracteres de la cadena son letras y si hay al menos un carácter. De lo contrario, devuelve False. |
| isdecimal() | Devuelve True si todos los caracteres de la cadena son dígitos decimales. De lo contrario, devuelve False. |
| isdigit() | Devuelve True si todos los caracteres de la cadena son dígitos y si hay al menos un carácter. De lo contrario, devuelve False. |
| isidentifier() | Devuelve True si la cadena es un identificador válido. |
| islower() | Devuelve True si todos los caracteres de la cadena están en minúsculas y si hay al menos un carácter. De lo contrario, devuelve False. |
| isnumeric() | Devuelve True si todos los caracteres de la cadena son numéricos. De lo contrario, devuelve False. |
| isprintable() | Devuelve True si todos los caracteres de la cadena son imprimibles o si la cadena está vacía, de lo contrario, devuelve False. |
| isspace() | Devuelve True si todos los caracteres de la cadena son espacios en blanco y si hay al menos un carácter. De lo contrario, devuelve False. |
| istitle() | Devuelve True si la cadena está en formato de título y si hay al menos un carácter. De lo contrario, devuelve False. Una cadena en formato de título tiene la primera letra de cada palabra en mayúsculas y las demás en minúsculas. |
| isupper() | Devuelve True si todos los caracteres de la cadena están en mayúsculas y si hay al menos un carácter. De lo contrario, devuelve False. |
| join(iterable) | Une las representaciones de cadenas de los elementos en el iterable con la cadena como separador. |
| len(string) | Devuelve la longitud de la cadena. |
| ljust(width[, fillchar]) | Devuelve una cadena con espacios rellenados a la izquierda para alcanzar el ancho especificado. |
| lower() | Convierte todos los caracteres de la cadena a minúsculas. |
| lstrip([chars]) | Elimina todos los espacios en blanco delanteros de la cadena. Si se proporcionan los caracteres, también los elimina delanteros de la cadena. |
| partition(sep) | Busca el separador sep en la cadena y devuelve la parte antes de él, el separador en sí mismo y la parte después de él. Si no se encuentra el separador, devuelve la cadena original y dos cadenas vacías. |
| maketrans() | Devuelve una tabla de traducción que se utiliza en la función translate. |
| replace(old, new[, count]) | Devuelve una copia de la cadena con todas las apariciones de la subcadena old reemplazadas por la subcadena new. Si el parámetro count está presente, solo se reemplazan las primeras apariciones count. |
| rfind(sub[, start[, end]]) | Devuelve el índice más alto donde se encuentra la subcadena en la cadena entre los índices de inicio y fin. Si no se encuentra la subcadena, devuelve -1. |
| rindex(sub[, start[, end]]) | Devuelve el índice más alto donde se encuentra la subcadena en la cadena entre los índices de inicio y fin. Si no se encuentra la subcadena, genera una excepción. Funciona de manera similar al método rfind(). |
| rjust(width[, fillchar]) | Devuelve una cadena con espacios rellenados a la derecha para alcanzar el ancho especificado. |
| rstrip([chars]) | Elimina todos los espacios en blanco posteriores de la cadena. Si se proporcionan los caracteres, también los elimina finales de la cadena. |
| rsplit([sep[, maxsplit]]) | Es similar a split() pero procesa la cadena desde la dirección inversa. Devuelve una lista de palabras en la cadena. Si no se especifica el separador, la cadena se divide según los espacios en blanco. |
| split([sep[, maxsplit]]) | Divide la cadena según el delimitador sep. Si no se proporciona el delimitador, la cadena se divide según los espacios en blanco. Devuelve una lista de subcadenas concatenadas con el delimitador. |
| splitlines([keepends]) | Divide la cadena en líneas de salto de línea. Devuelve una lista de líneas en la cadena, si hay saltos de línea en la cadena. Si no hay saltos de línea, devuelve la cadena. |
| startswith(prefix[, start[, end]]) | Devuelve un valor booleano si la cadena comienza con el prefijo dado entre los índices de inicio y fin. |
| strip([chars]) | Realiza lstrip() y rstrip() en la cadena. Si se proporcionan los caracteres, también los elimina de los extremos de la cadena. |
| swapcase() | Invierte el caso de todos los caracteres en una cadena. |
| title() | Convierte la cadena al formato de título, donde la primera letra de cada palabra está en mayúscula y el resto en minúscula. |
| translate(table) | Traduce la cadena según la tabla de traducción proporcionada. |
| upper() | Convierte todos los caracteres de la cadena a mayúsculas. |
| zfill(width) | Devuelve la cadena original con ceros agregados a la izquierda hasta alcanzar el ancho total especificado. Se utiliza principalmente para números, zfill() conserva cualquier signo dado (menos un cero). |
| rpartition(sep) | Busca el separador sep en la cadena y devuelve la parte antes de él, el separador en sí mismo y la parte después de él. Si no se encuentra el separador, devuelve la cadena original y dos cadenas vacías. |