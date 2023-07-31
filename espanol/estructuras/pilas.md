# Pilas (Stack)

Una pila es una estructura de datos lineal que sigue el principio de **Último en Entrar, Primero en Salir (LIFO)**. Esto significa que el último elemento insertado en la pila es el primero en ser removido.

Puedes pensar en la estructura de datos pila como un montón de platos apilados uno encima del otro.

![https://cdn.programiz.com/sites/tutorial2program/files/stack-of-plates_0.png](https://cdn.programiz.com/sites/tutorial2program/files/stack-of-plates_0.png)

**Representación de una pila similar a un montón de platos**

Aquí puedes:

- Colocar un nuevo plato encima.
- Quitar el plato de la parte superior.

Y si deseas el plato que está en la parte inferior, primero debes quitar todos los platos que están encima. Así es exactamente cómo funciona la estructura de datos pila.

# Principio LIFO de la Pila

En términos de programación, poner un elemento en la parte superior de la pila se llama **push** (emplazar), y quitar un elemento se llama **pop** (sacar).

![https://cdn.programiz.com/sites/tutorial2program/files/stack.png](https://cdn.programiz.com/sites/tutorial2program/files/stack.png)

**Operaciones de emplazar (push) y sacar (pop) en la pila**

En la imagen anterior, aunque el elemento **3** fue el último en ser colocado, fue el primero en ser removido. Esto es exactamente cómo funciona el **Principio LIFO (Último en Entrar, Primero en Salir)**.

Podemos implementar una pila en cualquier lenguaje de programación como C, C++, Java, Python o C#, pero la especificación es prácticamente la misma.

# Operaciones Básicas de la Pila

Hay algunas operaciones básicas que nos permiten realizar diferentes acciones en una pila.

- **Empujar (Push)**: Agregar un elemento en la parte superior de la pila.
- **Sacar (Pop)**: Quitar un elemento de la parte superior de la pila.
- **Está Vacía (IsEmpty)**: Comprobar si la pila está vacía.
- **Está Llena (IsFull)**: Comprobar si la pila está llena.
- **Mirar (Peek)**: Obtener el valor del elemento en la parte superior sin quitarlo.

# Funcionamiento de la Estructura de Datos Pila

Las operaciones funcionan de la siguiente manera:

1. Se utiliza un puntero llamado TOP para realizar un seguimiento del elemento en la parte superior de la pila.
    
    TOP
    
2. Al inicializar la pila, establecemos su valor en -1 para poder comprobar si la pila está vacía comparando `TOP == -1`.
3. Al empujar (push) un elemento, aumentamos el valor de TOP y colocamos el nuevo elemento en la posición indicada por TOP.
    
    TOP
    
    TOP
    
4. Al sacar (pop) un elemento, devolvemos el elemento apuntado por TOP y disminuimos su valor.
    
    TOP
    
5. Antes de empujar (push), verificamos si la pila ya está llena.
6. Antes de sacar (pop), verificamos si la pila ya está vacía.

![https://cdn.programiz.com/sites/tutorial2program/files/stack-operations.png](https://cdn.programiz.com/sites/tutorial2program/files/stack-operations.png)

**Funcionamiento de la Estructura de Datos Pila**

# Implementaciones de la Pila en Python

La implementación de pila más común es utilizando arreglos, pero también se puede implementar utilizando listas.

```python
# Implementación de la pila en Python

# Crear una pila
def crear_pila():
    pila = []
    return pila

# Verificar si la pila está vacía
def esta_vacia(pila):
    return len(pila) == 0

# Agregar elementos a la pila
def empujar(pila, elemento):
    pila.append(elemento)
    print("elemento empujado: " + elemento)

# Quitar un elemento de la pila
def sacar(pila):
    if (esta_vacia(pila)):
        return "la pila está vacía"

    return pila.pop()

pila = crear_pila()
empujar(pila, str(1))
empujar(pila, str(2))
empujar(pila, str(3))
empujar(pila, str(4))
print("elemento sacado: " + sacar(pila))
print("pila después de sacar un elemento: " + str(pila))
```

# Complejidad Temporal de la Pila

Para la implementación de la pila basada en un arreglo, las operaciones push y pop toman tiempo constante, es decir, `O(1)`.

# Aplicaciones de la Estructura de Datos Pila

Aunque la pila es una estructura de datos simple de implementar, es muy poderosa. Los usos más comunes de una pila son:

- **Invertir una palabra**: Colocar todas las letras en una pila y sacarlas. Debido al orden LIFO de la pila, se obtendrán las letras en orden inverso.
- **En compiladores**: Los compiladores utilizan la pila para calcular el valor de expresiones como `2 + 4 / 5 * (7 - 9)` mediante la conversión de la expresión a una forma prefija o postfija.
- **En navegadores web**: El botón de retroceso en un navegador web guarda todas las URL que has visitado previamente en una pila. Cada vez que visitas una nueva página, se agrega en la parte superior de la pila. Cuando presionas el botón de retroceso, se elimina la URL actual de la pila y se accede a la URL anterior.
