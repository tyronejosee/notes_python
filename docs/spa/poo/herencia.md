# Herencia

La herencia es un aspecto importante del paradigma orientado a objetos. La herencia proporciona reutilización de código al programa, ya que podemos usar una clase existente para crear una nueva clase en lugar de crearla desde cero.

En la herencia, la clase hija adquiere las propiedades y puede acceder a todos los miembros de datos y funciones definidos en la clase padre. Una clase hija también puede proporcionar su implementación específica para las funciones de la clase padre. En esta sección del tutorial, discutiremos la herencia en detalle.

En Python, una clase derivada puede heredar una clase base simplemente mencionando la base entre paréntesis después del nombre de la clase derivada. Considera la siguiente sintaxis para heredar una clase base en una clase derivada.

![https://static.javatpoint.com/python/images/python-inheritance.png](https://static.javatpoint.com/python/images/python-inheritance.png)

**Sintaxis**:

```python
class clase_derivada(clase_base):
    <bloque_de_código>
```

Una clase puede heredar múltiples clases mencionándolas todas dentro de los paréntesis. Considera la siguiente sintaxis.

**Sintaxis**:

```python
class clase_derivada(clase_base_1, clase_base_2, ..., clase_base_n):
    <bloque_de_código>
```

**Ejemplo:**

```python
class Animal:
    
    def speak(self):
        print("Animal hablando")


# La clase hija Perro hereda la clase base Animal
class Perro(Animal):

    def ladrar(self):
        print("El perro ladra")


d = Perro()
d.ladrar()
d.speak()
```

**Salida**:

```bash
El perro ladra
Animal hablando
```

## Herencia de Múltiples Niveles

La herencia de múltiples niveles es posible en Python al igual que en otros lenguajes orientados a objetos. La herencia de múltiples niveles se logra cuando una clase derivada hereda otra clase derivada. No hay límite en el número de niveles hasta los cuales se puede lograr la herencia de múltiples niveles en Python.

![https://static.javatpoint.com/python/images/python-inheritance2.png](https://static.javatpoint.com/python/images/python-inheritance2.png)

La sintaxis de la herencia de múltiples niveles se muestra a continuación.

**Sintaxis**:

```python
class clase1:
    <bloque_de_código>


class clase2(clase1):
    <bloque_de_código>


class clase3(clase2):
    <bloque_de_código>


.
.
```

**Ejemplo**:

```python
class Animal:

    def speak(self):
        print("Animal hablando")


# La clase hija Perro hereda la clase base Animal
class Perro(Animal):

    def ladrar(self):
        print("El perro ladra")


# La clase hija PerroHijo hereda otra clase hija Perro
class PerroHijo(Perro):

    def comer(self):
        print("Comiendo pan...")


d = PerroHijo()
d.ladrar()
d.speak()
d.comer()
```

**Salida**:

```bash
El perro ladra
Animal hablando
Comiendo pan...
```

## Herencia Múltiple

Python nos proporciona la flexibilidad de heredar múltiples clases base en la clase hija.

![https://static.javatpoint.com/python/images/python-inheritance3.png](https://static.javatpoint.com/python/images/python-inheritance3.png)

La sintaxis para realizar la herencia múltiple se muestra a continuación.

**Sintaxis**:

```python
class Base1:
    <bloque_de_código>


class Base2:
    <bloque_de_código>


.
.
.


class BaseN:
    <bloque_de_código>


class Derivada(Base1, Base2, ..., BaseN):
    <bloque_de_código>
```

**Ejemplo**:

```python
class Calculo1:

    def suma(self, a, b):
        return a + b


class Calculo2:

    def multiplicacion(self, a, b):
        return a * b


class Derivada(Calculo1, Calculo2):

    def dividir(self, a, b):
        return a / b


d = Derivada()
print(d.suma(10, 20))
print(d.multiplicacion(10, 20))
print(d.dividir(10, 20))
```

**Salida**:

```bash
30
200
0.5
```

## El Método issubclass(sub, sup)

El método issubclass(sub, sup) se utiliza para verificar las relaciones entre las clases especificadas. Devuelve verdadero si la primera clase es una subclase de la segunda clase, y falso en caso contrario.

**Ejemplo**:

```python
class Calculo1:

    def suma(self, a, b):
        return a + b


class Calculo2:

    def multiplicacion(self, a, b):
        return a * b


class Derivada(Calculo1, Calculo2):

    def dividir(self, a, b):
        return a / b


d = Derivada()

print(issubclass(Derivada, Calculo2))
print(issubclass(Calculo1, Calculo2))
```

**Salida**:

```bash
True
False
```

## El Método isinstance(obj, clase)

El método isinstance() se utiliza para verificar la relación entre los objetos y las clases. Devuelve verdadero si el primer parámetro, es decir, obj, es una instancia del segundo parámetro, es decir, clase.

Considera el siguiente ejemplo.

**Ejemplo**:

```python
class Calculo1:
    def suma(self, a, b):
        return a + b


class Calculo2:
    def multiplicacion(self, a, b):
        return a * b


class Derivada(Calculo1, Calculo2):
    def dividir(self, a, b):
        return a / b


d = Derivada()

print(isinstance(d, Derivada))
```

**Salida**:

```bash
True
```

## Anulación de métodos

Podemos proporcionar una implementación específica del método de la clase padre en nuestra clase hija. Cuando se define el método de la clase padre en la clase hija con una implementación específica, se llama a este concepto anulación de métodos. Podemos necesitar realizar la anulación de métodos en el escenario en el que se necesita una definición diferente de un método de la clase padre en la clase hija.

**Ejemplo**:

```python
class Animal:
    def speak(self):
        print("Animal hablando")


class Perro(Animal):
    def speak(self):
        print("El perro ladra
```

**Salida**:

```bash
El perro ladra
```

### Ejemplo de la vida real de anulación de métodos

```python
class Banco:

    def obtener_tasa_interes(self):
        return 10


class SBI(Banco):

    def obtener_tasa_interes(self):
        return 7


class ICICI(Banco):

    def obtener_tasa_interes(self):
        return 8


b1 = Banco()
b2 = SBI()
b3 = ICICI()

print("Tasa de interés del banco:", b1.obtener_tasa_interes())
print("Tasa de interés de SBI:", b2.obtener_tasa_interes())
print("Tasa de interés de ICICI:", b3.obtener_tasa_interes())
```

**Salida**:

```bash
Tasa de interés del banco: 10
Tasa de interés de SBI: 7
Tasa de interés de ICICI: 8
```

## Abstracción de Datos

La abstracción es un aspecto importante de la programación orientada a objetos. En Python, también podemos realizar ocultamiento de datos agregando el doble guion bajo (__) como prefijo al atributo que se desea ocultar. Después de esto, el atributo no será visible fuera de la clase a través del objeto.

**Ejemplo**:

```python
class Empleado:
    __count = 0

    def __init__(self):
        Empleado.__count = Empleado.__count + 1

    def mostrar(self):
        print("El número de empleados es", Empleado.__count)


emp = Empleado()
emp2 = Empleado()

try:
    print(emp.__count)
finally:
    emp.mostrar()
```

**Salida**:

```bash
El número de empleados es 2
AttributeError: 'Empleado' object has no attribute '__count'
```
