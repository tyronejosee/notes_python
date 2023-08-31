# Property

En este tutorial, aprenderemos sobre el decorador property o propiedad en Python. Comencemos con una introducción a los decoradores de propiedad.

## Decorador @property

Lo entenderemos con un ejemplo: Supongamos que tenemos una clase Empleado que tiene tres propiedades: **nombre, apellido** y **nombre_del_departamento**. También tenemos otra función **email()** que genera una dirección de correo electrónico para un empleado utilizando su nombre y **apellido**. Veamos el siguiente código.

**Ejemplo**:

```python
class Estudiante:
    def __init__(self, nombre, apellido, nombre_completo):
        self.nombre = nombre
        self.apellido = apellido
        self.nombre_del_departamento = nombre_completo

    # generar correo electrónico usando el nombre y el apellido
    def email(self):
        return '{}.{}@avenger.com'.format(self.nombre, self.apellido)
```

Ahora creemos un objeto de la clase y llamemos a la función **email()**.

```python
obj = Estudiante('Bruce', 'Banner', 'Bruce Banner')

print("Nombre es:", obj.nombre)
print("Apellido es:", obj.apellido)
print("Nombre del departamento es:", obj.nombre_del_departamento)
print(obj.email())
```

**Salida**:

```bash
Nombre es: Bruce
Apellido es: Banner
Nombre del departamento es: Bruce Banner
Bruce.Banner@avenger.com
```

En el código anterior, hemos definido las tres atributos **nombre, apellido** y **nombre_del_departamento** y **email()** son atributos derivados.

El nombre_completo se declara como una variable y **email()** se declara como una función. Cuando ejecutamos el programa, obtenemos **nombre, apellido** y **nombre_del_departamento**. El **nombre_del_departamento** se deriva del **nombre** y el **apellido**, por lo que también lo hace **email()**. Ahora, hagamos algunos cambios en el programa.

```python
obj.nombre = 'Natasha'

print("Nombre del departamento es:", obj.nombre_del_departamento)
print(obj.email())
```

Cambiando el **nombre** a Natasha e imprimiendo **nombre_del_departamento** y **email** nos dará la siguiente salida.

**Salida**:

```bash
Nombre del departamento es: Bruce Banner
Natasha.Banner@avenger.com
```

Podemos ver que el nombre ha cambiado y el correo electrónico cambia automáticamente. Sin embargo, **nombre_del_departamento** no cambia a pesar de usar el atributo **nombre** porque **email()** es una función llamada cuando queremos que se devuelva el correo electrónico, mientras que **nombre** se establece en el momento de la inicialización del objeto. Podemos resolver este problema creando otra función para **nombre_del_departamento** que creamos para **email()**.

**Ejemplo**:

```python
class Empleado:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_del_departamento(self):
        return self.nombre + ' ' + self.apellido

    # generar correo electrónico usando el nombre y el apellido
    def email(self):
        return '{}.{}@avenger.com'.format(self.nombre, self.apellido)

obj = Empleado('Bruce', 'Banner')

print("Nombre es:", obj.nombre)
print("Apellido es:", obj.apellido)
print(obj.nombre_del_departamento())
print(obj.email())

print('Después de cambiar el nombre:')

obj.nombre = 'Natasha'

print(obj.nombre_del_departamento())
print(obj.email())
```

**Salida**:

```bash
Nombre es: Bruce
Apellido es: Banner
Bruce Banner
Bruce.Banner@avenger.com
Después de cambiar el nombre:
Natasha Banner
Natasha.Banner@avenger.com
```

Obtenemos **nombre_del_departamento** cambiado y el correo electrónico actualizado, pero no es una forma "Pythonic" de resolver este problema. Aquí es donde entra en juego el decorador @property para resolver este problema.

## Uso del Decorador @property

El decorador de propiedad devuelve los atributos de propiedad de una clase a partir del getter y el setter declarados y los elimina como parámetros. Usaremos el decorador @property para resolver este problema. Veamos el ejemplo anterior utilizando el decorador @property.

**Ejemplo**:

