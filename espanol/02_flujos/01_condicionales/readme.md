# Condicionales

## Condiciones y Declaraciones if en Python

Python admite las condiciones lógicas habituales de las matemáticas:

- Igual: `a == b`
- No igual: `a != b`
- Menor que: `a < b`
- Menor o igual que: `a <= b`
- Mayor que: `a > b`
- Mayor o igual que: `a >= b`

Estas condiciones se pueden utilizar de varias formas, más comúnmente en "declaraciones if" y bucles.

## Declaración if

Una "declaración if" se escribe utilizando la palabra clave `if`.

### Ejemplo

```python
# Declaración if
a = 33
b = 200
if b > a:
	print("b es mayor que a")
```

En este ejemplo, utilizamos dos variables, `a` y `b`, que se utilizan como parte de la declaración if para probar si `b` es mayor que `a`. Dado que `a` es 33 y `b` es 200, sabemos que 200 es mayor que 33, por lo que imprimimos en la pantalla que "b es mayor que a".

## Indentación

Python se basa en la indentación (espacios en blanco al principio de una línea) para definir el alcance en el código. Otros lenguajes de programación a menudo utilizan llaves ({}) para este propósito.

### Ejemplo

```python
# Declaración if (sin indentación: generará un error)
a = 33
b = 200
if b > a:
print("b es mayor que a")  # obtendrás un error
```

## Declaración elif

La palabra clave `elif` es la forma de Python de decir "si las condiciones anteriores no son verdaderas, entonces prueba esta condición".

### Ejemplo

```python
a = 33
b = 33
if b > a:
	print("b es mayor que a")
elif a == b:
	print("a y b son iguales")
```

En este ejemplo, `a` es igual a `b`, por lo que la primera condición no es verdadera, pero la condición `elif` es verdadera, por lo que imprimimos en la pantalla que "a y b son iguales".

## Declaración else

La palabra clave `else` captura cualquier cosa que no sea capturada por las condiciones anteriores.

### Ejemplo

```python
a = 200
b = 33
if b > a:
	print("b es mayor que a")
elif a == b:
	print("a y b son iguales")
else:
	print("a es mayor que b")
```

En este ejemplo, `a` es mayor que `b`, por lo que la primera condición no es verdadera, y la condición `elif` tampoco es verdadera, por lo que pasamos a la condición `else` e imprimimos en la pantalla que "a es mayor que b".

También puedes tener un `else` sin el `elif.`

### Ejemplo

```python
a = 200
b = 33
if b > a:
	print("b es mayor que a")
else:
	print("b no es mayor que a")
```

## **Short Hand** if

Si solo tienes una declaración para ejecutar, puedes ponerla en la misma línea que la declaración if.

### Ejemplo

```python
# Declaración if en una línea
if a > b: print("a es mayor que b")
```

## **Short Hand** if-else

Si solo tienes una declaración para ejecutar, una para el if y otra para el else, puedes ponerlo todo en la misma línea.

### Ejemplo

```python
# Declaración if else en una línea
a = 2
b = 330
print("A") if a > b else print("B")
```

<aside>
💡 Esta técnica se conoce como **Operadores Ternarios** o **Expresiones Condicionales**.

</aside>

También puedes tener múltiples declaraciones else en la misma línea.

### Ejemplo

```python
# Declaración if else en una línea, con 3 condiciones
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```

## Operador and

La palabra clave `and` es un operador lógico y se utiliza para combinar declaraciones condicionales.

### Ejemplo

```python
# Prueba si a es mayor que b y si c es mayor que a
a = 200
b = 33
c = 500
if a > b and c > a:
	print("Ambas condiciones son verdaderas")
```

## Operador or

La palabra clave `or` es un operador lógico y se utiliza para combinar declaraciones condicionales.

### Ejemplo

```python
# Prueba si a es mayor que b o si a es mayor que c
a = 200
b = 33
c = 500
if a > b or a > c:
	print("Al menos una de las condiciones es verdadera")
```

## Operador not

La palabra clave `not` es un operador lógico y se utiliza para invertir el resultado de la declaración condicional.

### Ejemplo

```python
# Prueba si a NO es mayor que b
a = 33
b = 200
if not a > b:
	print("a NO es mayor que b")
```

## Declaración if: anidado

Puedes tener declaraciones `if` dentro de otras declaraciones `if`, esto se llama declaraciones `if` anidadas.

### Ejemplo

```python
x = 41

if x > 10:
	print("Mayor que diez,")
	if x > 20:
		print("¡y también mayor que 20!")
	else:
		print("pero no mayor que 20.")
```

## Declaración pass

Las declaraciones `if` no pueden estar vacías, pero si por alguna razón tienes una declaración `if` sin contenido, utiliza la declaración `pass` para evitar obtener un error.

### Ejemplo

```python
a = 33
b = 200
if b > a:
	pass
```
