# Números

En Python, hay tres tipos numéricos:

- `int` (entero)
- `float` (punto flotante)
- `complex` (complejo)

Las variables de los tipos numéricos se crean cuando les asignas un valor.

**Ejemplo**:

```python
x = 1 # int
y = 2.8 # float
z = 1j # complex
```

Para verificar el tipo de cualquier objeto en Python, utiliza la función `type()`.

**Ejemplo**:

```python
print(type(x))
print(type(y))
print(type(z))
```

## Tipo Int (Entero)

Int, o entero, es un número entero, positivo o negativo, sin decimales y de longitud ilimitada.

**Ejemplo**:

```python
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
```

## Tipo Float (Punto Flotante)

Float, o "número de punto flotante", es un número, positivo o negativo, que contiene uno o más decimales.

**Ejemplo**:

```python
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
```

Los floats también pueden representar números científicos con una "e" para indicar la potencia de 10.

**Ejemplo**:

```python
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```

## Tipo Complex (Complejo)

Los números complejos se escriben con una "j" como parte imaginaria.

**Ejemplo**:

```python
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```

## Conversión de Tipos

Puedes convertir de un tipo a otro utilizando los métodos `int()`, `float()` y `complex()`.

**Ejemplo**:

```python
x = 1 # int
y = 2.8 # float
z = 1j # complex

# Convertir de int a float
a = float(x)

# Convertir de float a int
b = int(y)

# Convertir de int a complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```

> **Nota:** No puedes convertir números complejos a otro tipo de número.

## Número Aleatorio

Python no tiene una función `random()` para generar un número aleatorio, pero tiene un módulo incorporado llamado `random` que se puede utilizar para generar números aleatorios.

**Ejemplo**:

Importa el módulo random y muestra un número aleatorio entre 1 y 9.

```python
import random

print(random.randrange(1, 10))
```
