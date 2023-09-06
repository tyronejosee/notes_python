# Paradigmas de Programación

El paradigma también puede denominarse como un método para resolver problemas o realizar tareas. Un paradigma de programación es un enfoque para resolver problemas utilizando algún lenguaje de programación, o también podemos decir que es un método para resolver un problema utilizando herramientas y técnicas disponibles para nosotros siguiendo cierto enfoque. Existen muchos lenguajes de programación conocidos, pero todos ellos necesitan seguir una estrategia cuando se implementan, y esta metodología o estrategia son los paradigmas. Además de las variedades de lenguajes de programación, existen muchos paradigmas para satisfacer cada demanda.

**Python Admite Tres Tipos de Paradigmas de Programación**:

- Paradigma de programación orientada a objetos.
- Paradigma de programación orientada a procedimientos.
- Paradigma de programación funcional.

## Paradigma de Programación Orientada a Objetos

En el paradigma de programación orientada a objetos, los objetos son el elemento clave de los paradigmas. Los objetos pueden definirse simplemente como la instancia de una clase que contiene tanto miembros de datos como funciones de métodos. Además, el estilo orientado a objetos relaciona los miembros de datos y las funciones de métodos que admiten la **encapsulación**, y con la ayuda del concepto de **herencia**, el código puede reutilizarse fácilmente. Sin embargo, la principal desventaja del paradigma de programación orientada a objetos es que si el código no está escrito correctamente, el programa puede volverse complicado.

**Ventajas**:

- Relación con entidades del mundo real.
- Reutilización de código.
- Abstracción u ocultamiento de datos.

**Desventajas**:

- Protección de datos.
- No es adecuado para todos los tipos de problemas.
- Velocidad lenta.

**Ejemplo**:

```python
# Se ha definido la clase Emp aquí

class Emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Hola, %s. Tienes %s años." % (self.name, self.age))

# Se han creado objetos de la clase Emp aquí
Emps = [Emp("Juan", 43),
        Emp("Hilberto", 16),
        Emp("Alicia", 30)]

# Se han utilizado objetos de la clase Emp aquí
for emp in Emps:
    emp.info()
```

**Salida**:

```bash
Hola, Juan. Tienes 43 años.
Hola, Hilberto. Tienes 16 años.
Hola, Alicia. Tienes 30 años.
```

## Paradigma de Programación Orientada a Procedimientos

En el paradigma de programación orientada a procedimientos, una serie de pasos computacionales se dividen en módulos, lo que significa que el código se agrupa en funciones y el código se ejecuta secuencialmente paso a paso. Básicamente, combina el código secuencial para instruir a una computadora con cada paso para realizar una tarea específica. Este paradigma ayuda en la modularidad del código y la modularización generalmente se realiza mediante la implementación funcional. Este paradigma de programación ayuda a organizar fácilmente elementos relacionados sin dificultad, y cada archivo actúa como un contenedor.

**Ventajas**:

- Programación de propósito general.
- Reutilización de código.
- Código fuente portable.

**Desventajas**:

- Protección de datos.
- No es adecuado para objetos del mundo real.
- Más difícil de escribir.

**Ejemplo**:

```python
# Forma procedural de encontrar la suma
# de una lista

mylist = [10, 20, 30, 40]

# Se realiza la modularización mediante un
# enfoque funcional
def sumar_lista(mylist):
    res = 0
    for val in mylist:
        res += val
    return res

print(sumar_lista(mylist))
```

**Salida**:

```bash
100
```

## Paradigma de Programación Funcional

El paradigma de programación funcional es un paradigma en el que todo está vinculado en un estilo de funciones matemáticas puras. Se le conoce como paradigma declarativo porque utiliza declaraciones en lugar de instrucciones. Utiliza la función matemática y trata cada declaración como una expresión funcional, ya que una expresión se ejecuta para producir un valor. Las funciones lambda o la recursión son enfoques básicos utilizados para su implementación. El paradigma se enfoca principalmente en "qué resolver" en lugar de "cómo resolverlo". La capacidad de tratar las funciones como valores y pasarlas como argumentos hace que el código sea más legible y comprensible.

**Ventajas**:

- Fácil de entender.
- Facilita la depuración y prueba del código.
- Mejora la comprensión y legibilidad del código.

**Desventajas**:

- Bajo rendimiento.
- Escribir programas es una tarea desafiante.
- Baja legibilidad del código.

**Ejemplo**:

```python
# Forma funcional de encontrar la suma de una lista

import functools

mylist = [11, 22, 33, 44]

# Enfoque funcional recursivo
def sumar_lista(mylist):
    if len(mylist) == 1:
        return mylist[0]
    else:
        return mylist[0] + sumar_lista(mylist[1:])

# Se utiliza una función lambda
print(functools.reduce(lambda x, y: x + y, mylist))
```

**Salida**:

```bash
110
```
