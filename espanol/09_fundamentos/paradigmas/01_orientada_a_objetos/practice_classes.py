
class Persona:
    def __init__(self, nombre, apellido, edad, rango):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.rango = rango
    def saludar (self):
        print("Hola mi nombre es ", self.nombre, self.apellido, " y tengo ", self.edad)

variable_uno = Persona("José", "Reyes", 26, "Backend")


# llamar a la clase en la variable con su metodo.
variable_uno.saludar()