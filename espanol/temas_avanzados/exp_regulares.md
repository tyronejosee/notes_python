# Expresiones Regulares

Una expresión regular es un conjunto de caracteres con una sintaxis altamente especializada que podemos usar para encontrar o coincidir con otros caracteres o grupos de caracteres. En resumen, las expresiones regulares, o regex, se utilizan ampliamente en el mundo de UNIX.

## Importar el Módulo re

```python
# Importar el módulo re
import re
```

El módulo re en Python proporciona soporte completo para expresiones regulares de estilo Perl. El módulo re genera la excepción re.error siempre que ocurra un error al implementar o usar una expresión regular.

Revisaremos funciones cruciales utilizadas para trabajar con expresiones regulares.

Pero primero, un punto menor: ***muchas letras tienen un significado particular cuando se utilizan en una expresión regular llamada metacaracteres.***

La mayoría de los símbolos y caracteres coincidirán fácilmente. (Se puede habilitar una función sin distinción entre mayúsculas y minúsculas, lo que permitirá que esta expresión regular coincida con Python o PYTHON). Por ejemplo, la expresión regular 'check' coincidirá exactamente con la cadena 'check'.

Sin embargo, hay algunas excepciones a esta regla general; ciertos símbolos son metacaracteres especiales que no coinciden por sí mismos. En cambio, indican que deben comparar algo inusual o afectar otras partes de la expresión regular mediante la repetición o modificación de su significado.

## Metacaracteres o Caracteres Especiales

Como sugiere el nombre, hay algunos caracteres con significados especiales:

| Caracteres | Significado |
| --- | --- |
| . | Punto: coincide con cualquier carácter excepto el carácter de nueva línea. |
| ^ | Acento circunflejo: se utiliza para coincidir con el patrón desde el inicio de la cadena. (Comienza con) |
| $ | Signo de dólar: coincide con el final de la cadena antes del carácter de nueva línea. (Termina con) |
| * | Asterisco: coincide con cero o más ocurrencias de un patrón. |
| + | Signo más: se utiliza cuando queremos que un patrón coincida al menos una vez. |
| ? | Signo de interrogación: coincide con cero o una ocurrencia de un patrón. |
| {} | Llaves: coincide con el número exactamente especificado de ocurrencias de un patrón. |
| [] | Corchetes: define el conjunto de caracteres. |
| | | Barra vertical: coincide con cualquiera de los dos patrones definidos. |

## Secuencias Especiales

La capacidad de coincidir con diferentes conjuntos de símbolos será la primera característica que las expresiones regulares pueden lograr, que no era previamente posible con las técnicas de cadenas. Por otro lado, las regex no serían una mejora significativa si esa fuera su única capacidad adicional. También podemos definir que algunas secciones de la RE deben repetirse un número especificado de veces.

El primer metacaracter que examinaremos para ocurrencias recurrentes es *. En lugar de coincidir con el carácter real '*', * indica que la letra anterior puede coincidir 0 o más veces en lugar de exactamente una vez.

Por ejemplo, Ba*t coincidirá con 'bt' (cero caracteres 'a'), 'bat' (un carácter 'a'), 'baaat' (tres caracteres 'a'), etc.

Las repeticiones voraces, como *, hacen que el algoritmo de coincidencia intente replicar la RE tantas veces como sea posible. Si los elementos posteriores de la secuencia no coinciden, el algoritmo de coincidencia volverá a intentarlo con menos repeticiones.

Las Secuencias Especiales consisten en '\' seguido de un carácter listado a continuación. Cada carácter tiene un significado diferente.

| Carácter | Significado |
| --- | --- |
| \d | Coincide con cualquier dígito y es equivalente a [0-9]. |
| \D | Coincide con cualquier carácter que no sea un dígito y es equivalente a [^0-9]. |
| \s | Coincide con cualquier carácter de espacio en blanco y es equivalente a [\t\n\r\f\v]. |
| \S | Coincide con cualquier carácter excepto el carácter de espacio en blanco y es equivalente a [^\t\n\r\f\v]. |
| \w | Coincide con cualquier carácter alfanumérico y es equivalente a [a-zA-Z0-9]. |
| \W | Coincide con cualquier carácter que no sea alfanumérico y es equivalente a [^a-zA-Z0-9]. |
| \A | Coincide con el patrón definido al principio de la cadena. |
| \b | r"\bxt" - Coincide con el patrón al principio de una palabra en una cadena. r"xt\b" - Coincide con el patrón al final de una palabra en una cadena. |
| \B | Es el opuesto de \b. |
| \Z | Devuelve un objeto de coincidencia cuando el patrón se encuentra al final de la cadena. |

