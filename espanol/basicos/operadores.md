# Operadores

El operador es un símbolo que realiza una determinada operación entre dos operandos, según una definición. En un lenguaje de programación en particular, los operadores sirven como base sobre la cual se construye la lógica en un programa. A continuación se enumeran los diferentes operadores que ofrece Python.

- Operadores aritméticos
- Operadores de comparación
- Operadores de asignación
- Operadores lógicos
- Operadores a nivel de bits
- Operadores de pertenencia
- Operadores de identidad
- Operadores aritméticos

## Operadores Aritméticos

Las operaciones aritméticas entre dos operandos se llevan a cabo utilizando operadores aritméticos. Incluyen el operador de exponente `**` así como los operadores de suma `+`, resta `-`, multiplicación `*`, división `/`, módulo `%`, y división entera `//`.

Considera la siguiente tabla para una explicación detallada de los operadores aritméticos.

| Operador | Descripción |
| --- | --- |
| + (Suma) | Se utiliza para sumar dos operandos. Por ejemplo, si a = 10, b = 10 => a+b = 20 |
| - (Resta) | Se utiliza para restar el segundo operando del primer operando. Si el primer operando es menor que el segundo operando, el resultado es negativo. Por ejemplo, si a = 20, b = 5 => a - b = 15 |
| / (División) | Retorna el cociente de dividir el primer operando por el segundo operando. Por ejemplo, si a = 20, b = 10 => a/b = 2.0 |
| * (Multiplicación) | Se utiliza para multiplicar un operando por otro. Por ejemplo, si a = 20, b = 4 => a * b = 80 |
| % (Módulo) | Retorna el residuo de la división del primer operando por el segundo operando. Por ejemplo, si a = 20, b = 10 => a%b = 0 |
| ** (Exponente) | Calcula el valor del primer operando elevado a la potencia del segundo operando. |
| // (División entera) | Retorna el cociente entero de dividir el primer operando por el segundo operando. |

## Operadores de Comparación

Los operadores de comparación comparan los valores de dos operandos y retornan un valor booleano verdadero o falso de acuerdo a la comparación. La siguiente tabla lista los operadores de comparación.

| Operador | Descripción |
| --- | --- |
| == | Si el valor de dos operandos es igual, entonces la condición es verdadera. |
| != | Si el valor de dos operandos no es igual, entonces la condición es verdadera. |
| <= | La condición se cumple si el primer operando es menor o igual al segundo operando. |
| >= | La condición se cumple si el primer operando es mayor o igual al segundo operando. |
| > | Si el primer operando es mayor que el segundo operando, entonces la condición es verdadera. |
| < | Si el primer operando es menor que el segundo operando, entonces la condición es verdadera. |

## Operadores de Asignación

Los operadores de asignación se utilizan para asignar el valor de una expresión a un operando izquierdo. La siguiente tabla proporciona una descripción de los operadores de asignación.

| Operador | Descripción |
| --- | --- |
| = | Asigna el valor de la expresión de la derecha al operando izquierdo. |
| += | El operando izquierdo recibe un valor modificado al multiplicar el valor del operando derecho por el valor del operando izquierdo. Por ejemplo, si a = 10, b = 20 => a += b será igual a a = a + b y por lo tanto, a = 30. |
| -= | Disminuye el valor del operando izquierdo por el valor del operando derecho y asigna el valor modificado de nuevo al operando izquierdo. Por ejemplo, si a = 20, b = 10 => a -= b será igual a a = a - b y por lo tanto, a = 10. |
| *= | Multiplica el valor del operando izquierdo por el valor del operando derecho y asigna el valor modificado de nuevo al operando izquierdo. Por ejemplo, si a = 10, b = 20 => a *= b será igual a a = a * b y por lo tanto, a = 200. |
| %= | Divide el valor del operando izquierdo por el valor del operando derecho y asigna el residuo de la división nuevamente al operando izquierdo. Por ejemplo, si a = 20, b = 10 => a %= b será igual a a = a % b y por lo tanto, a = 0. |
| **= | a**=b será igual a a=ab, por ejemplo, si a = 4, b = 2, a=b asignará 4**2 = 16 a a. |
| //= | a//=b será igual a a = a//b, por ejemplo, si a = 4, b = 3, a//=b asignará 4//3 = 1 a a. |

