# Bucles while

En la programación, los bucles están diseñados para ejecutar un bloque de código especificado repetidamente. Aprenderemos cómo construir un bucle "while" en Python, la sintaxis de un bucle "while", los controles de bucle como "break" y "continue", y otros ejercicios en este tutorial.

## Introducción a los Bucles "while"

La iteración de un bloque de código en el bucle "while" de Python se ejecuta siempre que la condición dada, es decir, la expresión_condicional, sea verdadera.

Si no sabemos cuántas veces ejecutaremos la iteración de antemano, podemos escribir un bucle indefinido.

**Sintaxis**:

```python
while expresión_condicional:
    Bloque de código del "while"
```

La condición dada, es decir, la expresión_condicional, se evalúa inicialmente en el bucle "while" de Python. Luego, si la expresión condicional devuelve un valor booleano Verdadero, se ejecutan las declaraciones del bucle "while". La expresión condicional se verifica nuevamente cuando se ejecuta por completo el bloque de código. Este procedimiento se repite hasta que la expresión condicional devuelva el valor booleano Falso.

- Las declaraciones del bucle "while" en Python están dictadas por la sangría.
- El bloque de código comienza cuando una declaración está sangrada y termina con la primera declaración sin sangría.
- Cualquier número distinto de cero en Python se interpreta como booleano Verdadero. Falso se interpreta como None y 0.

## Ejemplo de Bucle "while"

Aquí sumaremos los cuadrados de los primeros 15 números naturales usando un bucle "while".

**Ejemplo**:

```python
# Programa en Python de ejemplo para mostrar el uso del bucle "while"

num = 15

# inicializando la suma y un contador para la iteración

suma = 0
c = 1

while c <= num:  # especificando la condición del bucle
    # comenzando el bloque de código
    suma = c**2 + suma
    c = c + 1  # incrementando el contador

# imprimir la suma final
print("La suma de los cuadrados es", suma)
```

**Salida**:

```python
La suma de los cuadrados es 1240
```

Siempre que nuestro parámetro contador "c" devuelva verdadero para la condición "c" menor o igual a "num", el bucle ejecutará repetidamente el bloque de código "c" número de veces.

A continuación, un punto crucial (que a menudo se olvida). Debemos incrementar el valor del parámetro contador en las declaraciones del bucle. Si no lo hacemos, nuestro bucle "while" se ejecutará indefinidamente (un bucle infinito).

Finalmente, imprimimos el resultado usando la declaración print.

## Ejercicios de Bucle "while"

### Números Primos y Bucle "While"

Usando un bucle "while", construiremos un programa en Python para verificar si el entero dado es un número primo o no.

**Ejemplo**:

```python
num = [34, 12, 54, 23, 75, 34, 11]

def numero_primo(numero):
    condicion = 0
    iteracion = 2

    while iteracion <= numero / 2:
        if numero % iteracion == 0:
            condicion = 1
            break

        iteracion = iteracion + 1

    if condicion == 0:
        print(f"{numero} es un número PRIMO")
    else:
        print(f"{numero} no es un número PRIMO")

for i in num:
    numero_primo(i)
```

**Salida**:

```python
34 no es un número PRIMO
12 no es un número PRIMO
54 no es un número PRIMO
23 es un número PRIMO
75 no es un número PRIMO
34 no es un número PRIMO
11 es un número PRIMO
```

### Tabla de Multiplicar Usando el Bucle "while"

En este ejemplo, usaremos el bucle "while" para imprimir la tabla de multiplicar de un número dado.

**Ejemplo**:

```python
num = 21
contador = 1

# usaremos un bucle "while" para iterar 10 veces para la tabla de multiplicar

print("La Tabla de Multiplicar de:", num)

while contador <= 10:  # especificando la condición
    resultado = num * contador
    print(num, 'x', contador, '=', resultado)
    contador += 1  # expresión para incrementar el contador
```

**Salida**:

```python
La Tabla de Multiplicar de: 21
21 x 1 = 21
21 x 2 = 42
21 x 3 = 63
21 x 4 = 84
21 x 5 = 105
21 x 6 = 126
21 x 7 = 147
21 x 8 = 168
21 x 9 = 189
21 x 10 = 210
```

### Bucle "While" con una Lista

Usaremos un bucle "while" en Python para elevar al cuadrado cada número de una lista.

**Ejemplo**:

