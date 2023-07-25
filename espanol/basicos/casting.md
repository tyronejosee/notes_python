# Conversión de Tipos (Casting)

En este tutorial, aprenderemos cómo se realiza la conversión de tipos en Python.

Nos encontramos con diferentes tipos de operaciones aritméticas en las que se involucran múltiples tipos de datos y luego se obtienen resultados en consecuencia.

Aquí discutiremos ambos:

1. Conversión de tipo implícito
2. Conversión de tipo explícito

Entendámoslos con la ayuda de programas:

## Conversión de Tipo Implícito

Durante la conversión de tipo implícito, el usuario no necesita mencionar ningún tipo de datos específico durante la conversión.

El siguiente programa ilustra cómo se puede hacer en Python.

**Ejemplo:**

```bash
# Programa para demostrar la conversión de tipo implícito

# Inicializando el valor de a

a = 10

print(a)

print("El tipo de a es ", type(a))

# Inicializando el valor de b

b = 4.5

print(b)

print("El tipo de b es ", type(b))

# Inicializando el valor de c

c = 4.0

print(c)

print("El tipo de c es ", type(c))

# Inicializando el valor de d

d = 5.0

print(d)

print("El tipo de d es ", type(d))

# Realizando operaciones aritméticas

res = a * b

print("El producto de a y b es ", res)

add = c + d

print("La suma de c y d es ", add)

```

**Salida:**

```bash
10
El tipo de a es <class 'int'>
4.5
El tipo de b es <class 'float'>
4.0
El tipo de c es <class 'float'>
5.0
El tipo de d es <class 'float'>
El producto de a y b es 45.0
La suma de c y d es 9.0

```

**Explicación:**

Echemos un vistazo a la explicación de este programa.

1. Para verificar cómo se convierten los valores al realizar las operaciones, hemos inicializado los valores de a, b, c y d.
2. Luego, hemos verificado el tipo de datos de cada uno de ellos.
3. Finalmente, hemos realizado una suma en las variables a y b y una multiplicación en las variables c y d.
4. Al ejecutar el programa anterior, podemos observar que en el caso del producto, el resultado final es un valor flotante (a era un entero y b era un flotante).

Ahora, es hora de pasar a la siguiente cosa que es la conversión de tipo explícito.

## Conversión de Tipo Explícito

En este tipo de conversión, el usuario debe pasar el valor en una función para obtener el tipo de datos requerido.

int(), float() y str() se utilizan principalmente para la conversión de tipo explícito.

**Ejemplo:**

```bash
# Programa para demostrar la conversión de tipo explícito

# Inicializando el valor de a

a = 10.6

print("El tipo de 'a' antes de la conversión de tipo es ", type(a))

print(int(a))

print("El tipo de 'a' después de la conversión de tipo es", type(a))

# Inicializando el valor de b

b = 8.3

print("El tipo de 'b' antes de la conversión de tipo es ", type(b))

print(int(b))

print("El tipo de 'b' después de la conversión de tipo es", type(b))

# Inicializando el valor de c

c = 7

print("El tipo de 'c' antes de la conversión de tipo es ", type(c))

print(float(c))

print("El tipo de 'c' después de la conversión de tipo es", type(c))

```

**Salida:**

```bash
El tipo de 'a' antes de la conversión de tipo es  <class 'float'>
10
El tipo de 'a' después de la conversión de tipo es <class 'float'>
El tipo de 'b' antes de la conversión de tipo es  <class 'float'>
8
El tipo de 'b' después de la conversión de tipo es <class 'float'>
El tipo de 'c' antes de la conversión de tipo es  <class 'int'>
7.0
El tipo de 'c' después de la conversión de tipo es <class 'int'>

```

**Explicación:**

Entendamos lo que hemos hecho en este programa.

1. Hemos inicializado los valores de a, b y c.
2. Hemos utilizado int() y float() en este programa para ver cómo se realiza la conversión de tipo explícito.
3. Al ejecutar este programa, podemos verificar cómo cambia el tipo de datos.

Finalmente, echemos un vistazo al último programa de este artículo que cubre posibles tipos de conversiones de tipo explícito.

**Ejemplo:**

```bash
# Programa para demostrar la conversión de tipo explícito

# Inicializando el valor de a

a = 10

print("El tipo de 'a' antes de la conversión de tipo es ", type(a))

print(str(a))

print("El tipo de 'a' después de la conversión de tipo es", type(a))

# Inicializando el valor de b

b = '8'

print("El tipo de

 'b' antes de la conversión de tipo es ", type(b))

print(int(b))

print("El tipo de 'b' después de la conversión de tipo es", type(b))

# Inicializando el valor de c

c = '7.9'

print("El tipo de 'c' antes de la conversión de tipo es ", type(c))

print(float(c))

print("El tipo de 'c' después de la conversión de tipo es", type(c))

```

**Salida:**

```bash
El tipo de 'a' antes de la conversión de tipo es  <class 'int'>
10
El tipo de 'a' después de la conversión de tipo es <class 'int'>
El tipo de 'b' antes de la conversión de tipo es  <class 'str'>
8
El tipo de 'b' después de la conversión de tipo es <class 'str'>
El tipo de 'c' antes de la conversión de tipo es  <class 'str'>
7.9
El tipo de 'c' después de la conversión de tipo es <class 'str'>

```

**Explicación:**

El enfoque es similar al programa anterior y en este programa, hemos incluido conversiones usando int(), str() y float().

## Conclusión

En este tutorial, aprendimos qué es la conversión de tipos en Python, cuáles son sus tipos y cómo se puede realizar en Python.