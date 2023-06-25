"""
Variables
Las variables son contenedores para almacenar valores de datos.
"""

## Creación de variables
x = 5
y = "Juan"
print(x) # Imprime 5
print(y) # Imprime John

x = 4 # x es de tipo int
x = "María" # x ahora es de tipo str
print(x) # Imprime María

## Cambiar su tipo
x = str(3) # x será '3'
y = int(3) # y será 3
z = float(3) # z será 3.0

## Obtener el tipo de dato
x = 5
y = "Juan"
print(type(x)) # Imprime <class 'int'>
print(type(y)) # Imprime <class 'str'>

## ¿Comillas simples o dobles?
x = "Juan"
# Es lo mismo que
x = 'Juan'

## Distingue mayúsculas y minúsculas
a = 4
A = "María"
# La variable "A" no sobrescribirá "a"

### ----Nombres de variables-----

## Nombres de variables validos
myvar = "Juan"
my_var = "Juan"
_my_var = "Juan"
myVar = "Juan"
MYVAR = "Juan"
myvar2 = "Juan"

## Nombres de variables no validos
#2myvar = "Juan"
#my-var = "Juan"
#my var = "Juan"
# Descomenta para ver los errores

""" Recuerda que los nombres de las variables distinguen entre mayúsculas y minúsculas """

## Nombrar variables con diferentes estilos
## Camel Case
myVariableName = "Juan"

## Pascal Case
MyVariableName = "Juan"

## Snake Case
my_variable_name = "Juan"

### Asignar múltiples valores

## Asignar múltiples valores a múltiples variables
x, y, z = "Naranja", "Plátano", "Cereza"
print(x) # Imprime Naranja
print(y) # Imprime Plátano
print(z) # Imprime Cereza

""" Asegúrate de que la cantidad de variables coincida con la cantidad de valores, de lo contrario obtendrá un error """

## Un valor para múltiples variables
x = y = z = "Naranja"
print(x) # Imprime Naranja
print(y) # Imprime Naranja
print(z) # Imprime Naranja

## Desempaquetar una colección
frutas = ["Manzana", "Plátano", "Cereza"]
x, y, z = frutas
print(x) # Imprime Manzana
print(y) # Imprime Plátano
print(z) # Imprime Cereza

## Variables de salida
x = "Python es increíble"
print(x) # Imprime Python es increíble

# La función print() imprime todo en una sola línea
x = "Python"
y = "es"
z = "increíble"
print(x, y, z) # Imprime Python es increíble

# También puede usar el operador + para generar múltiples variables
x = "Python "
y = "es " # No olvides el espacio
z = "increíble"
print(x + y + z) # Imprime Python es increíble

# Para números, el carácter + funciona como un operador matemático
x = 5
y = 10
print(x + y) # Imprime 15

# Errores típicos
#x = 5
#y = "John"
#print(x + y) # Imprime TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Descomenta y ejecuta para ver el error