```python
# Programa en Python para elevar al cuadrado cada número de una lista

# inicializando una lista
lista = [3, 5, 1, 4, 6]
cuadrados = []

# programando un bucle "while"
while lista:  # hasta que la lista no esté vacía, esta expresión dará verdadero (True), después falso (False)
    cuadrados.append((lista.pop())**2)

# imprimir los cuadrados
print(cuadrados)
```

**Salida:**

```python
[36, 16, 1, 25, 9]
```

En el ejemplo anterior, ejecutamos un bucle "while" sobre una lista dada de enteros que se ejecutará repetidamente siempre que se encuentre un elemento en la lista.

## Bucle "While" con Múltiples Condiciones

Necesitaremos utilizar operadores lógicos para combinar dos o más expresiones que especifican condiciones en un solo bucle "while". Esto instruye a Python a analizar colectivamente todas las expresiones dadas de condiciones.

Podemos construir un bucle "while" con múltiples condiciones en este ejemplo. Hemos dado dos condiciones y la palabra clave "and", lo que significa que hasta que ambas condiciones den verdadero (True), el bucle ejecutará las declaraciones.

**Ejemplo**:

```python
num1 = 17
num2 = -12

while num1 > 5 and num2 < -5:  # múltiples condiciones en un solo bucle "while"
    num1 -= 2
    num2 += 3
    print((num1, num2))
```

**Salida**:

```python
(15, -9)
(13, -6)
(11, -3)
```

Veamos otro ejemplo de múltiples condiciones con el operador OR.

**Ejemplo**:

```python
num1 = 17
num2 = -12

while num1 > 5 or num2 < -5:
    num1 -= 2
    num2 += 3
    print((num1, num2))
```

**Salida**:

```python
(15, -9)
(13, -6)
(11, -3)
(9, 0)
(7, 3)
(5, 6)
```

También podemos agrupar múltiples expresiones lógicas en el bucle "while", como se muestra en este ejemplo.

**Ejemplo**:

```python
num1 = 9
num2 = 14
valor_maximo = 4
contador = 0

while (contador < num1 or contador < num2) and not contador >= valor_maximo:  # agrupando múltiples condiciones
    print(f"Número de iteraciones: {contador}")
    contador += 1
```

**Salida**:

```python
Número de iteraciones: 0
Número de iteraciones: 1
Número de iteraciones: 2
Número de iteraciones: 3
```

## Bucle "while" de una Sola Declaración

Similar a la sintaxis de la declaración "if", si nuestra cláusula "while" consiste en una sola declaración, puede escribirse en la misma línea que la palabra clave "while".

Aquí está la sintaxis y un ejemplo de una cláusula de una sola línea "while":

```python
# Programa en Python para mostrar cómo crear un bucle "while" de una sola declaración

contador = 1

while contador: print('Bucles While en Python')
```

## Declaraciones de Control de Bucle

Ahora discutiremos en detalle las declaraciones de control de bucle. Veremos un ejemplo de cada declaración de control.

### Declaración "continue"

Devuelve el control del intérprete de Python al inicio del bucle.

**Ejemplo**:

```python
# Programa en Python para mostrar cómo usar la declaración "continue" en el control de bucles

# Iniciando el bucle

for caracter in "Bucles While":
    if caracter == "o" or caracter == "i" or caracter == "e":
        continue
    print('Letra actual:', caracter)
```

**Salida:**

```python
Letra actual: B
Letra actual: u
Letra actual: c
Letra actual: l
Letra actual:
Letra actual: L
Letra actual: p
Letra actual: s
```

### Declaración "break"

Detiene la ejecución del bucle cuando se alcanza la declaración "break".

**Ejemplo**:

```python
# Programa en Python para mostrar cómo usar la declaración "break"

# Iniciando el bucle
for caracter in "Bucles Python":
    if caracter == 'n':
        break
    print('Letra actual:', caracter)
```

**Salida**:

```python
Letra actual:  P
Letra actual:  y
Letra actual:  t
Letra actual:  h
Letra actual:  o
```

### Declaración "pass"

Las declaraciones "pass" se utilizan para crear bucles vacíos. La declaración "pass" también se utiliza para clases, funciones y declaraciones de control vacías.

**Ejemplo**:

```python
# Programa en Python para mostrar cómo usar la declaración "pass"

for caracter in "Bucles While":
    pass

print('Última letra:', caracter)
```

**Salida**:

```python
Última letra: e
```