## Operadores Bitwise

Los operadores a nivel de bits o bitwise procesan los valores de dos operandos bit a bit. Considera el siguiente ejemplo.

**Ejemplo:**

```python
if a = 7
   b = 6
then, binary (a) = 0111
    binary (b) = 0110

hence, a & b = 0011
      a | b = 0111
             a ^ b = 0100      
       ~ a = 1000
```

| Operador | Descripción |
| --- | --- |
| & (and binario) | Se copia un 1 al resultado si ambos bits en las mismas posiciones de los dos operandos son 1. En caso contrario, se copia un 0. |
| | (or binario) | El bit resultante será 0 si ambos bits son cero; de lo contrario, el bit resultante será 1. |
| ^ (xor binario) | Si los dos bits son diferentes, el bit resultante será 1, de lo contrario será 0. |
| ~ (negación) | Los bits del operando se calculan como sus negaciones, por lo que si un bit es 0, el siguiente bit será 1 y viceversa. |
| << (desplazamiento a la izquierda) | El valor del operando izquierdo se desplaza hacia la izquierda la cantidad de bits especificada por el operando derecho. |
| >> (desplazamiento a la derecha) | El operando izquierdo se desplaza hacia la derecha la cantidad de bits especificada por el operando derecho. |

## Operadores Lógicos

Los operadores lógicos se utilizan típicamente para evaluar expresiones y tomar decisiones. A continuación se presentan los operadores lógicos soportados por Python.

| Operador | Descripción |
| --- | --- |
| and | La condición también será verdadera si la expresión es verdadera. Si las dos expresiones a y b son verdaderas, entonces a y b deben ser verdaderas. |
| or | La condición será verdadera si una de las expresiones es verdadera. Si a y b son las dos expresiones, entonces a o b debe ser verdadera si a es verdadera y b es falsa. |
| not | Si una expresión a es verdadera, entonces not (a) será falsa y viceversa. |

## Operadores de Pertenencia

Los operadores de pertenencia se utilizan para verificar si un valor está presente en una estructura de datos de Python. El resultado es verdadero si el valor está en la estructura de datos; de lo contrario, devuelve `false`.

| Operador | Descripción |
| --- | --- |
| in | Si el primer operando no se encuentra en el segundo operando, se evalúa como verdadero (lista, tupla o diccionario). |
| not in | Si el primer operando no está presente en el segundo operando, la evaluación es verdadera (lista, tupla o diccionario). |

## Operadores de Identidad

| Operador | Descripción |
| --- | --- |
| is | Si las referencias en ambos lados apuntan al mismo objeto, se determina que es verdadero. |
| is not | Si las referencias en ambos lados no apuntan al mismo objeto, se determina que es verdadero. |

## Precedencia de Operadores

El orden en el que se examinan los operadores es crucial para entender cuál operador se debe considerar primero. A continuación se muestra una lista de las tablas de precedencia de los operadores de Python.

| Operador | Descripción |
| --- | --- |
| ** | Por encima de todos los demás operadores utilizados en la expresión, el operador de exponente tiene precedencia. |
| ~ + - | el signo menos, el signo más unario y la negación. |
| * / % // | la división entera, el módulo, la división y la multiplicación. |
| + - | Suma binaria y resta binaria. |
| >> << | Desplazamiento a la izquierda y desplazamiento a la derecha. |
| & | And binario. |
| ^ | Xor binario y or binario. |
| <= < > >= | Operadores de comparación (menor que, menor o igual que, mayor que, mayor o igual que). |
| <> == != | Operadores de igualdad. |
| = %= /= //= -= += *= **= | Operadores de asignación. |
| is is not | Operadores de identidad. |
| in not in | Operadores de pertenencia. |
| not or and | Operadores lógicos. |
