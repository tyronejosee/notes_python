### Classes ###

class Persona:
    # Definiendo los atributos de mi clase.
    def __init__(self, nombre, apellido, edad, ocupacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ocupacion = ocupacion
    # Definiendo los metodos de mi clase.
    def saludar (self):
        print("Hola mi nombre es ", self.nombre, " y tengo ", self.edad)

# Creando una instancia de mi clase.
PERSONA_UNO = Persona("José", "Reyes", 26, "Backend")

# Llamando a los atributos de mi clase.
print(PERSONA_UNO.edad)
