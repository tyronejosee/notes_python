# Sentencia break

`break` es una palabra clave en Python que se utiliza para sacar el control del programa fuera del bucle. La sentencia `break` rompe los bucles uno por uno, es decir, en el caso de bucles anidados, rompe primero el bucle interno y luego procede a los bucles externos. En otras palabras, podemos decir que `break` se usa para abortar la ejecución actual del programa y el control pasa a la siguiente línea después del bucle.

`break` se utiliza comúnmente en casos en los que necesitamos interrumpir el bucle para una condición dada. La sintaxis de la sentencia `break` en Python es la siguiente:

**Sintaxis:**

```python
# Declaración del bucle
break
```

## Ejemplo 1: Sentencia break con bucle for

**Ejemplo:**

```python
# Ejemplo de sentencia break

mi_lista = [1, 2, 3, 4]
contador = 1

for item in mi_lista:
    if item == 4:
        print("Elemento encontrado")
        contador += 1
        break

print("Encontrado en la posición", contador)
```

**Salida:**

```bash
Elemento encontrado
Encontrado en la posición 2
```

En el ejemplo anterior, se itera una lista usando un bucle `for`. Cuando se encuentra el elemento con valor 4, se ejecuta la sentencia `break` y el bucle termina. Luego, se imprime el contador al ubicar el elemento.

## Ejemplo 2: Salir del bucle prematuramente

**Ejemplo:**

```python
# Ejemplo de sentencia break

mi_str = "python"

for char in mi_str:
    if char == 'o':
        break

    print(char)
```

**Salida:**

```bash
p
y
t
h
```

Cuando se encuentra el carácter en la lista de caracteres, se ejecuta `break` y la iteración se detiene inmediatamente. Luego se imprime la siguiente línea de la instrucción `print`.

## Ejemplo 3: Sentencia break con bucle while

**Ejemplo:**

```python
# Ejemplo de sentencia break

i = 0

while True:
    print(i, end=" ")
    i = i + 1
    if i == 10:
        break

print("Salimos del bucle while")
```

**Salida:**

```bash
0 1 2 3 4 5 6 7 8 9 Salimos del bucle while
```

Es lo mismo que los programas anteriores. El bucle `while` se inicializa como verdadero, lo que crea un bucle infinito. Cuando el valor es 10 y la condición se vuelve verdadera, se ejecutará la sentencia `break` y saltará a la siguiente instrucción `print`, terminando el bucle `while`.

## Ejemplo 4: Sentencia break con bucles anidados

**Ejemplo:**

```python
# Ejemplo de sentencia break

n = 2

while True:
    i = 1

    while i <= 10:
        print("%d X %d = %d\n" % (n, i, n * i))
        i += 1

    choice = int(input("¿Deseas continuar imprimiendo la tabla? Presiona 0 para no: "))

    if choice == 0:
        print("Saliendo del programa...")
        break

    n += 1

print("Programa finalizado exitosamente.")
```

**Salida:**

```bash
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
2 X 10 = 20
¿Deseas continuar imprimiendo la tabla? Presiona 0 para no: 1
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
3 X 10 = 30
¿Deseas continuar imprimiendo la tabla? Presiona 0 para no: 0
Saliendo del programa...
Programa finalizado exitosamente.
```

En el programa anterior hay dos bucles anidados: el bucle interno y el bucle externo. El bucle interno se encarga de imprimir la tabla de multiplicar, mientras que el bucle externo se encarga de incrementar el valor de `n`. Cuando el bucle interno completa su ejecución, el usuario puede optar por continuar imprimiendo. Cuando se ingresa 0, finalmente se ejecuta la sentencia `break` y se termina el bucle anidado.
