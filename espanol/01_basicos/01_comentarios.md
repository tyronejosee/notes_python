# Comentarios

Los comentarios se pueden utilizar para explicar código Python.

Los comentarios se pueden utilizar para que el código sea más legible.

Los comentarios se pueden utilizar para evitar la ejecución al probar código.

## Crear un Comentario

Los comentarios comienzan con un `#`, y Python los ignorará.

#### Ejemplo

```python
# Este es un comentario
print("Hola, Mundo!")
```

Los comentarios se pueden colocar al final de una línea, y Python ignorará el resto de la línea:

#### Ejemplo

```python
print("Hola, Mundo!") # Este es un comentario
```

Un comentario no tiene que ser texto que explique el código, también se puede utilizar para evitar que Python ejecute código.

#### Ejemplo

```python
#print("Hola, Mundo!")
print("¡Salud, compañero!")
```

## Comentarios de Varias Líneas

Python no tiene realmente una sintaxis para comentarios de varias líneas.

Para agregar un comentario de varias líneas, puedes insertar un `#` en cada línea.

#### Ejemplo

```python
# Este es un comentario
# escrito en
# más de una línea
print("Hola, Mundo!")
```

O, no exactamente como se pretendía, puedes usar una cadena de varias líneas.

Dado que Python ignorará las literales de cadena que no están asignadas a una variable, puedes agregar una cadena de varias líneas (comillas triples) en tu código y colocar tu comentario dentro de ella.

#### Ejemplo

```python
"""
Este es un comentario
escrito en
más de una línea
"""
print("Hola, Mundo!")
```

Mientras la cadena no esté asignada a una variable, Python leerá el código pero luego lo ignorará, y habrás creado un comentario de varias líneas.
