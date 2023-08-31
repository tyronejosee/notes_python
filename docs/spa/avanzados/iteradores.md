# Iteradores

Un iterador en Python es un objeto que se utiliza para recorrer objetos iterables como listas, tuplas, diccionarios y conjuntos. El objeto iterador en Python se inicializa utilizando el método `iter()` y se utiliza el método `next()` para la iteración.

1. **iter()**: El método iter() se llama para la inicialización de un iterador. Esto devuelve un objeto iterador.
2. **next()**: El método next devuelve el siguiente valor del objeto iterable. Cuando utilizamos un bucle for para recorrer cualquier objeto iterable, internamente se utiliza el método iter() para obtener un objeto iterador, que luego utiliza el método next() para iterar sobre los elementos. Este método genera una excepción de StopIteration para señalar el final de la iteración.

## Ejemplo de iter()

**Ejemplo**:

```python
cadena = "GFG"

iterador_ch = iter(cadena)

print(next(iterador_ch))
print(next(iterador_ch))
print(next(iterador_ch))
```

**Salida**:

```bash
G
F
G
```

### Creación e iteración sobre un iterador usando iter() y next()

A continuación se muestra un sencillo iterador en Python que crea un tipo de iterador que recorre desde 10 hasta un límite dado. Por ejemplo, si el límite es 15, imprimirá 10 11 12 13 14 15. Y si el límite es 5, no imprimirá nada.

**Ejemplo**:

```python
# Un sencillo programa en Python para demostrar
# el funcionamiento de los iteradores utilizando un tipo de ejemplo
# que itera desde 10 hasta un valor dado

# Un tipo iterable definido por el usuario

class Test:
    # Constructor
    def __init__(self, limite):
        self.limit = limite

    # Crea el objeto iterador
    # Se llama cuando se inicializa la iteración
    def __iter__(self):
        self.x = 10
        return self

    # Para pasar al siguiente elemento. En Python 3,
    # se debe reemplazar next con __next__
    def __next__(self):
        # Almacena el valor actual de x
        x = self.x

        # Detiene la iteración si se alcanza el límite
        if x > self.limit:
            raise StopIteration

        # Incrementa y devuelve el valor anterior
        self.x = x + 1
        return x

# Imprime los números del 10 al 15
for i in Test(15):
    print(i)

# No imprime nada
for i in Test(5):
    print(i)
```

**Salida**:

```bash
10
11
12
13
14
15
```

### Iterando sobre iterables incorporados utilizando el método iter()

En las siguientes iteraciones, el estado de la iteración y la variable del iterador se gestionan internamente (no podemos verlo) utilizando un objeto iterador para recorrer los iterables incorporados como list, tuple, dict, etc.

**Ejemplo**:

```python
# Ejemplos de iteradores incorporados

# Iterando sobre una lista
print("Iteración de lista")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Iterando sobre una tupla (inmutable)
print("\\nIteración de tupla")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# Iterando sobre una cadena
print("\\nIteración de cadena")
s = "Geeks"
for i in s:
    print(i)

# Iterando sobre un diccionario
print("\\nIteración de diccionario")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" % (i, d[i]))
```

**Salida**:

```bash
Iteración de lista
geeks
for
geeks

Iteración de tupla
geeks
for
geeks

Iteración de cadena
G
e
e
k
s

Iteración de diccionario
xyz 123
abc 345
```

## Iterable vs. Iterador

Los objetos iterables y los objetos iteradores en Python son diferentes. La principal diferencia entre ellos es que un objeto iterable en Python no puede guardar el estado de la iteración, mientras que los iteradores sí pueden guardar el estado de la iteración actual.

**Nota**: Cada iterador también es un objeto iterable, pero no todo objeto iterable es un iterador en Python.

### Iterando sobre un Objeto Iterable

Iterando sobre cada elemento del objeto iterable.

**Ejemplo**:

```python
tupla = ('a', 'b', 'c', 'd', 'e')

for elemento in tupla:
    print(elemento)
```

**Salida**:

```bash
a
b
c
d
e
```

### Iterando sobre un Iterador

**Ejemplo**:

```python
tupla = ('a', 'b', 'c', 'd', 'e')

# creando un iterador a partir de la tupla
tup_iter = iter(tupla)

print("Dentro del bucle:")

# iterando sobre cada elemento del objeto iterador
for indice, item in enumerate(tup_iter):
    print(item)

    # salir del bucle después de iterar en 3 elementos
    if indice == 2:
        break

# podemos imprimir los elementos restantes que se deben iterar usando next()
# así que el estado fue guardado

print("Fuera del bucle:")
print(next(tup_iter))
print(next(tup_iter))
```

**Salida**:

```bash
Dentro del bucle:
a
b
c
Fuera del bucle:
d
e
```

### Obteniendo un Error de StopIteration al Utilizar un Iterador

En Python, los objetos iterables se pueden iterar varias veces, pero los iteradores generan un error de StopIteration cuando ya se han iterado todos los elementos.

En este ejemplo, estamos intentando obtener el siguiente elemento del iterador después de completar el bucle for. Dado que el iterador ya está agotado, se genera una excepción StopIteration. En cambio, utilizando un objeto iterable, podemos iterar varias veces utilizando un bucle for o podemos obtener elementos utilizando la indexación.

**Ejemplo**:

```python
iterable = (1, 2, 3, 4)
iterator_obj = iter(iterable)

print("Bucle iterable 1:")

# iterando sobre el objeto iterable
for item in iterable:
    print(item, end=",")

print("\\nBucle iterable 2:")

# iterando sobre el objeto iterable nuevamente
for item in iterable:
    print(item, end=",")

print("\\nIterando sobre un iterador:")

# iterando sobre el objeto iterador varias veces
for item in iterator_obj:
    print(item, end=",")

print("\\nIterador: Fuera del bucle")

# esta línea generará una excepción StopIteration
# ya que todos los elementos se han iterado en el bucle for anterior
print(next(iterator_obj))
```

**Salida**:

```bash
Bucle iterable 1:
1,2,3,4,
Bucle iterable 2:
1,2,3,4,
Iterando sobre un iterador:
1,2,3,4,
Iterador: Fuera del bucle

Traceback (most recent call last):
  File "scratch_1.py", line 21, in <module>
    print(next(iterator_obj))
StopIteration
```
