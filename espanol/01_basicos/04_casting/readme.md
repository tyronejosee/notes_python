# Casting

## Especificar Un Tipo de Variable

Puede haber momentos en los que desees especificar un tipo para una variable. Esto se puede hacer mediante la conversión de tipos (casting). Python es un lenguaje orientado a objetos y, como tal, utiliza clases para definir tipos de datos, incluyendo sus tipos primitivos.

La conversión de tipos en Python se realiza utilizando funciones constructoras:

- `int()` - construye un número entero a partir de un literal entero, un literal de punto flotante (eliminando todos los decimales) o un literal de cadena (si la cadena representa un número entero).
- `float()` - construye un número de punto flotante a partir de un literal entero, un literal de punto flotante o un literal de cadena (si la cadena representa un número de punto flotante o entero).
- `str()` - construye una cadena a partir de una amplia variedad de tipos de datos, incluyendo cadenas, literales enteros y literales de punto flotante.

### Ejemplo:

```python
# Enteros
x = int(1) # x será 1
y = int(2.8) # y será 2
z = int("3") # z será 3
```

```python
# Flotantes
x = float(1) # x será 1.0
y = float(2.8) # y será 2.8
z = float("3") # z será 3.0
w = float("4.2") # w será 4.2
```

```python
# Cadenas
x = str("s1") # x será 's1'
y = str(2) # y será '2'
z = str(3.0) # z será '3.0'
```
