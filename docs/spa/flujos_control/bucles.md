# Bucles

A continuación, se presentan los bucles disponibles en Python para satisfacer las necesidades de repetición. Python ofrece 3 opciones para ejecutar los bucles. La funcionalidad básica de todas las técnicas es la misma, aunque la sintaxis y la cantidad de tiempo requerido para verificar la condición difieren.

Podemos ejecutar una sola declaración o un conjunto de declaraciones repetidamente usando un comando de bucle.

Los siguientes tipos de bucles están disponibles en el lenguaje de programación Python.

| Núm. | Nombre del bucle | Tipo de bucle y descripción |
| --- | --- | --- |
| 1 | Bucle while | Repite una declaración o grupo de declaraciones mientras una condición dada sea VERDADERA. Prueba la condición antes de ejecutar el cuerpo del bucle. |
| 2 | Bucle for | Este tipo de bucle ejecuta un bloque de código varias veces y abrevia el código que maneja la variable del bucle. |
| 3 | Bucles anidados | Podemos iterar un bucle dentro de otro bucle. |

## Declaraciones

Las declaraciones utilizadas para controlar los bucles y cambiar el curso de la iteración se llaman declaraciones de control. Todos los objetos producidos dentro del alcance local del bucle se eliminan cuando se completa la ejecución.

Python proporciona las siguientes declaraciones de control. Las discutiremos más adelante en detalle.

Repasemos rápidamente las definiciones de estas declaraciones de control de bucle.

| Núm. | Nombre de la declaración de control | Descripción |
| --- | --- | --- |
| 1 | Declaración break | Esta instrucción termina la ejecución del bucle y transfiere el control del programa a la siguiente declaración después del bucle. |
| 2 | Declaración continue | Esta instrucción omite la iteración actual del bucle. Las declaraciones que siguen a la declaración continue no se ejecutan una vez que el intérprete de Python llega a la declaración continue. |
| 3 | Declaración pass | Se utiliza la declaración pass cuando una declaración es sintácticamente necesaria, pero no se debe ejecutar ningún código. |

## El Bucle for

El bucle for de Python está diseñado para ejecutar repetidamente un bloque de código mientras itera a través de una lista, tupla, diccionario u otros objetos iterables de Python. El proceso de recorrer una secuencia se conoce como iteración.

**Sintaxis**:

```python
for valor in secuencia:
    { bloque de código }
```

En este caso, la variable "valor" se utiliza para contener el valor de cada elemento presente en la secuencia antes de que comience la iteración hasta que se complete esta iteración particular.

El bucle itera hasta que se llega al último elemento de la secuencia.

**Ejemplo**:

```python
# Programa en Python para mostrar cómo funciona el bucle for

# Creación de una secuencia que es una tupla de números

numeros = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]

# Variable para almacenar el cuadrado del número

cuadrado = 0

# Creación de una lista vacía

cuadrados = []

# Creación de un bucle for

for valor in numeros:
    cuadrado = valor ** 2
    cuadrados.append(cuadrado)

print("La lista de cuadrados es", cuadrados)
```

**Salida**:

```python
La lista de cuadrados es [16, 4, 36, 49, 9, 25, 64, 100, 36, 1, 81, 4]
```

### Uso de la Declaración "else" con el Bucle "for"

Como se ha dicho anteriormente, un bucle "for" ejecuta el bloque de código hasta que se alcance el elemento de la secuencia. La declaración "else" se escribe justo después de que se haya ejecutado el bucle "for" y después de que la ejecución del bucle "for" esté completa.

La declaración "else" solo se ejecuta si la ejecución se completa. No se ejecutará si salimos del bucle o si se produce un error.

Aquí hay un código para entender mejor las declaraciones "if-else".

**Ejemplo**:

```python
# Programa en Python para mostrar cómo funcionan las declaraciones if-else

cadena = "Bucle Python"

# Iniciando un bucle

for caracter in cadena:

    # dando una condición en el bloque "if"
    if caracter == "o":
        print("Bloque if")
    # si la condición no se cumple, entonces se ejecuta el bloque "else"
    else:
        print(caracter)
```

**Salida**:

```python
B
u
c
l
e
Bloque if
P
y
t
h
o
n
B
l
o
q
u
e

P
y
t
h
o
n
```

Ahora, de manera similar, usando "else" con el bucle "for".

**Sintaxis**:

```python
for valor in secuencia:

    # ejecuta las declaraciones hasta que las secuencias se agoten

else:

    # ejecuta estas declaraciones cuando el bucle "for" se haya completado
```

**Ejemplo**:

```python
# Programa en Python para mostrar cómo usar la declaración "else" con el bucle "for"

# Creación de una secuencia
tupla_ = (3, 4, 6, 8, 9, 2, 3, 8, 9, 7)

# Iniciando el bucle
for valor in tupla_:
    if valor % 2 != 0:
        print(valor)

    # dando una declaración "else"
    else:
        print("Estos son los números impares presentes en la tupla")
```

**Salida**:

```python
3
9
3
9
7
Estos son los números impares presentes en la tupla
```

### La Función range()

Con la ayuda de la función range(), podemos generar una serie de números. range(10) generará valores entre 0 y 9 (10 números).