## Funciones de Expresiones Regulares (RegEx)

- ***compile***: Se utiliza para convertir un patrón regular en un objeto de expresión regular que se puede usar de varias formas para buscar patrones en una cadena.
- ***search***: Se utiliza para encontrar la primera ocurrencia de un patrón de regex en una cadena dada.
- ***match***: Comienza a buscar el patrón desde el inicio de la cadena.
- ***fullmatch***: Se utiliza para hacer coincidir toda la cadena con un patrón de regex.
- ***split***: Se utiliza para dividir la cadena según el patrón de regex.
- ***findall***: Se utiliza para encontrar todos los patrones no superpuestos en una cadena. Devuelve una lista de patrones coincidentes.
- ***finditer***: Devuelve un iterador que produce objetos de coincidencia.
- ***sub***: Devuelve una cadena después de sustituir la primera ocurrencia del patrón por el reemplazo.
- ***subn***: Funciona igual que 'sub'. Devuelve una tupla (nueva_cadena, num_de_sustituciones).
- ***escape***: Se utiliza para escapar caracteres especiales en un patrón.
- ***purge***: Se utiliza para limpiar la caché de expresiones regulares.

### 1. re.compile(patrón, flags=0)

Se utiliza para crear un objeto de expresión regular que puede usarse para buscar patrones en una cadena.

**Ejemplo:**

```python
# Importar el módulo re
import re

# Definir el patrón de RegEx
patrón = "increíble"

# Crear un objeto de RegEx
objeto_regex = re.compile(patrón)

# Cadena
texto = "¡Este tutorial es increíble!"

# Buscar el patrón en la cadena
objeto_coincidencia = objeto_regex.search(texto)

# Resultado
print("Objeto de coincidencia:", objeto_coincidencia)
```

**Salida:**

```bash
Objeto de coincidencia:
```

Esto es equivalente a:

| re_obj = re.compile(patrón)resultado = re_obj.search(cadena) | = | resultado = re.search(patrón, cadena) |
| --- | --- | --- |

> Nota: cuando se trata de usar objetos de expresiones regulares varias veces, la versión con re.compile() es mucho más eficiente.
> 

### 2. re.match(patrón, cadena, flags=0)

- Comienza a buscar el patrón desde el inicio de la cadena.
- Devuelve un objeto de coincidencia si se encuentra alguna coincidencia con información como inicio, fin, intervalo, etc.
- Devuelve un valor NULO en caso de que no se encuentre ninguna coincidencia.

**Parámetros:**

- **patrón:** esta es la expresión que se va a buscar. Debe ser una expresión regular.
- **cadena:** Esta es la cadena que se comparará con el patrón al inicio de la cadena.
- **flags:** se puede usar una OR bitwise (|) para expresar múltiples flags.

**Ejemplo:**

```python
# Importar el módulo re
import re

# Nuestro patrón
patrón = "hola"

# Devuelve un objeto de coincidencia si se encuentra, de lo contrario, nulo
coincidencia = re.match(patrón, "hola mundo")
print(coincidencia)  # Imprimir el objeto de coincidencia
print("Intervalo:", coincidencia.span())  # Devuelve la tupla (inicio, fin)
print("Inicio:", coincidencia.start())  # Devuelve el índice de inicio
print("Fin:", coincidencia.end())  # Devuelve el índice de fin
```

**Salida:**

```bash
Intervalo: (0, 4)
Inicio: 0
Fin: 4
```

Otro ejemplo de la implementación del método re.match() en Python.

- Las expresiones ".w*" y ".w*?" coincidirán con palabras que tengan la letra "w", y se ignorará cualquier cosa que no tenga la letra "w".
- El bucle for se utiliza en esta ilustración de re.match() de Python para inspeccionar las coincidencias para cada elemento de la lista de palabras.

