# Operadores

Los operadores se utilizan para realizar operaciones en variables y valores.

En el ejemplo siguiente, utilizamos el operador `+` para sumar dos valores.

#### Ejemplo

```python
print(10 + 5)
```

Python divide los operadores en los siguientes grupos:

- Operadores aritméticos
- Operadores de asignación
- Operadores de comparación
- Operadores lógicos
- Operadores de identidad
- Operadores de membresía
- Operadores bitwise

## Operadores Aritméticos

Los operadores aritméticos se utilizan con valores numéricos para realizar operaciones matemáticas comunes.

| Operador | Nombre | Ejemplo |
| --- | --- | --- |
| + | Adición | x + y |
| - | Sustracción | x - y |
| * | Multiplicación | x * y |
| / | División | x / y |
| % | Módulo | x % y |
| ** | Exponenciación | x ** y |
| // | División entera | x // y |

## Operadores de Asignación

Los operadores de asignación se utilizan para asignar valores a variables.

| Operador | Ejemplo | Igual Que |
| --- | --- | --- |
| = | x = 5 | x = 5 |
| += | x += 3 | x = x + 3 |
| -= | x -= 3 | x = x - 3 |
| *= | x *= 3 | x = x * 3 |
| /= | x /= 3 | x = x / 3 |
| %= | x %= 3 | x = x % 3 |
| //= | x //= 3 | x = x // 3 |
| **= | x **= 3 | x = x ** 3 |
| &= | x &= 3 | x = x & 3 |
| |= | x |= 3 | x = x | 3 |
| ^= | x ^= 3 | x = x ^ 3 |
| >>= | x >>= 3 | x = x >> 3 |
| <<= | x <<= 3 | x = x << 3 |

## Operadores de Comparación

Los operadores de comparación se utilizan para comparar dos valores.

| Operador | Nombre | Ejemplo |
| --- | --- | --- |
| == | Igual | x == y |
| != | No igual | x != y |
| > | Mayor que | x > y |
| < | Menor que | x < y |
| >= | Mayor o igual que | x >= y |
| <= | Menor o igual que | x <= y |

## Operadores Lógicos

Los operadores lógicos se utilizan para combinar declaraciones condicionales.

| Operador | Descripción | Ejemplo |
| --- | --- | --- |
| and | Devuelve True si ambas declaraciones son verdaderas | x < 5 and x < 10 |
| or | Devuelve True si una de las declaraciones es verdadera | x < 5 or x < 4 |
| not | Invierte el resultado, devuelve False si el resultado es verdadero | not(x < 5 and x < 10) |

## Operadores de Identidad

Los operadores de identidad se utilizan para comparar objetos, no si son iguales, sino si son realmente el mismo objeto, con la misma ubicación de memoria.

| Operador | Descripción | Ejemplo |
| --- | --- | --- |
| is | Devuelve True si ambas variables son el mismo objeto | x is y |
| is not | Devuelve True si ambas variables no son el mismo objeto | x is not y |

## Operadores de Membresía

Los operadores de membresía se utilizan para comprobar si una secuencia está presente en un objeto.

| Operador | Descripción | Ejemplo |
| --- | --- | --- |
| in | Devuelve True si una secuencia con el valor especificado está presente en el objeto | x in y |
| not in | Devuelve True si una secuencia con el valor especificado no está presente en el objeto | x not in y |

## Operadores Bitwise

Los operadores bitwise se utilizan para comparar números (binarios).

| Operador | Nombre | Descripción | Ejemplo |
| --- | --- | --- | --- |
| & | AND | Establece cada bit en 1 si ambos bits son 1 | x & y |
| | | OR | Establece cada bit en 1 si uno de los dos bits es 1 | x | y |
| ^ | XOR | Establece cada bit en 1 solo si uno de los dos bits es 1 | x ^ y |
| ~ | NOT | Invierte todos los bits | ~x |
| << | Desplazamiento hacia la izquierda con relleno de ceros | Desplazamiento hacia la izquierda empujando ceros desde la derecha y dejando caer los bits más a la izquierda | x << 2 |
| >> | Desplazamiento hacia la derecha con signo | Desplazamiento hacia la derecha empujando copias del bit más a la izquierda desde la izquierda y dejando caer los bits más a la derecha | x >> 2 |

## Precedencia de Operadores

La precedencia de operadores describe el orden en el que se realizan las operaciones.

#### Ejemplo

Los paréntesis tienen la mayor precedencia, lo que significa que las expresiones dentro de los paréntesis deben evaluarse primero.

```python
print((6 + 3) - (6 + 3))
```

#### Ejemplo

La multiplicación `*` tiene una precedencia más alta que la suma `+`, por lo que las multiplicaciones se evalúan antes que las sumas.

```python
print(100 + 5 * 3)
```

El orden de precedencia se describe en la siguiente tabla, comenzando por la mayor precedencia en la parte superior.

| Operador | Descripción |
| --- | --- |
| () | Paréntesis |
| ** | Exponenciación |
| +x -x ~x | Operadores unarios de suma, resta y bitwise NOT |
| * / // % | Multiplicación, división, división entera y módulo |
| + - | Suma y resta |
| << >> | Desplazamientos a la izquierda y a la derecha Bitwise |
| & | Bitwise AND |
| ^ | Bitwise XOR |
| | | Bitwise OR |
| == != > >= < <= is is not in not in | Operadores de comparación, identidad y membresía |
| not | NOT lógico |
| and | AND lógico |
| or | OR lógico |

Si dos operadores tienen la misma precedencia, la expresión se evalúa de izquierda a derecha.

#### Ejemplo

La suma `+` y la resta `-` tienen la misma precedencia, por lo que evaluamos la expresión de izquierda a derecha.

```python
print(5 + 4 - 7 + 3)
```