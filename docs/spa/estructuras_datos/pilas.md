# Pilas (Stacks)

Una **pila** es una estructura de datos lineal que almacena elementos en un orden de **[Último en entrar, primero en salir (LIFO)](https://www.geeksforgeeks.org/lifo-last-in-first-out-approach-in-programming/)** o de primero en entrar, último en salir (FILO). En una pila, un nuevo elemento se agrega en un extremo y solo se elimina un elemento de ese extremo. Las operaciones de inserción y eliminación se llaman comúnmente "push" y "pop", respectivamente.

![https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/stack.png](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/stack.png)

**Las funciones asociadas con una pila son:**

- **empty()** - Devuelve si la pila está vacía - Complejidad temporal: O(1)
- **size()** - Devuelve el tamaño de la pila - Complejidad temporal: O(1)
- **top() / peek()** - Devuelve una referencia al elemento superior de la pila - Complejidad temporal: O(1)
- **push(a)** - Inserta el elemento 'a' en la parte superior de la pila - Complejidad temporal: O(1)
- **pop()** - Elimina el elemento superior de la pila - Complejidad temporal: O(1)

### Implementación:

Existen varias formas en que se puede implementar una pila en Python. Este artículo cubre la implementación de una pila utilizando estructuras de datos y módulos de la biblioteca Python.

Una pila en Python se puede implementar utilizando las siguientes formas:

- Lista (list)
- Collections.deque
- queue.LifoQueue

# Implementación usando lista (list):

En Python, la estructura de datos incorporada "list" se puede utilizar como una pila. En lugar de "push()", se utiliza "append()" para agregar elementos en la parte superior de la pila, mientras que "pop()" elimina el elemento en orden LIFO.

Desafortunadamente, la lista tiene algunas limitaciones. El problema más grande es que puede experimentar problemas de velocidad a medida que crece. Los elementos en la lista se almacenan uno al lado del otro en memoria. Si la pila crece más grande que el bloque de memoria que la contiene actualmente, entonces Python necesita hacer algunas asignaciones de memoria. Esto puede hacer que algunas llamadas de "append()" tomen mucho más tiempo que otras.

**Ejemplo:**

```python
# Programa en Python para
# demostrar la implementación de una pila
# usando "list"

pila = []

# Función "append()" para agregar
# elementos en la pila

pila.append('a')
pila.append('b')
pila.append('c')

print('Pila inicial:')
print(pila)

# Función "pop()" para eliminar
# elementos de la pila en orden LIFO

print('\\nElementos extraídos de la pila:')
print(pila.pop())
print(pila.pop())
print(pila.pop())

print('\\nPila después de eliminar elementos:')
print(pila)

# Descomentar pila.pop()
# causará un IndexError
# ya que la pila está ahora vacía

```

**Salida:**

```python
Pila inicial
['a', 'b', 'c']

Elementos extraídos de la pila:
c
b
a

Pila después de eliminar elementos:
[]

```

# Implementación usando collections.deque:

En Python, una pila se puede implementar utilizando la clase "deque" del módulo "collections". La cola doble ("deque") se prefiere sobre la lista en casos donde necesitamos operaciones de agregar y quitar elementos más rápidas desde ambos extremos del contenedor, ya que "deque" proporciona una complejidad temporal de O(1) para las operaciones de agregar y quitar, en comparación con la lista que proporciona una complejidad temporal de O(n).

Se utilizan las mismas funciones que en la lista, "append()" y "pop()".

- Python3

```python
# Programa en Python para
# demostrar la implementación de una pila
# usando "collections.deque"

from collections import deque

pila = deque()

# Función "append()" para agregar
# elementos en la pila

pila.append('a')
pila.append('b')
pila.append('c')

print('Pila inicial:')
print(pila)

# Función "pop()" para eliminar
# elementos de la pila en orden LIFO

print('\\nElementos extraídos de la pila:')
print(pila.pop())
print(pila.pop())
print(pila.pop())

print('\\nPila después de eliminar elementos:')
print(pila)

# Descomentar pila.pop()
# causará un IndexError
# ya que la pila está ahora vacía

```

**Salida:**

```python
Pila inicial:
deque(['a', 'b', 'c'])

Elementos extraídos de la pila:
c
b
a

Pila después de eliminar elementos:
deque([])

```

### Implementación utilizando el módulo "queue"

El módulo "queue" también tiene una estructura de datos llamada LifoQueue, que es básicamente una pila. Los datos se insertan en la cola utilizando la función "put()" y se extraen utilizando la función "get()".

Hay varias funciones disponibles en este módulo:

- **maxsize**: Número máximo de elementos permitidos en la cola.
- **empty()**: Devuelve True si la cola está vacía, False en caso contrario.
- **full()**: Devuelve True si hay "maxsize" elementos en la cola. Si la cola se inicializó con maxsize=0 (por defecto), full() nunca devuelve True.
- **get()**: Elimina y devuelve un elemento de la cola. Si la cola está vacía, espera hasta que haya un elemento disponible.
- **get_nowait()**: Devuelve un elemento si hay uno disponible de inmediato; de lo contrario, genera una excepción QueueEmpty.
- **put(item)**: Coloca un elemento en la cola. Si la cola está llena, espera hasta que haya un espacio libre antes de agregar el elemento.
- **put_nowait(item)**: Coloca un elemento en la cola sin bloqueo. Si no hay espacio libre de inmediato, genera una excepción QueueFull.
- **qsize()**: Devuelve el número de elementos en la cola.

**Ejemplo:**

```python
# Programa Python para
# demostrar la implementación de una pila
# usando el módulo "queue"

from queue import LifoQueue

# Inicialización de una pila

pila = LifoQueue(maxsize=3)

# qsize() muestra el número de elementos
# en la pila

print(pila.qsize())

# Función "put()" para agregar
# elementos a la pila

pila.put('a')
pila.put('b')
pila.put('c')

print("Llena: ", pila.full())
print("Tamaño: ", pila.qsize())

# Función "get()" para extraer
# el elemento de la pila en orden LIFO

print('\\nElementos extraídos de la pila:')
print(pila.get())
print(pila.get())
print(pila.get())

print("\\nVacia: ", pila.empty())

```

---

**Salida:**

```python
0
Llena:  True
Tamaño:  3

Elementos extraídos de la pila:
c
b
a

Vacia:  True

```

### Implementación usando una lista enlazada simple:

La lista enlazada tiene dos métodos: `addHead(item)` y `removeHead()`, que se ejecutan en tiempo constante. Estos dos métodos son adecuados para implementar una pila.

- **getSize()** - Obtiene el número de elementos en la pila.
- **isEmpty()** - Devuelve True si la pila está vacía, False en caso contrario.
- **peek()** - Devuelve el elemento superior de la pila. Si la pila está vacía, se lanza una excepción.
- **push(value)** - Agrega un valor en la cabeza de la pila.
- **pop()** - Elimina y devuelve un valor de la cabeza de la pila. Si la pila está vacía, se lanza una excepción.

**A continuación se muestra la implementación del enfoque anterior:**

```python
# Programa Python para demostrar
# la implementación de una pila usando una lista enlazada simple.

# Clase nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    # Inicializar una pila.
    # Usar un nodo ficticio, que es
    # más fácil para manejar casos especiales.
    def __init__(self):
        self.cabeza = Nodo("cabeza")
        self.tamaño = 0

    # Representación en cadena de la pila
    def __str__(self):
        actual = self.cabeza.siguiente
        cadena = ""
        while actual:
            cadena += str(actual.valor) + "->"
            actual = actual.siguiente
        return cadena[:-2]

    # Obtener el tamaño actual de la pila
    def getSize(self):
        return self.tamaño

    # Verificar si la pila está vacía
    def isEmpty(self):
        return self.tamaño == 0

    # Obtener el elemento superior de la pila
    def peek(self):
        # Comprobar si estamos mirando una pila vacía.
        if self.isEmpty():
            raise Exception("Mirando desde una pila vacía")
        return self.cabeza.siguiente.valor

    # Agregar un valor a la pila en la cabeza
    def push(self, valor):
        nodo = Nodo(valor)
        nodo.siguiente = self.cabeza.siguiente
        self.cabeza.siguiente = nodo
        self.tamaño += 1

    # Eliminar un valor de la pila y devolverlo.
    def pop(self):
        if self.isEmpty():
            raise Exception("Extrayendo desde una pila vacía")
        remover = self.cabeza.siguiente
        self.cabeza.siguiente = self.cabeza.siguiente.siguiente
        self.tamaño -= 1
        return remover.valor

# Código del controlador
if __name__ == "__main__":
    pila = Pila()
    for i in range(1, 11):
        pila.push(i)
    print(f"Pila: {pila}")
    for _ in range(1, 6):
        remover = pila.pop()
        print(f"Extracción: {remover}")
    print(f"Pila: {pila}")

```

---

**Salida:**

```python
Pila: 10->9->8->7->6->5->4->3->2->1
Extracción: 10
Extracción: 9
Extracción: 8
Extracción: 7
Extracción: 6
Pila: 5->4->3->2->1

```

### **Ventajas de la pila:**

- Las pilas son estructuras de datos simples con un conjunto de operaciones bien definido, lo que las hace fáciles de entender y utilizar.
- Las pilas son eficientes para agregar y eliminar elementos, ya que estas operaciones tienen una complejidad de tiempo de O(1).
- Para revertir el orden de los elementos, utilizamos la estructura de datos de pila.
- Las pilas se pueden utilizar para implementar funciones de deshacer/rehacer en aplicaciones.

### **Desventajas de la pila:**

- La restricción del tamaño en la pila es una desventaja, y si están llenas, no se pueden agregar más elementos a la pila.
- Las pilas no proporcionan un acceso rápido a elementos que no sean el elemento superior.
- Las pilas no admiten una búsqueda eficiente, ya que debes extraer elementos uno por uno hasta que encuentres el elemento que estás buscando.
