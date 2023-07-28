# Programación Orientada a Objetos

## Conceptos

Al igual que otros lenguajes de programación de propósito general, Python también es un lenguaje orientado a objetos desde sus inicios. Nos permite desarrollar aplicaciones utilizando un enfoque orientado a objetos. En Python, podemos crear y utilizar fácilmente clases y objetos.

El paradigma orientado a objetos consiste en diseñar el programa utilizando clases y objetos. El objeto está relacionado con entidades del mundo real, como libros, casas, lápices, etc. El concepto de OOP se centra en escribir código reutilizable. Es una técnica ampliamente utilizada para resolver problemas mediante la creación de objetos.

Los principales principios del sistema de programación orientada a objetos son los siguientes:

- Clase
- Objeto
- Método
- Herencia
- Polimorfismo
- Abstracción de datos
- Encapsulación

## Clase

La clase se puede definir como una colección de objetos. Es una entidad lógica que tiene atributos y métodos específicos. Por ejemplo, si tienes una clase de empleados, debería contener un atributo y un método, como una dirección de correo electrónico, nombre, edad, salario, etc.

**Sintaxis:**

```python
class NombreClase:
    <declaraciones-1>
    .
    .
    <declaraciones-N>
```

## Objeto

El objeto es una entidad que tiene estado y comportamiento. Puede ser cualquier objeto del mundo real, como un ratón, un teclado, una silla, una mesa, un bolígrafo, etc.

Todo en Python es un objeto y casi todo tiene atributos y métodos. Todas las funciones tienen un atributo incorporado llamado `__doc__`, que devuelve el docstring definido en el código fuente de la función.

Cuando definimos una clase, necesitamos crear un objeto para asignarle memoria. Considera el siguiente ejemplo.

**Ejemplo:**

```python
class Coche:
    def __init__(self, modelo, año):
        self.modelo = modelo
        self.año = año

    def mostrar(self):
        print(self.modelo, self.año)

c1 = Coche("Toyota", 2016)
c1.mostrar()
```

**Salida:**

```bash
Toyota 2016
```

En el ejemplo anterior, hemos creado la clase llamada `Coche`, y tiene dos atributos: `modelo` y `año`. Hemos creado un objeto `c1` para acceder al atributo de la clase. El objeto `c1` asignará memoria para estos valores. Aprenderemos más sobre clases y objetos en el próximo tutorial.

## Método

El método es una función asociada a un objeto. En Python, un método no es exclusivo de las instancias de clase. Cualquier tipo de objeto puede tener métodos.

## Herencia

La herencia es el aspecto más importante de la programación orientada a objetos, ya que simula el concepto de herencia del mundo real. Especifica que el objeto hijo adquiere todas las propiedades y comportamientos del objeto padre.

Mediante el uso de la herencia, podemos crear una clase que utilice todas las propiedades y comportamientos de otra clase. La nueva clase se conoce como clase derivada o clase hija, y aquella de la cual se adquieren las propiedades se conoce como clase base o clase padre.

Esto proporciona la reutilización del código.

## Polimorfismo

El polimorfismo consta de dos palabras: "poly" y "morphs". "Poly" significa muchos, y "morph" significa forma. Con el polimorfismo, entendemos que una tarea se puede realizar de diferentes formas. Por ejemplo, tienes una clase "animal" y todos los animales hablan. Pero hablan de manera diferente. Aquí, el comportamiento "hablar" es polimórfico en un sentido y depende del animal. Por lo tanto, el concepto abstracto de "animal" no "habla" realmente, pero animales específicos (como perros y gatos) tienen una implementación concreta de la acción "hablar".

## Encapsulación

La encapsulación también es un aspecto esencial de la programación orientada a objetos. Se utiliza para restringir el acceso a métodos y variables. En la encapsulación, el código y los datos se encapsulan juntos en una sola unidad para evitar modificaciones accidentales.

## Abstracción de Datos

La abstracción de datos y la encapsulación a menudo se utilizan como sinónimos. Ambos son casi sinónimos porque la abstracción de datos se logra mediante la encapsulación.

La abstracción se utiliza para ocultar los detalles internos y mostrar solo las funcionalidades. Abstraer algo significa dar nombres a las cosas para que el nombre capture la esencia de lo que hace una función o un programa completo.

## Lenguajes de Prog. Orientada a Objetos vs. Lenguajes de Prog. Orientada a Procedimientos

A continuación, se muestra la diferencia entre la programación orientada a objetos y la programación orientada a procedimientos:

| Índice | Prog. Orientada a Objetos | Prog. Orientada a Procedimientos |
| --- | --- | --- |
| 1. | La programación orientada a objetos es un enfoque para resolver problemas y se utiliza cuando se realiza la computación utilizando objetos. | La programación orientada a procedimientos utiliza una lista de instrucciones para realizar la computación paso a paso. |
| 2. | Facilita el desarrollo y el mantenimiento. | En la programación orientada a procedimientos, no es fácil mantener los códigos cuando el proyecto se vuelve extenso. |
| 3. | Simula la entidad del mundo real. Por lo tanto, los problemas del mundo real se pueden resolver fácilmente a través de la programación orientada a objetos. | No simula el mundo real. Funciona con instrucciones paso a paso divididas en partes pequeñas llamadas funciones. |
| 4. | Proporciona ocultación de datos. Por lo tanto, es más seguro que los lenguajes procedimentales. No se puede acceder a los datos privados desde cualquier lugar. | Los lenguajes procedimentales no proporcionan una forma adecuada de vinculación de datos, por lo que son menos seguros. |
| 5. | Ejemplos de lenguajes de programación orientados a objetos son C++, Java, .Net, Python, C#, etc. | Ejemplos de lenguajes de programación procedimentales son C, Fortran, Pascal, VB, etc. |