```python
class Empleado:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @property
    def nombre_del_departamento(self):
        return self.nombre + ' ' + self.apellido

    # generar correo electrónico usando el nombre y el apellido
    def email(self):
        return '{}.{}@avenger.com'.format(self.nombre, self.apellido)

obj = Empleado('Bruce', 'Banner')

print("Nombre es:", obj.nombre)
print("Apellido es:", obj.apellido)
print("Nombre del departamento es:", obj.nombre_del_departamento)
print("Correo electrónico es:", obj.email())

print('Después de cambiar el nombre:')

obj.nombre = 'Natasha'

print("Nombre del departamento es:", obj.nombre_del_departamento)
print("Correo electrónico es:", obj.email())
```

**Salida**:

```bash
Nombre es: Bruce
Apellido es: Banner
Nombre del departamento es: Bruce Banner
Correo electrónico es: Bruce.Banner@avenger.com
Después de cambiar el nombre:
Nombre del departamento es: Natasha Banner
Correo electrónico es: Natasha.Banner@avenger.com
```

**Explicación**:

En el código anterior, se utiliza el decorador @property en la función **nombre_del_departamento**, y ahora esta función se convierte en un atributo y también puede funcionar como un getter debido al decorador @property.

## Uso de los Métodos Setter y Deleter con el Decorador @property

La función a la que se aplica el decorador @property se conoce como el getter. En el ejemplo anterior, **nombre_del_departamento** actúa como un getter. En esta sección, entenderemos el getter y el setter.

Como su nombre sugiere, el método setter establece el valor de los atributos y el método deleter elimina los atributos de la memoria. Implementemos un método setter y getter para el atributo **nombre_del_departamento**.

**Ejemplo**:

```python
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor <= 0:
            raise ValueError('Por favor, ingrese un número positivo')
        self._edad = valor

    @edad.deleter
    def edad(self):
        self._edad = None
        print("La edad ha sido eliminada")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.strip() == '':
            raise ValueError('Por favor, ingrese una cadena válida')
        self._nombre = valor

    @nombre.deleter
    def nombre(self):
        self._nombre = None
        print("El nombre ha sido eliminado")

s1 = Estudiante('Rishabh Pant', 21)

print(s1.edad)
print(s1.nombre)

s1.nombre = 'KL Rahul'

print(s1.nombre)

s1.nombre = ''

print(s1.nombre)
```

**Salida**:

```bash
21
Rishabh Pant
KL Rahul
Traceback (most recent call last):
  File "d:/Python Project/property.py", line 557, in
    s1.nombre = ''
  File "d:/Python Project/bubble_sort.py", line 544, in nombre
    raise ValueError('Por favor, ingrese una cadena válida')
ValueError: Por favor, ingrese una cadena válida
```

**Explicación**:

En el código anterior, hemos creado la clase **Estudiante** donde hemos pasado **nombre** y **edad** en el constructor. Primero, creamos el método **edad()** que aplica el decorador @property; este obtendrá la edad y la devolverá. Luego creamos el método setter para **edad** donde verificamos si el usuario ingresó un valor negativo y si es así, lanzamos un error. Luego creamos el método deleter para **edad**. Lo mismo hemos hecho con los atributos **nombre**. En el método setter, verificamos si el usuario ingresa el nombre como una cadena vacía, lanzamos un error; de lo contrario, establecemos el nombre dado.

**Ejemplo 2**:

```python
class Empleado:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @property
    def nombre_del_departamento(self):
        return self.nombre + ' ' + self.apellido

    # Setter para nombre_del_departamento
    @nombre_del_departamento.setter
    def nombre_del_departamento(self, nombre_completo):
        # Separar el nombre por espacio
        primer_nombre, apellido = nombre_completo.split(" ")
        self.nombre = primer_nombre
        self.apellido = apellido

    # Deleter para nombre_del_departamento
    @nombre_del_departamento.deleter
    def nombre_del_departamento(self):
        self.nombre = None
        self.apellido = None
        print('Se eliminó nombre_del_departamento')

    # Generar correo electrónico usando el nombre y el apellido
    def email(self):
        return '{}.{}@avenger.com'.format(self.nombre, self.apellido)

obj = Empleado('Steve', 'Rogers')

print('Nombre completo es:', obj.nombre_del_departamento)
print('Correo electrónico es:', obj.email())

# Actualizar el primer nombre del objeto obj
obj.nombre = 'Bruce'

print('Nombre completo de obj es:', obj.nombre_del_departamento)
print('Correo electrónico es:', obj.email())

# Establecer nuevo valor para nombre_del_departamento
obj.nombre_del_departamento = 'Hello World'

print('Nuevo nombre completo de obj es:', obj.nombre_del_departamento)

# Eliminar nombre_del_departamento
del obj.nombre_del_departamento
```

