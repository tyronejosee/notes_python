# Sentencia Pass

En este tutorial, aprenderemos más sobre la sentencia `pass` (pase). Esta se interpreta como un marcador de posición para futuras funciones, clases, bucles y otras operaciones.

## ¿Qué es la Sentencia Pass?

La sentencia `pass` también se conoce como la sentencia nula. El intérprete de Python no ignora una declaración, aunque una sentencia `pass` no sea una instrucción real. Por lo tanto, estas dos palabras clave de Python son distintas.

Podemos usar la sentencia `pass` como un marcador de posición cuando no estamos seguros del código que se proporcionará en el futuro. Por lo tanto, solo se necesita colocar `pass` en esa línea. La sentencia `pass` se puede utilizar cuando no queremos que se ejecute ningún código. Simplemente podemos insertar `pass` en casos donde el código vacío no está permitido, como en bucles, funciones, definiciones de clases y declaraciones if-else.

**Sintaxis**:

```python
Palabra clave:
    pass
```

Normalmente, lo utilizamos como una perspectiva para el futuro.

Supongamos que tenemos una declaración if-else o un bucle que queremos completar en el futuro pero no podemos hacerlo en el momento. Un cuerpo vacío para la palabra clave `pass` sería gramaticalmente incorrecto. El intérprete de Python mostraría un error sugiriendo llenar el espacio. Por lo tanto, utilizamos la sentencia `pass` para crear un bloque de código que no hace nada.

### Una Ilustración de la Sentencia Pass

**Ejemplo**:

```python
# Programa de Python para mostrar cómo usar la sentencia pass en un bucle for

'''''pass actúa como un marcador de posición. Podemos completar este espacio más adelante'''

sequence = {"Python", "Pass", "Statement", "Placeholder"}

for value in sequence:
    if value == "Pass":
        pass  # dejando un bloque if vacío usando la sentencia pass
    else:
        print("No se alcanzó la palabra clave pass:", value)
```

**Salida**:

```bash
No se alcanzó la palabra clave pass: Python
No se alcanzó la palabra clave pass: Placeholder
No se alcanzó la palabra clave pass: Statement
```

Lo mismo también es posible para crear una función o una clase vacía.

**Ejemplo**:

```python
# Programa de Python para mostrar cómo crear una función y una clase vacías

# Función vacía:
def empty()
    pass

# Clase vacía
class Empty:
    pass
```
