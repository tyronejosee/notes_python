# Clases y Objetos

Python es un lenguaje de programación orientado a objetos que ofrece clases, las cuales son una herramienta poderosa para escribir código reutilizable. Las clases se utilizan para describir objetos con características y comportamientos compartidos. En este artículo examinaremos los conceptos de clases y objetos en Python.

# Clases

En Python, una clase es un tipo de dato definido por el usuario que contiene tanto los datos en sí como los métodos que se pueden utilizar para manipularlos. En cierto sentido, las clases sirven como plantilla para crear objetos. Proporcionan las características y operaciones que los objetos utilizarán.

Supongamos que una clase es un prototipo de un edificio. Un edificio contiene todos los detalles sobre el piso, las habitaciones, las puertas, las ventanas, etc. Podemos crear tantos edificios como queramos basados en estos detalles. Por lo tanto, el edificio puede verse como una clase, y podemos crear tantos objetos de esta clase como deseemos.

# Creación de Clases

En Python, se puede crear una clase utilizando la palabra clave `class`, seguida del nombre de la clase. La sintaxis para crear una clase es la siguiente.

**Sintaxis:**

```python
class NombreClase:
    # conjunto_de_declaraciones
```

En Python, debemos tener en cuenta que cada clase está asociada a una cadena de documentación a la que se puede acceder utilizando `<nombre-de-clase>.__doc__`. Una clase contiene un conjunto de declaraciones que incluye la definición de campos, constructor, funciones, etc.

**Ejemplo:**

**Código:**

```python
class Persona:

    def __init__(self, nombre, edad):
        # Este es el método constructor que se llama al crear un nuevo objeto Persona
        # Toma dos parámetros, nombre y edad, y los inicializa como atributos del objeto
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        # Este es un método de la clase Persona que imprime un mensaje de saludo
        print("Hola, mi nombre es " + self.nombre)
```

Nombre y edad son las dos propiedades de la clase Persona. Además, tiene una función llamada saludar que imprime un saludo.

# Objetos

Un objeto es una instancia particular de una clase con características y funciones únicas. Después de que se ha establecido una clase, se pueden crear objetos basados en ella. Se puede crear un objeto de una clase en Python utilizando el constructor de la clase. Los atributos del objeto se inicializan en el constructor, que es un procedimiento especial con el nombre `__init__`.

**Sintaxis:**

```python
# Declarar un objeto de una clase
nombre_objeto = Nombre_Clase(argumentos)
```

**Código:**

```python
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es " + self.nombre)

# Crear una nueva instancia de la clase Persona y asignarla a la variable persona1
persona1 = Persona("Ayan", 25)

persona1.saludar()
```

**Salida:**

```bash
"Hola, mi nombre es Ayan"
```

# El Parámetro self

El parámetro self hace referencia a la instancia actual de la clase y accede a las variables de la clase. Podemos usar cualquier nombre en lugar de self, pero debe ser el primer parámetro de cualquier función que pertenezca a la clase.

# Método **init**

Para crear una instancia de una clase en Python, se llama a una función específica llamada `__init__`. Aunque se utiliza para establecer los atributos del objeto, a menudo se le llama constructor.

El argumento self es el único requerido por el método `__init__`. Este argumento hace referencia a la instancia recién creada de la clase. Puedes declarar argumentos adicionales en el método `__init__` para inicializar los valores de cada atributo asociado a los objetos.

# Variables de Clase e Instancia

Todas las instancias de una clase comparten variables de clase. Estas variables funcionan de forma independiente de cualquier método de clase y se pueden acceder utilizando el nombre de la clase. Aquí tienes un ejemplo:

**Código:**

```python
class Persona:

    contador = 0  # Esta es una variable de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre  # Esta es una variable de instancia
        self.edad = edad

        Persona.contador += 1  # Accediendo a la variable de clase utilizando el nombre de la clase

persona1 = Persona("Ayan", 25)
persona2 = Persona("Bobby", 30)

print(Persona.contador)
```

**Salida:**

```bash
2
```

En cambio, las variables de instancia son específicas de cada instancia de una clase. Se especifican utilizando el argumento self en el método `__init__`. Aquí tienes un ejemplo.

**Código:**

```python
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre  # Esta es una variable de instancia
        self.edad = edad

persona1 = Persona("Ayan", 25)
persona2 = Persona("Bobby", 30)

print(persona1.nombre)
print(persona2.edad)
```

**Salida:**

```bash
Ayan
30
```

Las variables de clase se crean por separado de cualquier método de clase y son compartidas por todas las instancias de la clase. Cada instancia de una clase tiene sus propias variables de instancia, que se especifican en el método `__init__` utilizando el argumento self.

# Conclusión

En conclusión, los conceptos de clases y objetos de Python son ideas poderosas que te permiten escribir programas reutilizables. Puedes combinar información y capacidades en una única entidad que se puede utilizar para construir muchos objetos mediante el establecimiento de una clase. Después de crear un objeto, puedes acceder a sus métodos y propiedades utilizando la notación de punto. Al comprender las clases y objetos de Python, puedes desarrollar un código más lógico, eficiente y manejable.
