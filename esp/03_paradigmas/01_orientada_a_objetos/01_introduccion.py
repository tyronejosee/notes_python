"""
Prog. Orientada a Objetos
Este paradigma se basa en la idea de objetos y sus interacciones. 
Python soporta la POO con características como clases, herencia y polimorfismo.
"""

## Ventajas
# - Relación con entidades del mundo real
# - Reutilización de código
# - Abstracción u ocultación de datos

## Desventajas
# - Protección de Datos
# - No apto para todo tipo de problemas
# - Velocidad lenta

## Ejemplo
# Se ha definido la clase Emp aquí
class Emp:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
      
    def informacion(self):
        print("Hola, %s. Tienes %s años." % (self.nombre, self.edad))
  
# Se han creado objetos de la clase Emp aquí        
empleados = [Emp("John", 43),
             Emp("Hilbert", 16),
             Emp("Alice", 30)]
  
# Se utilizan objetos de la clase Emp aquí
for empleado in empleados:
    empleado.informacion()

## Salida
# Hola John. Tienes 43 años
# Hola Hilberto. Tienes 16 años
# Hola, Alicia. Tienes 30 años
