# Tipos de Datos

## Tipos de Datos Incorporados

En programación, el tipo de datos es un concepto importante.

Las variables pueden almacenar datos de diferentes tipos, y diferentes tipos pueden hacer cosas diferentes.

Python tiene los siguientes tipos de datos incorporados por defecto, en estas categorías:

Tipo de texto: `str`
Tipos numéricos: `int`, `float`, `complex`
Tipos de secuencia: `list`, `tuple`, `range`
Tipo de mapeo: `dict`
Tipos de conjunto: `set`, `frozenset`
Tipo booleano: `bool`
Tipos binarios: `bytes`, `bytearray`, `memoryview`
Tipo de nulo: `NoneType`

## Obteniendo el Tipo de Datos

Puedes obtener el tipo de datos de cualquier objeto utilizando la función `type()`:

### Ejemplo:

```python
# Imprime el tipo de datos de la variable x
x = 5
print(type(x))
```

## Estableciendo el Tipo de Datos

En Python, el tipo de datos se establece cuando asignas un valor a una variable:

| Ejemplo | Tipo de Dato |
| --- | --- |
| x = "Hola Mundo” | str |
| x = 20 | int |
| x = 20.5 | float |
| x = 1j | complex |
| x = ["manzana", "plátano", "cereza"] | list |
| x = ("manzana", "plátano", "cereza") | tuple |
| x = range(6) | range |
| x = {"nombre" : "Juan", "edad" : 36} | dict |
| x = {"manzana", "plátano", "cereza"} | set |
| x = frozenset({"manzana", "plátano", "cereza"}) | frozenset |
| x = True | bool |
| x = b"Hello” | bytes |
| x = bytearray(5) | bytearray |
| x = memoryview(bytes(5)) | memoryview |
| x = None | NoneType |

## Estableciendo el Tipo de Datos Específico

| Ejemplo | Tipo de Dato |
| --- | --- |
| x = str("Hola Mundo”) | str |
| x = int(20) | int |
| x = float(20.5) | float |
| x = complex(1j) | complex |
| x = list(("manzana", "plátano", "cereza")) | list |
| x = tuple(("manzana", "plátano", "cereza")) | tuple |
| x = range(6) | range |
| x = dict("nombre" : "Juan", "edad" : 36) | dict |
| x = set(("manzana", "plátano", "cereza")) | set |
| x = frozenset(("manzana", "plátano", "cereza")) | frozenset |
| x = bool(5) | bool |
| x = bytes(5) | bytes |
| x = bytearray(5) | bytearray |
| x = memoryview(bytes(5)) | memoryview |