**Ejemplo:**

```python
import re

cadena = "Aprender Python a través de tutoriales en javatpoint"
objeto_coincidencia = re.match(r'.w* (.w?) (.w*?)', cadena, re.M|re.I)

if objeto_coincidencia:

print("grupo de objeto de coincidencia: ", objeto_coincidencia.group())

print("grupo 1 de objeto de coincidencia: ", objeto_coincidencia.group(1))

print("grupo 2 de objeto de coincidencia: ", objeto_coincidencia.group(2))

else:

print("¡No se encontró ninguna coincidencia!")
```

**Salida:**

```bash
¡No se encontró ninguna coincidencia!
```

### 3. re.search(patrón, cadena, flags=0)

La función re.search() buscará la primera ocurrencia de una secuencia de expresión regular y la devolverá. A diferencia de re.match() de Python, verificará todas las filas de la cadena suministrada. Si se encuentra una coincidencia con el patrón, la función re.search() produce un objeto de coincidencia; de lo contrario, devuelve "nulo".

Para ejecutar la función search(), primero debemos importar el módulo Python re y luego ejecutar el programa. La "secuencia" y el "contenido" para comprobar desde nuestra cadena principal se pasan a la llamada Python re.search().

Aquí está la descripción de los parámetros -

**Patrón:** esta es la expresión que se va a buscar. Debe ser una expresión regular.

**Cadena:** La cadena proporcionada es aquella en la que se buscará el patrón en cualquier lugar dentro de ella.

**Flags:** Se puede utilizar una OR bitwise (|) para expresar múltiples flags. Estos son modificadores, y la siguiente tabla los enumera.

**Ejemplo:**

```python
import re

cadena = "Aprender Python a través de tutoriales en javatpoint";

objeto_búsqueda = re.search(r' .*t? (. * t?) (. * t?)', cadena)

if objeto_búsqueda:

print("Grupo de objeto de búsqueda: ", objeto_búsqueda.group())

print("Grupo 1 de objeto de búsqueda: ", objeto_búsqueda.group(1))

print("Grupo 2 de objeto de búsqueda: ", objeto_búsqueda.group(2))

else:

print("¡Nada encontrado!")
```

**Salida:**

```bash
Grupo de objeto de búsqueda:   Python a través de tutoriales en javatpoint
Grupo 1 de objeto de búsqueda:  en
Grupo 2 de objeto de búsqueda

:  javatpoint
```

### 4. re.sub(patrón, reemplazo, cadena, count=0, flags=0)

- Sustituye el patrón coincidente con el 'reemplazo' en la cadena.
- **patrón:** Es simplemente un patrón de regex a coincidir.
- **reemplazo:** reemplazo es el que reemplaza el patrón en la cadena.
- **count:** Este parámetro se utiliza para controlar el número de sustituciones.

**Ejemplo 1:**

```python
# Importar el módulo re

import re

# Definir los parámetros

patrón = "gustar"  # a reemplazar

reemplazo = "encantar"  # Reemplazo

texto = "Me gusta Javatpoint!"  # Cadena

# Devuelve una nueva cadena con el patrón sustituido

nuevo_texto = re.sub(patrón, reemplazo, texto)

# Resultado

print("Texto original:", texto)

print("Texto sustituido: ", nuevo_texto)
```

**Salida:**

```bash
Texto original: Me gusta Javatpoint!
Texto sustituido:  Me encanta Javatpoint!
```

En el ejemplo anterior, la función sub sustituye 'gustar' por 'encantar'.

**Ejemplo 2:** Sustituir 3 ocurrencias de un patrón.

```python
# Importar el módulo re

import re

# Definir los parámetros

patrón = "l"  # a reemplazar

reemplazo = "L"  # Reemplazo

texto = "Me gusta Javatpoint! También me gustan los tutoriales!"  # Cadena

# Devuelve una nueva cadena con el patrón sustituido

nuevo_texto = re.sub(patrón, reemplazo, texto, 3)

# Resultado

print("Texto original:", texto)

print("Texto sustituido:", nuevo_texto)
```

