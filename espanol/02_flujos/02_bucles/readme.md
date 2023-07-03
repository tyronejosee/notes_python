# Bucles

Python tiene dos comandos de bucle primitivos:

- Bucles `while`
- Bucles `for`

## El Bucle while

Con el bucle `while` podemos ejecutar un conjunto de instrucciones mientras una condición sea verdadera.

#### Ejemplo

Imprimir `i` siempre que `i` sea menor que 6.

```python
i = 1
while i < 6:
    print(i)
    i += 1
```

> **Nota:** recuerda incrementar i, de lo contrario, el bucle continuará para siempre.
> 

El bucle `while` requiere que las variables relevantes estén listas, en este ejemplo necesitamos definir una variable de indexación, `i`, que establecemos en 1.

## La Declaración break

Con la declaración `break` podemos detener el bucle aunque la condición del `while` sea verdadera.

#### Ejemplo

Salir del bucle cuando `i` sea 3.

```python
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
```

## La Declaración continue

Con la declaración `continue` podemos detener la iteración actual y continuar con la siguiente.

#### Ejemplo

Continuar con la siguiente iteración si `i` es 3.

```python
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
```

## La Declaración else

Con la declaración `else` podemos ejecutar un bloque de código una vez que la condición ya no sea verdadera.

#### Ejemplo

Imprimir un mensaje una vez que la condición sea falsa.

```python
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i ya no es menor que 6")
```

## El Bucle for

Un bucle `for` se utiliza para iterar sobre una secuencia (que puede ser una lista, una tupla, un diccionario, un conjunto o una cadena de caracteres).

Esto es menos similar a la palabra clave `for` en otros lenguajes de programación y funciona más como un método iterador que se encuentra en otros lenguajes de programación orientados a objetos.

Con el bucle `for` podemos ejecutar un conjunto de instrucciones una vez para cada elemento de una lista, tupla, conjunto, etc.

#### Ejemplo

Imprimir cada fruta de una lista de frutas.

```python
frutas = ["manzana", "plátano", "cereza"]
for x in frutas:
    print(x)
```

El bucle `for` no requiere una variable de indexación para establecerse de antemano.

## Iterando a Través de una Cadena de Caracteres

Incluso las cadenas de caracteres son objetos iterables, ya que contienen una secuencia de caracteres.

#### Ejemplo

Recorrer las letras de la palabra "banana".

```python
for x in "banana":
    print(x)
```

## La Declaración break

Con la declaración `break` podemos detener el bucle antes de que haya iterado sobre todos los elementos.

#### Ejemplo

Salir del bucle cuando `x` sea "banana".

```python
frutas = ["manzana", "plátano", "cereza"]
for x in frutas:
    print(x)
    if x == "banana":
        break
```

#### Ejemplo

Salir del bucle cuando `x` sea "banana", pero esta vez la declaración `break` se coloca antes de la instrucción `print`.

```python
frutas = ["manzana", "plátano", "cereza"]
for x in frutas:
    if x == "banana":
        break
    print(x)
```

## La Declaración continue

Con la declaración `continue` podemos detener la iteración actual del bucle y continuar con la siguiente.

#### Ejemplo

No imprimir "plátano".

```python
frutas = ["manzana", "plátano", "cereza"]
for x in frutas:
    if x == "banana":
        continue
    print(x)
```

## La Función range()

Para iterar un número específico de veces, podemos usar la función `range()`.

La función `range()` devuelve una secuencia de números que comienza desde 0 de forma predeterminada, se incrementa en 1 (por defecto) y termina en un número especificado.

#### Ejemplo

Usando la función `range()`.

```python
for x in range(6):
    print(x)
```

> **Nota:** range(6) no incluye los valores del 0 al 6, sino los valores del 0 al 5.
> 

La función `range()` tiene un valor de inicio predeterminado de 0, pero es posible especificar el valor de inicio agregando un parámetro: `range(2, 6)`, lo que significa valores del 2 al 6 (sin incluir el 6):

#### Ejemplo

Usando el parámetro de inicio.

```python
for x in range(2, 6):
    print(x)
```

La función `range()` incrementa la secuencia en 1 de forma predeterminada, pero es posible especificar el valor de incremento agregando un tercer parámetro: `range(2, 30, 3)`.

#### Ejemplo

Incrementar la secuencia en 3 (el valor predeterminado es 1).

```python
for x in range(2, 30, 3):
    print(x)
```

## El Bloque else en un Bucle for

La palabra clave `else` en un bucle `for` especifica un bloque de código que se ejecutará cuando el bucle haya terminado.

#### Ejemplo

Imprimir todos los números del 0 al 5 y mostrar un mensaje cuando el bucle haya terminado.

```python
for x in range(6):
    print(x)
else:
    print("¡Finalmente terminado!")
```

> **Nota:** el bloque else NO se ejecutará si el bucle se detiene con una declaración break.
> 

#### Ejemplo

Interrumpir el bucle cuando `x` sea 3 y ver qué sucede con el bloque `else`.

```python
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("¡Finalmente terminado!")
```

## Bucles Anidados

Un bucle anidado es un bucle dentro de otro bucle.

El "bucle interno" se ejecutará una vez por cada iteración del "bucle externo".

#### Ejemplo

Imprimir cada adjetivo para cada fruta.

```python
adjetivos = ["roja", "grande", "sabrosa"]
frutas = ["manzana", "plátano", "cereza"]

for adjetivo in adjetivos:
    for fruta in frutas:
        print(adjetivo, fruta)
```

## La Declaración pass

Los bucles `for` no pueden estar vacíos, pero si por alguna razón tienes un bucle `for` sin contenido, puedes utilizar la declaración `pass` para evitar obtener un error.

#### Ejemplo

```python
for x in [0, 1, 2]:
    pass
```
