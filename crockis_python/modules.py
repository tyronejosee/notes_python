from package import funciones

funciones.suma_values(2, 3)

import package.funciones

print(package.funciones.suma_values(2, 6))

from package.funciones import valores

print(valores)

# Importando modulos de python.
from math import pi
print(pi)

# Importando modulos y renombrando rutas.
from math import pi as PI_VALOR
print(PI_VALOR)
