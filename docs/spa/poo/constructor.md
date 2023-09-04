# Constructor

Un constructor es un tipo especial de método (función) que se utiliza para inicializar los miembros de instancia de la clase.

En C++ o Java, el constructor tiene el mismo nombre que su clase, pero se trata de manera diferente en Python. Se utiliza para crear un objeto.

Los constructores pueden ser de dos tipos:

1. Constructor con parámetros
2. Constructor sin parámetros

La definición del constructor se ejecuta cuando creamos el objeto de esta clase. Los constructores también verifican que haya suficientes recursos para que el objeto realice cualquier tarea de inicio.

## Creando el Constructor

En Python, el método `__init()__` simula el constructor de la clase. Este método se llama cuando se instancia la clase. Acepta la palabra clave **self** como primer argumento, lo que permite acceder a los atributos o métodos de la clase.

Podemos pasar cualquier número de argumentos al momento de crear el objeto de la clase, dependiendo de la definición de `__init()__`. Se utiliza principalmente para inicializar los atributos de la clase. Cada clase debe tener un constructor, incluso si se basa simplemente en el constructor predeterminado.

Considera el siguiente ejemplo para inicializar los atributos de la clase `Empleado`.

**Ejemplo**:

```python
class Empleado:
    def __init__(self, nombre, id):
        self.id = id
        self.nombre = nombre

    def mostrar(self):
        print("ID: %d\\nNombre: %s" % (self.id, self.nombre))

emp1 = Empleado("John", 101)
emp2 = Empleado("David", 102)

# Accediendo al método mostrar() para imprimir la información del empleado 1
emp1.mostrar()

# Accediendo al método mostrar() para imprimir la información del empleado 2
emp2.mostrar()
```

**Salida**:

```bash
ID: 101
Nombre: John
ID: 102
Nombre: David
```

## Contando el Número de Objetos de Una Clase

El constructor se llama automáticamente cuando creamos el objeto de la clase. Considera el siguiente ejemplo.

**Ejemplo**:

```python
class Estudiante:
    contador = 0

    def __init__(self):
        Estudiante.contador = Estudiante.contador + 1


s1 = Estudiante()
s2 = Estudiante()
s3 = Estudiante()

print("El número de estudiantes:", Estudiante.contador)
```

**Salida**:

```bash
El número de estudiantes: 3
```

## Constructor sin Parámetros

El constructor sin parámetros se utiliza cuando no queremos manipular el valor o cuando el constructor tiene solo `self` como argumento. Considera el siguiente ejemplo.

**Ejemplo**:

```python
class Estudiante:
    # Constructor sin parámetros
    def __init__(self):
        print("Este es el constructor sin parámetros")

    def mostrar(self, nombre):
        print("Hola", nombre)


estudiante = Estudiante()
estudiante.mostrar("John")
```

## Constructor con Parámetros

El constructor con parámetros tiene varios parámetros junto con `self`. Considera el siguiente ejemplo.

**Ejemplo**:

```python
class Estudiante:
    # Constructor con parámetros
    def __init__(self, nombre):
        print("Este es el constructor con parámetros")
        self.nombre = nombre

    def mostrar(self):
        print("Hola", self.nombre)


estudiante = Estudiante("John")
estudiante.mostrar()
```

**Salida**:

```bash
Este es el constructor con parámetros
Hola John
```

## Constructor Predeterminado

Cuando no incluimos el constructor en la clase o nos olvidamos de declararlo, entonces se convierte en el constructor predeterminado. No realiza ninguna tarea, pero inicializa los objetos. Considera el siguiente ejemplo.

**Ejemplo**:

```python
class Estudiante:
    num_lista = 101
    nombre = "Joseph"

    def mostrar(self):
        print(self.num_lista, self.nombre)


st = Estudiante()
st.mostrar()
```

**Salida**:

```bash
101 Joseph
```

## Más de Un Constructor en Una Sola Clase

Veamos otro escenario, ¿qué sucede si declaramos dos constructores iguales en la clase?

**Ejemplo**:

```python
class Estudiante:
    def __init__(self):
        print("Primer constructor")

    def __init__(self):
        print("Segundo constructor")


st = Estudiante()
```

**Salida**:

```bash
Segundo constructor
```

En el código anterior, el objeto `st` llama al segundo constructor, aunque ambos tienen la misma configuración. El primer método no es accesible mediante el objeto `st`. Internamente, el objeto de la clase siempre llamará al último constructor si la clase tiene varios constructores.

> **Nota**: La sobrecarga de constructores no está permitida en Python.

## Funciones Integradas de Clase

Las funciones integradas definidas en la clase se describen en la siguiente tabla.

| N. | Función | Descripción |
| --- | --- | --- |
| 1 | getattr(obj, name, default) | Se utiliza para acceder al atributo del objeto. |
| 2 | setattr(obj, name, value) | Se utiliza para asignar un valor específico a un atributo específico de un objeto. |
| 3 | delattr(obj, name) | Se utiliza para eliminar un atributo específico. |
| 4 | hasattr(obj, name) | Devuelve verdadero si el objeto contiene un atributo específico. |

**Ejemplo**:

```python
class Estudiante:
    def __init__(self, nombre, id, edad):
        self.nombre = nombre
        self.id = id
        self.edad = edad


s = Estudiante("John", 101, 22)

# Imprime el atributo nombre del objeto s
print(getattr(s, 'nombre'))

# Cambia el valor del atributo edad a 23
setattr(s, "edad", 23)

# Imprime el valor modificado de edad
print(getattr(s, 'edad'))

# Devuelve verdadero si el estudiante contiene el atributo con nombre id
print(hasattr(s, 'id'))

# Elimina el atributo edad
delattr(s, 'edad')

# Esto generará un error ya que se ha eliminado el atributo edad
print(s.edad)
```

**Salida**:

```bash
John
23
True
AttributeError: 'Estudiante' object has no attribute 'edad'
```

## Atributos de Clase Integrados

Junto con los otros atributos, una clase de Python también contiene algunos atributos de clase integrados que proporcionan información sobre la clase.

Los atributos de clase integrados se muestran en la siguiente tabla.

| N. | Atributo | Descripción |
| --- | --- | --- |
| 1 | __dict__ | Proporciona el diccionario que contiene la información sobre el espacio de nombresde la clase. |
| 2 | __doc__ | Contiene una cadena que tiene la documentación de la clase. |
| 3 | __name__ | Se utiliza para acceder al nombre de la clase. |
| 4 | __module__ | Se utiliza para acceder al módulo en el que se define esta clase. |
| 5 | __bases__ | Contiene una tupla que incluye todas las clases base. |

**Ejemplo**:

```python
class Estudiante:
    def __init__(self, nombre, id, edad):
        self.nombre = nombre
        self.id = id
        self.edad = edad

    def mostrar_detalles(self):
        print("Nombre: %s, ID: %d, Edad: %d" % (self.nombre, self.id, self.edad))


s = Estudiante("John", 101, 22)

print(s.__doc__)
print(s.__dict__)
print(s.__module__)
```

**Salida**:

```bash
None
{'nombre': 'John', 'id': 101, 'edad': 22}
__main__
```
