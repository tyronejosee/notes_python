# Entrada

Python permite la entrada del usuario.

Esto significa que podemos solicitar al usuario una entrada.

El método es un poco diferente en Python 3.6 que en Python 2.7.

Python 3.6 utiliza el método `input()`.

Python 2.7 utiliza el método `raw_input()`.

El siguiente ejemplo solicita el nombre de usuario y, cuando ingreses el nombre de usuario, se imprime en la pantalla:

## Python 3.6

```python
username = input("Ingrese el nombre de usuario:")
print("El nombre de usuario es: " + username)

```

## Python 2.7

```python
username = raw_input("Ingrese el nombre de usuario:")
print("El nombre de usuario es: " + username)

```

Python detiene la ejecución cuando se encuentra con la función `input()`, y continúa cuando el usuario ha proporcionado alguna entrada.