**Salida:**

```bash
Texto original: Me gusta Javatpoint! También me gustan los tutoriales!
Texto sustituido: Me gusta Javatpoint! También me guLstan los tutoriales!
```

Aquí, se sustituye las primeras tres ocurrencias de 'l' por "L" en la cadena.

### 5. re.subn(patrón, reemplazo, cadena, count=0, flags=0)

- El funcionamiento de subn es igual que el de la función sub.
- Devuelve una tupla (nueva_cadena, num_de_sustituciones)

**Ejemplo:**

```python
# Importar el módulo re

import re

# Definir los parámetros

patrón = "l"  # a reemplazar

reemplazo = "L"  # Reemplazo

texto = "Me gusta Javatpoint! También me gustan los tutoriales!"  # Cadena

# Devuelve una nueva cadena con el patrón sustituido

nuevo_texto = re.subn(patrón, reemplazo, texto, 3)

# Resultado

print("Texto original:", texto)

print("Texto sustituido:", nuevo_texto)
```

**Salida:**

```bash
Texto original: Me gusta Javatpoint! También me gustan los tutoriales!
Texto sustituido: ('Me gusta Javatpoint! TambiLn me guLstan los tutoriales!', 3)

```

En el programa anterior, la función subn sustituye las tres primeras ocurrencias de 'l' por "L" en la cadena y devuelve una tupla con la nueva cadena y el número de sustituciones.

### 6. re.fullmatch(patrón, cadena, flags=0)

- Hace coincidir toda la cadena con el patrón.
- Devuelve un objeto de coincidencia correspondiente.
- Devuelve None en caso de que no se encuentre ninguna coincidencia.
- Por otro lado, la función search() buscará solo la primera ocurrencia que coincida con el patrón.

**Ejemplo:**

```python
# Importar el módulo re

import re

# Cadena de ejemplo

linea = "Hola mundo";

# Usando re.fullmatch()

print(re.fullmatch("Hola", linea))

print(re.fullmatch("Hola mundo", linea))
```

**Salida:**

```bash
None
```

En el programa anterior, solo la cadena "Hola mundo" ha coincidido completamente con el patrón, no "Hola".

**Pregunta: ¿Cuándo usar re.findall()?**

***Respuesta:*** Supongamos que tenemos una línea de texto y queremos obtener todas las ocurrencias del contenido, entonces usamos la función re.findall() de Python. Buscará todo el contenido proporcionado.

### 7. re.finditer(patrón, cadena, flags=0)

- Devuelve un iterador que produce todas las coincidencias no superpuestas del patrón en una cadena.
- La cadena se analiza de izquierda a derecha.
- Devuelve las coincidencias en el orden en que se descubrieron.

**Ejemplo:**

```python
# Importar el módulo re

import re

# Cadena de ejemplo

linea = "Hola mundo. Estoy aquí!";

# Patrón de regex

patrón = r'[aeiou]'

# Usando re.finditer()

iterador = re.finditer(patrón, linea)

# Iterando el iterador
for i in iterador:
    print(i)
```

**Salida:**

- En este ejemplo, el patrón de regex r'[aeiou]' buscará todas las vocales en la cadena.
- Se imprimirán las coincidencias de vocales encontradas en la cadena.

### 8. re.split(patrón, cadena, maxsplit=0, flags=0)

- Divide la cadena según las ocurrencias del patrón.
- Si maxsplit es cero, entonces se produce el número máximo de divisiones.
- Si maxsplit es uno, entonces divide la cadena por la primera ocurrencia del patrón y devuelve la cadena restante como resultado final.

**Ejemplo:**

```python
# Importar el módulo re

import re

# Patrón

patrón = ' '

# Cadena de ejemplo

linea = "Aprender Python a través de tutoriales en javatpoint"

# Usando la función split para dividir la cadena después de ' '

resultado = re.split(patrón, linea)

# Imprimir el resultado

print("Cuando maxsplit = 0, resultado:", resultado)

# Cuando Maxsplit es uno

resultado = re.split(patrón, linea, maxsplit=1)

print("Cuando maxsplit = 1, resultado =", resultado)
```

**Salida:**

