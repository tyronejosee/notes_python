"""
Variables
"""

### Creación de variables

## Ejemplo: Una variable se crea en el momento en que le asignas un valor por primera vez.
x = 5
y = "Juan"
print(x) # Imprime 5
print(y) # Imprime John

## Ejemplo: Las variables no necesitan ser declaradas con un tipo específico y pueden cambiar de tipo incluso después de haber sido asignadas.
x = 4 # x es de tipo int
x = "María" # x ahora es de tipo str
print(x) # Imprime María

### Casting

## Ejemplo: Si deseas especificar el tipo de datos de una variable, esto se puede hacer mediante el casting.
x = str(3) # x será '3'
y = int(3) # y será 3
z = float(3) # z será 3.0


### Obtener el tipo de dato

## Ejemplo: Puedes obtener el tipo de datos de una variable utilizando la función type().
x = 5
y = "Juan"
print(type(x)) # Imprime <class 'int'>
print(type(y)) # Imprime <class 'str'>

### ¿Comillas simples o dobles?

## Ejemplo: Las variables de tipo cadena se pueden declarar utilizando comillas simples o dobles.
x = "Juan"
# Es lo mismo que
x = 'Juan'

## Ejemplo: Distingue mayúsculas y minúsculas
a = 4
A = "María"
# La variable "A" no sobrescribirá "a"

### Nombrar variables

## Ejemplo: Nombres de variables validos
myvar = "Juan"
my_var = "Juan"
_my_var = "Juan"
myVar = "Juan"
MYVAR = "Juan"
myvar2 = "Juan"

## Ejemplo: Nombres de variables no validos
#2myvar = "Juan"
#my-var = "Juan"
#my var = "Juan"
# Descomenta para ver los errores

### Nombrar variables con diferentes estilos
# Los nombres de variables con más de una palabra pueden ser difíciles de leer.
# Hay varias técnicas que puede utilizar para hacerlos más legibles.

## Camel Case: Cada palabra, excepto la primera, comienza con una letra mayúscula.
myVariableName = "Juan"

## Pascal Case: Cada palabra comienza con una letra mayúscula.
MyVariableName = "Juan"

## Snake Case: Cada palabra está separada por un guion bajo.
my_variable_name = "Juan"

### Asignar múltiples valores a múltiples variables

## Ejemplo: Python te permite asignar valores a múltiples variables en una sola línea.
x, y, z = "Naranja", "Plátano", "Cereza"
print(x) # Imprime Naranja
print(y) # Imprime Plátano
print(z) # Imprime Cereza

### Un valor para múltiples variables

## Ejemplo: Y puede asignar el mismo valor a múltiples variables en una línea.
x = y = z = "Naranja"
print(x) # Imprime Naranja
print(y) # Imprime Naranja
print(z) # Imprime Naranja

### Desempaquetar una colección
# Puedes extraer los valores de una colección, en variables individuales, lo cual se conoce como desempaquetado (unpacking)

## Ejemplo: Desempaquetar una lista.
frutas = ["Manzana", "Plátano", "Cereza"]
x, y, z = frutas
print(x) # Imprime Manzana
print(y) # Imprime Plátano
print(z) # Imprime Cereza

### Variables de salida

## Ejemplo: La función print() de Python se utiliza frecuentemente para mostrar variables.
x = "Python es increíble"
print(x) # Imprime Python es increíble

## Ejemplo: La función print() imprime todo en una sola línea.
x = "Python"
y = "es"
z = "increíble"
print(x, y, z) # Imprime Python es increíble

## Ejemplo: También puede usar el operador + para generar múltiples variables
x = "Python "
y = "es " # No olvides el espacio
z = "increíble"
print(x + y + z) # Imprime Python es increíble

## Ejemplo: Para números, el carácter + funciona como un operador matemático
x = 5
y = 10
print(x + y) # Imprime 15

## Ejemplo: Errores típicos al usar + en tipos de datos diferentes.
#x = 5
#y = "John"
#print(x + y) # Imprime TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Descomenta y ejecuta para ver el error

## Ejemplo: En su lugar usa comas, para evitar estos errores.
x = 5
y = "John"
print(x, y) # Imprime 5 John

### Variables Globales
# Al crear una variable dentro de una función, esta es local y solo se puede utilizar dentro de esa función.
# Para crear una variable global dentro de una función, puedes usar la palabra clave "global".

## Ejemplo: Si utilizas la palabra clave "global", la variable pertenece al ámbito global.
def mifuncion():
  global x
  x = "fantástico"

mifuncion()

print("Python es " + x) # Imprime Python es fantastico

## Ejemplo: Crear una variable dentro de una función con el mismo nombre que la variable global.
#x = "impresionante"

#def mifuncion():
#  x = "fantástico"
#  print("Python es " + x)

#mifuncion() # Imprime Python es fantástico

#print("Python es " + x) # Imprime Python es impresionante
# Descomenta, función ya creada al duplicarla genera errores.

### La palabra clave "global"
# Normalmente, cuando creas una variable dentro de una función, esa variable es local y solo puede ser utilizada dentro de esa función.
# Para crear una variable global dentro de una función, puedes utilizar la palabra clave "global".

## Ejemplo: Si usas la palabra clave "global", la variable pertenece al ámbito global.
#def mi_funcion():
#global x
#x = "fantástico"

#mi_funcion()

#print("Python es " + x) # Imprime Python es fantástico

# Además, utiliza la palabra clave "global" si deseas cambiar una variable global dentro de una función.

## Ejemplo: Para cambiar el valor de una variable global dentro de una función, haz referencia a la variable utilizando la palabra clave "global".
#x = "increíble"

#def mi_funcion():
#global x
#x = "fantástico"

#mi_funcion()

#print("Python es " + x)