Podemos proporcionar valores específicos de inicio, final y tamaño de paso de la siguiente manera: range(inicio, final, tamaño de paso). Si no se especifica el tamaño de paso, se establece en 1.

Dado que no crea cada valor que "contiene" después de construirlo, el objeto range se puede caracterizar como "lento". Proporciona acciones in, len y **getitem**, pero no es un iterador.

El siguiente ejemplo aclarará esto.

**Ejemplo**:

```python
# Programa en Python para mostrar cómo funciona la función range()

print(range(15))
print(list(range(15)))
print(list(range(4, 9)))
print(list(range(5, 25, 4)))
```

**Salida**:

```python
range(0, 15)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
[4, 5, 6, 7, 8]
[5, 9, 13, 17, 21]
```

Para iterar a través de una secuencia de elementos, podemos aplicar el método range() en bucles "for". Podemos usar la indexación para iterar a través de la secuencia dada combinándola con la función len() de un iterable. Aquí tienes una ilustración.

**Ejemplo**:

```python
# Programa en Python para iterar sobre una secuencia con la ayuda de la indexación

tupla_ = ("Python", "Bucles", "Secuencia", "Condición", "Rango")

# iterar sobre la tupla_ usando la función range()
for iterador in range(len(tupla_)):
    print(tupla_[iterador].upper())
```

**Salida**:

```python
PYTHON
BUCLES
SECUENCIA
CONDICIÓN
RANGO
```

## Bucle "While"

Los bucles "while" se utilizan en Python para iterar hasta que se cumpla una condición especificada. Sin embargo, la declaración en el programa que sigue al bucle "while" se ejecuta una vez que la condición cambia a falso.

**Sintaxis**:

```python
while <condición>:
    { bloque de código }
```

Todas las declaraciones de programación que siguen a un comando estructural definen un bloque de código. Estas declaraciones están destinadas con el mismo número de espacios. Python agrupa las declaraciones juntas con sangría.

**Ejemplo**:

```python
# Programa en Python para mostrar cómo usar un bucle "while"
contador = 0

# Iniciando el bucle
while contador < 10:  # dando la condición
    contador = contador + 3
    print("Bucles Python")
```

**Salida**:

```python
Bucles Python
Bucles Python
Bucles Python
Bucles Python
```

### Uso de la Declaración "else" con Bucles "while"

Como se discutió anteriormente en la sección del bucle "for", también podemos usar la declaración "else" con el bucle "while". Tiene la misma sintaxis.

**Ejemplo**:

```python
# Programa en Python para mostrar cómo usar la declaración "else" con el bucle "while"

contador = 0

# Iterando a través del bucle "while"
while contador < 10:
    contador = contador + 3
    print("Bucles Python")  # Ejecutado hasta que se cumpla la condición

# Una vez que la condición del bucle "while" sea Falsa, esta declaración se ejecutará
else:
    print("Bloque de código dentro de la declaración 'else'")
```

**Salida**:

```python
Bucles Python
Bucles Python
Bucles Python
Bucles Python
Bloque de código dentro de la declaración 'else'
```

### Bloque "while" de una Sola Declaración

El bucle se puede declarar en una sola declaración, como se ve a continuación. Esto es similar al bloque if-else, donde podemos escribir el bloque de código en una sola línea.

**Ejemplo**:

```python
# Programa en Python para mostrar cómo escribir un bucle "while" de una sola declaración

contador = 0

while (contador < 3): print("Bucles Python")
```

## Declaraciones de Control de Bucle

Ahora discutiremos en detalle las declaraciones de control de bucle. Veremos un ejemplo de cada declaración de control.

### Declaración "Continue"

Devuelve el control al comienzo del bucle.

**Ejemplo**:

```python
# Programa en Python para mostrar cómo funciona la declaración "continue"

# Iniciando el bucle
for caracter in "Bucles Python":
    if caracter == "o" or caracter == "p" or caracter == "t":
        continue

    print('Letra actual:', caracter)
```

**Salida**:

```python
Letra actual: B
Letra actual: u
Letra actual: c
Letra actual: l
Letra actual: e
Letra actual: s
Letra actual:
Letra actual: y
Letra actual: h
Letra actual: n
```

### Declaración "Break"

Detiene la ejecución del bucle cuando se alcanza la declaración "break".

**Ejemplo**:

```python
# Programa en Python para mostrar cómo funciona la declaración "break"

# Iniciando el bucle
for caracter in "Bucles Python":
    if caracter == 'l':
        break

    print('Letra actual:', caracter)
```

**Salida**:

```python
Letra actual:  B
Letra actual:  u
Letra actual:  c
Letra actual:  e
Letra actual:  s
Letra actual:
Letra actual:  P
Letra actual:  y
```

### Declaración "Pass"

Las declaraciones "pass" se utilizan para crear bucles vacíos. La declaración "pass" también se utiliza para clases, funciones y declaraciones de control vacías.

**Ejemplo**:

```python
# Programa en Python para mostrar cómo funciona la declaración "pass"

for caracter in "Bucles Python":
    pass

print('Última letra:', caracter)
```

**Salida**:

```python
Última letra: n
```
