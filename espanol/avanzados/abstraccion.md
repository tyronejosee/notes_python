# Abstracción

La abstracción se utiliza para ocultar la funcionalidad interna de una función a los usuarios. Los usuarios solo interactúan con la implementación básica de la función, pero se oculta el funcionamiento interno. El usuario está familiarizado con **"qué hace la función"**, pero no sabe **"cómo lo hace"**.

En pocas palabras, todos usamos teléfonos inteligentes y estamos muy familiarizados con sus funciones como la cámara, el grabador de voz, la marcación de llamadas, etc., pero no sabemos cómo se llevan a cabo estas operaciones en segundo plano. Tomemos otro ejemplo: cuando usamos el control remoto del televisor para aumentar el volumen. No sabemos cómo presionar una tecla aumenta el volumen del televisor. Solo sabemos presionar el botón "+" para aumentar el volumen.

Eso es exactamente la abstracción que funciona en el concepto orientado a objetos.

## ¿Por Qué es Importante la Abstracción?

En Python, la abstracción se utiliza para ocultar los datos/clases irrelevantes con el fin de reducir la complejidad. También mejora la eficiencia de la aplicación. A continuación, aprenderemos cómo podemos lograr la abstracción utilizando el programa de Python.

## Clases de Abstracción

En Python, se puede lograr la abstracción mediante el uso de clases abstractas e interfaces.

Una clase que consta de uno o más métodos abstractos se llama clase abstracta. Los métodos abstractos no contienen su implementación. Una clase abstracta puede ser heredada por la subclase y el método abstracto obtiene su definición en la subclase. Las clases de abstracción están destinadas a ser el diseño de otras clases. Una clase abstracta puede ser útil cuando estamos diseñando funciones grandes. Una clase abstracta también es útil para proporcionar la interfaz estándar para diferentes implementaciones de componentes. Python proporciona el módulo **abc** para usar la abstracción en el programa de Python. Veamos la siguiente sintaxis.

**Sintaxis:**

```python
from abc import ABC
class NombreClase(ABC):
```

Importamos la clase ABC del módulo **abc**.

## Clases Base Abstractas

Una clase base abstracta es la aplicación común de la interfaz para un conjunto de subclases. Puede ser utilizado por terceros, que proporcionará las implementaciones, como con complementos. También es beneficioso cuando trabajamos con una base de código grande y es difícil recordar todas las clases.

## Funcionamiento de las Clases Abstractas

A diferencia de otros lenguajes de alto nivel, Python no proporciona la clase abstracta en sí. Necesitamos importar el módulo **abc**, que proporciona la base para definir clases base abstractas (ABC). La ABC funciona decorando los métodos de la clase base como abstractos. Registra las clases concretas como la implementación de la base abstracta. Usamos el decorador **@abstractmethod** para definir un método abstracto o si no proporcionamos la definición del método, se convierte automáticamente en el método abstracto. Veamos el siguiente ejemplo.

**Ejemplo:**

```python
# Programa de Python que demuestra

# El funcionamiento de la clase base abstracta
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("El rendimiento es de 30 km/h")

class Suzuki(Car):
    def mileage(self):
        print("El rendimiento es de 25 km/h")

class Duster(Car):
    def mileage(self):
        print("El rendimiento es de 24 km/h")

class Renault(Car):
    def mileage(self):
        print("El rendimiento es de 27 km/h")

# Código del controlador
t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()

d = Duster()
d.mileage()
```

**Salida:**

```bash
El rendimiento es de 30 km/h
El rendimiento es de 27 km/h
El rendimiento es de 25 km/h
El rendimiento es de 24 km/h
```

**Explicación:**

En el código anterior, hemos importado el módulo **abc** para crear la clase base abstracta. Creamos la clase Car que hereda de la clase ABC y definimos un método abstracto llamado "mileage" (rendimiento). Luego, heredamos la clase base en tres subclases diferentes e implementamos el método abstracto de manera diferente. Creamos los objetos para llamar al método abstracto.

Veamos otro ejemplo.

**Ejemplo:**

```python
# Programa de Python para definir

# una clase abstracta
from abc import ABC

class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass

class Triangle(Polygon):
    def sides(self):
        print("El triángulo tiene 3 lados")

class Pentagon(Polygon):
    def sides(self):
        print("El pentágono tiene 5 lados")

class Hexagon(Polygon):
    def sides(self):
        print("El hexágono tiene 6 lados")

class Square(Polygon):
    def sides(self):
        print("El cuadrado tiene 4 lados")

# Código del controlador
t = Triangle()
t.sides()

s = Square()
s.sides()

p = Pentagon()
p.sides()

k = Hexagon()
k.sides()
```

**Salida:**

```bash
El triángulo tiene 3 lados
El cuadrado tiene 4 lados
El pentágono tiene 5 lados
El hexágono tiene 6 lados
```

**Explicación:**

En el código anterior, hemos definido la clase base abstracta llamada Polygon y también hemos definido el método abstracto. Esta clase base es heredada por varias subclases. Implementamos el método abstracto en cada subclase. Creamos el objeto de las subclases e invocamos el método **sides()**. Se pone en juego la implementación oculta del método **sides()** dentro de cada subclase. El método abstracto **sides()**, definido en la clase base abstracta, nunca se invoca.

## Puntos Para Recordar

A continuación se presentan los puntos que debemos recordar sobre la clase base abstracta en Python.

- Una clase abstracta puede contener tanto métodos normales como métodos abstractos.
- Una clase abstracta no se puede instanciar; no podemos crear objetos de la clase abstracta.

La abstracción es esencial para ocultar la funcionalidad central a los usuarios. Hemos cubierto todos los conceptos básicos de la abstracción en Python.