```bash
Cuando maxsplit = 0, resultado: ['Aprender', 'Python', 'a', 'través', 'de', 'tutoriales', 'en', 'javatpoint']
Cuando maxsplit = 1, resultado = ['Aprender', 'Python a través de tutoriales en javatpoint']
```

### 9. re.escape(patrón)

- Escapa el carácter especial en el patrón.
- La función escape se vuelve más importante cuando la cadena contiene metacaracteres de expresiones regulares.

**Ejemplo:**

```python
# Importar el módulo re

import re

# Patrón

patrón = '<https://www.javatpoint.com/>'

# Usando la función escape para escapar metacaracteres

resultado = re.escape(patrón)

# Imprimir el resultado

print("Resultado:", resultado)
```

**Salida:**

```bash
Resultado: <https://www>\\.javatpoint\\.com/
```

La función escape escapa el metacaracter '.' del patrón. Esto es útil cuando se desea tratar los metacaracteres como caracteres regulares para que coincidan con los caracteres reales.

### 10. re.purge()

La función purge no toma ningún argumento y simplemente limpia la caché de expresiones regulares.

**Ejemplo:**

```python
# Importar el módulo re

import re

# Definir algunas expresiones regulares

patrón1 = r'\\d+'

patrón2 = r'[a-z]+'

# Usar las expresiones regulares

print(re.search(patrón1, '123abc'))

print(re.search(patrón2, '123abc'))

# Limpiar la caché de expresiones regulares

re.purge()

# Usar las expresiones regulares nuevamente

print(re.search(patrón1, '456def'))

print(re.search(patrón2, '456def'))
```

**Salida:**

Después de usar patrón1 y patrón2 para buscar coincidencias en la cadena '123abc'.
Hemos limpiado la caché utilizando re.purge().
Hemos vuelto a usar patrón1 y patrón2 para buscar coincidencias en la cadena '456def'.
Dado que se ha limpiado la caché de expresiones regulares, las expresiones regulares se han vuelto a compilar y la búsqueda de coincidencias en '456def' se ha realizado con el nuevo objeto de expresión regular.

### Comparación entre Coincidencia y Búsqueda - re.match() vs. re.search()

Python tiene dos funciones principales de expresiones regulares: match y search. La función match busca una coincidencia solo donde comienza la cadena, mientras que la función search busca una coincidencia en cualquier lugar de la cadena.

**Ejemplo:**

```python
# Importar el módulo re

import re

# Cadena de ejemplo

linea = "Aprender Python a través de tutoriales en javatpoint"

# Usar la función match para coincidir con 'a través'

objeto_coincidencia = re.match( r'a través', linea, re.M|re.I)

if objeto_coincidencia:

    print("Grupo del objeto de coincidencia:", objeto_coincidencia)

else:

    print("¡No hay ninguna coincidencia!!")

# Usar la función search para buscar

objeto_busqueda = re.search( r'a través', linea, re.M|re.I)

if objeto_busqueda:

    print("Grupo del objeto de búsqueda:", objeto_busqueda)

else:

    print("¡No se encontró nada!!")
```

**Salida:**

```bash
¡No hay ninguna coincidencia!!
Grupo del objeto de búsqueda:
```

La función match verifica si la cadena comienza con 'a través' o no, y la función search verifica si hay 'a través' en la cadena o no.

### CONCLUSIÓN

El módulo re en Python admite expresiones regulares. Las expresiones regulares son una herramienta avanzada para el procesamiento de texto y la búsqueda de patrones. Podemos encontrar patrones en cadenas de texto utilizando el módulo re y dividir y reemplazar texto según patrones, entre otras cosas.

Además, no siempre es una buena idea usar el paquete re. Si solo estamos buscando una cadena fija o una clase de caracteres específica y no estamos aprovechando ninguna característica de re, como la bandera IGNORECASE, no sería necesario utilizar la capacidad completa de las expresiones regulares. Las cadenas ofrecen varias formas de realizar tareas con cadenas fijas y generalmente son considerablemente más rápidas que el solucionador de expresiones regulares más grande y más generalizado, porque la ejecución es un simple bucle C corto que ha sido optimizado para el trabajo.
