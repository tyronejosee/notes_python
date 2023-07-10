# Entrada

## ¿Qué es la Consola?

En esencia, la consola (también conocida como Shell) es un intérprete de línea de comandos que procesa la entrada del usuario, o un comando a la vez. Si no hay errores, se ejecuta el comando y se produce la salida necesaria; de lo contrario, se muestra un mensaje de error.

Cada vez que seleccionas el comando correspondiente en el menú de Herramientas, la consola se muestra como una ventana de herramientas.

![https://static.javatpoint.com/python/images/taking-input-from-console-in-python.png](https://static.javatpoint.com/python/images/taking-input-from-console-in-python.png)

Simplemente presiona la tecla Enter después de escribir tu comando en este campo para que se ejecute.

Es necesario comprender los fundamentos de la consola de Python para programar en este lenguaje.

Los tres símbolos de mayor que (>>>) sirven como el indicador predeterminado de la consola de Python.

Solo después de ejecutar el primer comando, tenemos la opción de escribir el siguiente comando en la consola. Después del indicador, podemos ingresar comandos en Python en la Consola de Python.

## Aceptando Entrada Desde la Consola

El usuario ha ingresado los valores en la consola, y el programa utiliza esos valores según sea necesario.

Utilizamos una función incorporada llamada input() para obtener la entrada del usuario.

**Ejemplo:**

```python
# Mostrar entrada
entrada_1 = input()

# Mostrar salida
print(entrada_1)
```

Al incluir el método input() dentro de la función print(), también podemos convertir ese valor de entrada en un entero, flotante o cadena.

## Conversión de Tipo de la Entrada a Entero

El siguiente código acepta dos entradas (entero/flotante) desde la consola y las convierte en enteros antes de imprimir la suma. Puede haber situaciones en las que necesites una entrada entera del usuario o de la consola. Hasta donde sabemos, el método input() incorporado de Python siempre produce un objeto de la clase str (cadena). Por lo tanto, para aceptar una entrada entera, debemos convertir esas entradas a enteros utilizando la función int() proporcionada por Python.

La conversión de tipo es una técnica utilizada para cambiar los tipos de datos variables a un tipo de datos específico para que los usuarios puedan realizar una acción. Este artículo examinará varias técnicas de conversión de tipo.

**Ejemplo:**

```python
# Mostrar entrada
n1 = int(input())
n2 = int(input())

# Imprimir la suma como entero
print(n1 + n2)
```

## Conversión de Tipo de la Entrada a Flotante

El siguiente programa funcionará para convertir la entrada a un número de punto flotante.

**Ejemplo:**

```python
# Mostrar entrada
n1 = float(input())
n2 = float(input())

# Imprimir la suma como flotante
print(n1 + n2)
```

## Conversión de Tipo de la Entrada a una Cadena

Ya sea que la entrada sea un número de punto flotante o un entero, se puede convertir a una cadena. Para hacer la conversión, utilizamos la palabra clave str.

**Ejemplo:**

```python
# Mostrar entrada
S1 = str(input())

# Mostrar salida
print(S1)
```
