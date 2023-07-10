# Comentarios

Estudiaremos cómo escribir comentarios en nuestro programa en este artículo. También aprenderemos sobre comentarios de una sola línea, comentarios de varias líneas, cadenas de documentación y otros comentarios en Python.

## Introducción a los Comentarios

Es posible que deseemos describir el código que desarrollamos. Tal vez deseemos tomar notas sobre por qué una sección del script funciona, por ejemplo. Utilizamos los comentarios para lograr esto. Las fórmulas, procedimientos y lógica empresarial sofisticada se explican típicamente con comentarios. El intérprete de Python pasa por alto los comentarios e interpreta únicamente el script al ejecutar un programa. Los comentarios de una sola línea, los comentarios de varias líneas y las cadenas de documentación son los 3 tipos de comentarios en Python.

## Ventajas de Usar Comentarios

Nuestro código es más comprensible cuando usamos comentarios en él. Nos ayuda a recordar por qué se crearon secciones específicas de código al hacer el programa más comprensible.

Además de eso, podemos aprovechar los comentarios para pasar por alto cierto código mientras evaluamos otras secciones de código. Esta técnica sencilla evita que algunas líneas se ejecuten o crea un seudocódigo rápido para el programa.

A continuación se presentan algunos de los usos más comunes de los comentarios:

- Legibilidad del código
- Restringir la ejecución de código
- Proporcionar una descripción general del programa o metadatos del proyecto
- Agregar recursos al código

## Tipos de Comentarios

En Python, hay 3 tipos de comentarios. Se describen a continuación:

### Comentarios de Una Sola Línea

Los comentarios de una sola línea en Python han demostrado ser eficaces para proporcionar descripciones rápidas para parámetros, definiciones de funciones y expresiones. Un comentario de una sola línea en Python es aquel que tiene un hashtag (#) al principio y continúa hasta el final de la línea. Si el comentario continúa en la siguiente línea, se agrega un hashtag a la línea siguiente y se reanuda la conversación. Considere el siguiente fragmento de código, que muestra cómo usar un comentario de una sola línea:

**Ejemplo:**

```python
# Este código es para mostrar un ejemplo de un comentario de una sola línea
print('Esta declaración no tiene un hashtag delante')
```

**Salida:**

```bash
Esta declaración no tiene un hashtag delante
```

Lo siguiente es el comentario:

```python
# Este código es para mostrar un ejemplo de un comentario de una sola línea
```

El compilador de Python ignora esta línea.

Todo lo que sigue después del hashtag se omite. Por lo tanto, podemos poner el programa mencionado anteriormente en una sola línea de la siguiente manera:

**Ejemplo:**

```python
print('Esto no es un comentario')  # este código es para mostrar un ejemplo de un comentario de una sola línea
```

**Salida:**

```bash
Esto no es un comentario
```

La salida de este programa será idéntica al ejemplo anterior. La computadora pasa por alto todo el contenido que sigue al hashtag.

### Comentarios de Varias Líneas

Python no proporciona la facilidad de comentarios de varias líneas. Sin embargo, hay varias formas de crear comentarios de varias líneas.

**Con Varios Hashtags (#):**

En Python, podemos usar varios hashtags (#) para construir varias líneas de comentarios. Cada línea con un hashtag (#) antes de ella se considerará un comentario de una sola línea.

**Ejemplo:**

```python
# esto es
# un comentario
# que se extiende a varias líneas
```

En este caso, cada línea se considera un comentario y todas se omiten.

**Usando Literales de Cadena:**

Debido a que Python pasa por alto las expresiones de cadena que no se asignan a una variable, podemos utilizarlas como comentarios.

**Ejemplo:**

```python
'esto es un comentario que se extiende a varias líneas'
```

Podemos observar que al ejecutar este código no habrá ninguna salida; por lo tanto, utilizamos las cadenas dentro de triple comillas (""") como comentarios de varias líneas.

### Docstring

Las cadenas encerradas en triple comillas que vienen inmediatamente después de la función definida se llaman docstring de Python. Está diseñado para vincular la documentación desarrollada para módulos, métodos, clases y funciones de Python. Se coloca justo debajo de la función, módulo o clase para explicar qué hacen. El docstring luego es fácilmente accesible en Python utilizando el atributo **doc**.

**Ejemplo:**

```python
# Código para mostrar cómo usamos docstrings en Python
def add(x, y)
"""Esta función suma los valores de x e y"""
return x + y
# Mostrando el docstring de la función add
print(add.__doc__)
```

**Salida:**

```bash
Esta función suma los valores de x e y
```
