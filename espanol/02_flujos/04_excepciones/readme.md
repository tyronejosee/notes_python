# Excepciones

El bloque `try` te permite probar un bloque de código en busca de errores.

El bloque `except` te permite manejar el error.

El bloque `else` te permite ejecutar código cuando no hay error.

El bloque `finally` te permite ejecutar código, sin importar el resultado de los bloques try y except.

## Manejo de Excepciones

Cuando ocurre un error, o excepción como lo llamamos, Python normalmente se detendrá y generará un mensaje de error.

Estas excepciones pueden ser manejadas utilizando la declaración `try` .

#### Ejemplo

El bloque `try` generará una excepción porque `x` no está definido.

```python
try:
	print(x)
except:
	print("An exception occurred")
```

Dado que el bloque try genera un error, se ejecutará el bloque except.

Sin el bloque try, el programa se bloqueará y generará un error.

#### Ejemplo

Esta instrucción generará un error, porque `x` no está definido.

```python
print(x)
```

## Muchas Excepciones

Puedes definir tantos bloques de excepción como desees, por ejemplo, si deseas ejecutar un bloque de código especial para un tipo especial de error.

#### Ejemplo

Imprimir un mensaje si el bloque `try` genera un `NameError` y otro mensaje para otros errores.

```python
try:
	print(x)
except NameError:
	print("La variable x no está definida")
except:
	print("Algo más salió mal")
```

## Else

Puedes usar la palabra clave `else` para definir un bloque de código que se ejecutará si no se generaron errores:

#### Ejemplo

En este ejemplo, el bloque `try` no genera ningún error.

```python
try:
	print("Hola")
except:
	print("Algo salió mal")
else:
	print("No ocurrió ningún error")
```

## Finally

El bloque `finally`, si se especifica, se ejecutará sin importar si el bloque try genera un error o no.

#### Ejemplo

```python
try:
	print(x)
except:
	print("Algo salió mal")
finally:
	print("El bloque 'try except' ha finalizado")
```

Esto puede ser útil para cerrar objetos y limpiar recursos.

#### Ejemplo

Intentar abrir y escribir en un archivo que no es escribible.

```python
try:
	f = open("demofile.txt")
	try:
		f.write("Lorum Ipsum")
	except:
		print("Algo salió mal al escribir en el archivo")
	finally:
		f.close()
except:
	print("Algo salió mal al abrir el archivo")

```

El programa puede continuar sin dejar el objeto de archivo abierto.

## Lanzar una Excepción

Como desarrollador de Python, puedes elegir lanzar una excepción si ocurre una condición.

Para lanzar (o levantar) una excepción, utiliza la palabra clave `raise`.

#### Ejemplo

Generar un error y detener el programa si x es menor que 0.

```python
x = -1

if x < 0:
	raise Exception("Lo siento, no se permiten números inferiores a cero")
```

La palabra clave `raise` se utiliza para lanzar una excepción.

Puedes definir qué tipo de error lanzar y el texto que se imprimirá al usuario.

#### Ejemplo

Lanzar un `TypeError` si `x` no es un entero.

```python
x = "hola"

if not type(x) is int:
	raise TypeError("Solo se permiten enteros")
```