**Salida**:

```bash
Nombre completo es: Steve Rogers
Correo electrónico es: Steve.Rogers@avenger.com
Nombre completo de obj es: Bruce Rogers
Correo electrónico es: Bruce.Rogers@avenger.com
Nuevo nombre completo de obj es: Hello World
Se eliminó nombre_del_departamento
```

En el código anterior, hemos creado el getter, setter y deleter utilizando el decorador @property.

### La función property()

Podemos usar la función **property()** para crear getters, setters y deleters en lugar del decorador @property. La sintaxis es la siguiente:

**Sintaxis**:

```python
property(fget=None, fset=None, fdel=None, doc)
```

**Parámetros**:

- **fget() -** Se usa para obtener el valor del atributo, similar a los getters.
- **fset() -** Se usa para establecer el valor del atributo, similar a los setters.
- **fdel() -** Se usa para eliminar el valor del atributo.
- **doc() -** Representa una cadena que contiene la documentación (docstring) para el atributo.

La función retorna un atributo de propiedad a partir del getter, setter y deleter dados.

Veamos el siguiente ejemplo.

**Ejemplo**:

```python
class Empleado:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.nombre_completo = nombre + ' ' + apellido

    def nombre_completo_getter(self):
        return self.nombre + ' ' + self.apellido

    def nombre_completo_setter(self, nombre_completo):
        primer_nombre, apellido = nombre_completo.split()
        self.nombre = primer_nombre
        self.apellido = apellido

    def nombre_completo_deleter(self):
        self.nombre = None
        self.apellido = None
        print('Se eliminó nombre_completo')

    def email(self):
        return '{}.{}@email.com'.format(self.nombre, self.apellido)

nombre_completo = property()
nombre_completo = nombre_completo.getter(nombre_completo_getter)
nombre_completo = nombre_completo.setter(nombre_completo_setter)
nombre_completo = nombre_completo.deleter(nombre_completo_deleter)

# Esto también se puede hacer en una sola línea
# nombre_completo = property(nombre_completo_getter, nombre_completo_setter, nombre_completo_deleter)

obj = Empleado('Nick', 'Fury')

print('Nombre completo es:', obj.nombre_completo)
print('Correo electrónico es:', obj.email())

# Actualizar el primer nombre del objeto obj
obj.nombre = 'Oddin'

print('Nombre completo de obj es:', obj.nombre_completo)
print('Correo electrónico es:', obj.email())

# Establecer nuevo valor para nombre_completo
obj.nombre_completo = 'Bruce Banner'

print('Nuevo nombre completo de obj es:', obj.nombre_completo)

# Eliminar nombre_completo
del obj.nombre_completo
```

**Salida**:

```bash
Nombre completo es: Nick Fury
Correo electrónico es: Nick.Fury@email.com
Nombre completo de obj es: Oddin Fury
Correo electrónico es: Oddin.Fury@email.com
Nuevo nombre completo de obj es: Bruce Banner
Se eliminó nombre_completo
```

También podemos implementar estos métodos usando una sola línea de código.

`nombre_completo = property(nombre_completo_getter, nombre_completo_setter, nombre_completo_deleter)`

## Consejos Importantes

No necesitamos crear los tres métodos para cada propiedad en el código. Podemos definir propiedades de solo lectura incluyendo solo un método getter. También podemos evitar el método deleter y usar solo los métodos getter y setter. Podemos evitar el método setter si queremos establecer el atributo cuando se crea la instancia o si debe modificarse dentro de la clase.

Los usuarios son libres de elegir cualquier método según su contexto de trabajo.
