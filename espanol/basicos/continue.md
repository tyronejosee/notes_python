# Sentencia continue

En este tutorial, veremos cómo usar la palabra clave `continue` de Python para saltar las declaraciones restantes del bucle actual y pasar a la siguiente iteración. También veremos la diferencia entre las palabras clave `continue` y `pass`.

## Aplicación de la sentencia continue

En Python, los bucles repiten procesos de manera eficiente. Sin embargo, puede haber ocasiones en las que deseemos salir completamente del bucle actual, omitir una iteración o ignorar la condición que controla el bucle. Para esos casos, utilizamos las sentencias de control de bucle. La palabra clave `continue` es una sentencia de control de bucle que nos permite cambiar el control del bucle.

## La palabra clave continue

En Python, la palabra clave `continue` devuelve el control de la iteración al comienzo del bucle `for` o `while` de Python. Todas las líneas restantes en la iteración actual del bucle se omiten mediante la palabra clave `continue`, y la ejecución vuelve al inicio de la siguiente iteración del bucle.

Tanto los bucles `while` como los bucles `for` de Python pueden utilizar la sentencia `continue`.

### Ejemplo de sentencias continue de Python en un bucle For

Supongamos el siguiente escenario: queremos desarrollar un programa que devuelva números del 10 al 20, pero sin incluir el 15. Se menciona que debemos hacer esto con un bucle `for`. Aquí es donde entra en juego la palabra clave `continue`. Ejecutaremos un bucle desde 10 hasta 20 y probaremos la condición de que el iterador sea igual a 15. Si es igual a 15, utilizaremos la sentencia `continue` para saltar a la siguiente iteración sin mostrar ningún resultado; de lo contrario, el bucle imprimirá el resultado.

El siguiente código es un ejemplo del escenario descrito:

**Ejemplo:**

```python
# Código Python para mostrar un ejemplo de la sentencia continue

# Recorriendo desde 10 hasta 20

for iterator in range(10, 21):

    # Si el iterador es igual a 15, el bucle continuará con la siguiente iteración

    if iterator == 15:
        continue

    # de lo contrario, imprimirá el valor del iterador

    print(iterator)
```

**Salida:**

```bash
10
11
12
13
14
16
17
18
19
20
```

Ahora repetiremos el código anterior, pero esta vez con una cadena de texto. Tomaremos la cadena "Javatpoint" e imprimiremos cada letra de la cadena excepto "a". Esta vez utilizaremos un bucle `while` de Python para hacerlo. El bucle `while` continuará ejecutándose siempre que el valor del iterador sea menor que la longitud de la cadena.

**Ejemplo:**

```python
# Creando una cadena de texto

string = "JavaTpoint"

# Inicializando un iterador

iterator = 0

# Iniciando un bucle while

while iterator < len(string):

    # Si el bucle se encuentra con la letra 'a', omitirá el código restante y pasará a la siguiente iteración

    if string[iterator] == 'a':
        continue

    # de lo contrario, imprimirá la letra

    print(string[iterator])

    iterator += 1
```

**Salida:**

```bash
J
v
T
p
o
i
n
t
```

## Python continue vs. pass

Suele haber cierta confusión entre las palabras clave `continue` y `pass`. Así que aquí están las diferencias entre ambas.

| Encabezados | continue | pass |
| --- | --- | --- |
| Definición | La sentencia continue se utiliza para saltar las declaraciones restantes del bucle actual, pasar a la siguiente iteración y volver al principio. | La palabra clave pass se usa cuando es necesario colocar una frase sintácticamente, pero no se desea que se ejecute nada. |
| Acción | Devuelve el control al inicio del bucle. | No sucede nada si el intérprete de Python encuentra la sentencia pass. |
| Aplicación | Funciona tanto con los bucles while como con los bucles for de Python. | No realiza ninguna acción; por lo tanto, es una operación nula. |
| Sintaxis | Tiene la siguiente sintaxis: continue | Su sintaxis es la siguiente: pass |
| Interpretación | Se utiliza principalmente dentro de la condición de un bucle. | Durante la etapa de compilación de bytes, la palabra clave pass se elimina. |
