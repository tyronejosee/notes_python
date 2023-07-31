# Colas (Queues)

# ¿Qué es una Cola?

Una cola es una estructura de datos lineal que está abierta en ambos extremos y las operaciones se realizan en orden de Primero en Entrar, Primero en Salir (FIFO, por sus siglas en inglés). Definimos una cola como una lista en la que todas las adiciones a la lista se realizan en un extremo, y todas las eliminaciones de la lista se realizan en el otro extremo. El elemento que se coloca primero en la cola es el primero en ser eliminado.

# Principio FIFO de la Cola

- Una cola es como una fila esperando para comprar boletos, donde la primera persona en la fila es la primera en ser atendida (es decir, primero en llegar, primero en ser atendido).
- La posición de la entrada en una cola lista para ser atendida, es decir, la primera entrada que se eliminará de la cola, se llama el **frente** de la cola (a veces también se le llama **cabecera** de la cola). De manera similar, la posición de la última entrada en la cola, es decir, la más recientemente agregada, se llama el **extremo trasero** (o la **cola**) de la cola. Ver la figura a continuación.

![https://media.geeksforgeeks.org/wp-content/uploads/20220805131014/fifo.png](https://media.geeksforgeeks.org/wp-content/uploads/20220805131014/fifo.png)

*Propiedad FIFO de la cola*

# Características de la Cola

- La cola puede manejar múltiples datos.
- Podemos acceder a ambos extremos de la cola.
- Son rápidas y flexibles.

# Representación de la Cola

### 1. Representación de Cola mediante Arrays:

Al igual que las pilas, las colas también pueden representarse en un array: En esta representación, la cola se implementa utilizando el array. Las variables utilizadas en este caso son:

- **Queue:** el nombre del array que almacena los elementos de la cola.
- **Front**: el índice donde se almacena el primer elemento en el array que representa la cola.
- **Rear:** el índice donde se almacena el último elemento en el array que representa la cola.

Representación de la cola mediante arrays:

```python
# Creando una cola vacía

# Una estructura para representar una cola

class Queue:

    # Constructor
    def __init__(self, cap):
        self.cap = cap
        self.front = 0
        self.size = 0
        self.rear = cap - 1
        self.arr = [0] * cap

    # Función para crear una cola de la capacidad dada
    # Inicializa el tamaño de la cola como 0
    def createQueue(self):
        return Queue(self.cap)
```

### 2. Representación de Cola mediante Listas Enlazadas:

Una cola también puede representarse utilizando las siguientes entidades:

- Listas enlazadas,
- Punteros, y
- Estructuras.

Representación de la cola mediante listas enlazadas:

```python
class QNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

# Este código fue contribuido por Tapesh (tapeshdua420)

```

# Tipos de Cola

Existen diferentes tipos de colas:

1. **Cola de Entrada Restringida:** Esta es una cola simple. En este tipo de cola, la entrada solo se puede realizar desde un extremo, pero la eliminación puede realizarse desde cualquiera de los extremos.
2. **Cola de Salida Restringida:** También es una cola simple. En este tipo de cola, la entrada se puede realizar desde ambos extremos, pero la eliminación solo se puede hacer desde un extremo.
3. **[Cola Circular](https://www.geeksforgeeks.org/introduction-and-array-implementation-of-circular-queue/):** Este es un tipo especial de cola donde la última posición está conectada nuevamente con la primera posición. Aquí también, las operaciones se realizan en orden FIFO (Primero en Entrar, Primero en Salir). Para obtener más información, consulta **[este enlace](https://www.geeksforgeeks.org/introduction-and-array-implementation-of-circular-queue/)**.
4. **[Cola de Doble Extremo (Dequeue)](https://www.geeksforgeeks.org/deque-set-1-introduction-applications/):** En una cola de doble extremo, tanto las operaciones de inserción como de eliminación se pueden realizar desde ambos extremos. Para obtener más información, consulta **[este enlace](https://www.geeksforgeeks.org/deque-set-1-introduction-applications/)**.
5. **[Cola de Prioridad](https://www.geeksforgeeks.org/priority-queue-set-1-introduction/):** Una cola de prioridad es una cola especial donde los elementos se acceden en función de la prioridad asignada a cada uno de ellos. Para obtener más información, consulta **[este enlace](https://www.geeksforgeeks.org/priority-queue-set-1-introduction/)**.

Para aprender más sobre los diferentes tipos de colas, lee el artículo sobre "**[Tipos de Colas](https://www.geeksforgeeks.org/different-types-of-queues-and-its-applications/)**".

# Operaciones Básicas de Cola

Algunas de las operaciones básicas de una cola en estructuras de datos son:

1. **Enqueue() –** Agrega (o almacena) un elemento al final de la cola.
2. **Dequeue() –** Elimina elementos de la cola.
3. **Peek() o front()-** Obtiene el elemento de datos disponible en el nodo frontal de la cola sin eliminarlo.
4. **rear() –** Esta operación devuelve el elemento en el extremo trasero de la cola sin eliminarlo.
5. **isFull() –** Valida si la cola está llena.
6. **isNull() –** Verifica si la cola está vacía.

También hay algunas operaciones de soporte (operaciones auxiliares):

### **1. Enqueue():**

La operación Enqueue en una cola **agrega (o almacena) un elemento al final de la cola**.

Los siguientes pasos deben llevarse a cabo para encolar (insertar) datos en una cola:

- **Paso 1:** Verificar si la cola está llena.
- **Paso 2:** Si la cola está llena, mostrar un mensaje de desbordamiento y salir.
- **Paso 3:** Si la cola no está llena, incrementar el puntero trasero para que apunte al siguiente espacio vacío.
- **Paso 4:** Agregar el elemento de datos a la ubicación de la cola donde apunta el puntero trasero.
- **Paso 5:** Retornar éxito.

Representación gráfica de Enqueue:

![https://media.geeksforgeeks.org/wp-content/uploads/20220805122158/fifo1-660x371.png](https://media.geeksforgeeks.org/wp-content/uploads/20220805122158/fifo1-660x371.png)

Implementación de Enqueue:

```python
# Función para agregar un elemento a la cola.
# Cambia el puntero trasero y el tamaño

def EnQueue(self, item):
    if self.isFull():
        print("Cola llena")
        return

    self.rear = (self.rear + 1) % (self.capacity)
    self.Q[self.rear] = item
    self.size = self.size + 1
    print("%s encolado en la cola" % str(item))

# Este código fue contribuido por Susobhan Akhuli

```

### **2. Dequeue():**

Remueve (o accede) el primer elemento de la cola.

Los siguientes pasos se llevan a cabo para realizar la operación Dequeue:

- **Paso 1:** Verificar si la cola está vacía.
- **Paso 2:** Si la cola está vacía, retornar el error de desbordamiento y salir.
- **Paso 3:** Si la cola no está vacía, acceder al dato donde apunta el frente.
- **Paso 4:** Incrementar el puntero frente para que apunte al siguiente elemento de datos disponible.
- **Paso 5:** Retornar éxito.

Operación Dequeue:

```python
# Función para eliminar un elemento de la cola.

# Cambia el puntero frente y el tamaño

def DeQueue(self):

    if self.isEmpty():

        print("La cola está vacía")

        return

    print("%s desencolado de la cola" % str(self.Q[self.front]))

    self.front = (self.front + 1) % (self.capacity)

    self.size = self.size - 1

# Este código fue contribuido por Susobhan Akhuli

```

### **3. front():**

Esta operación devuelve el elemento en el extremo frontal de la cola sin eliminarlo.

```python
# Función para obtener el frente de la cola

def que_front(self):

    if self.isempty():

        return "La cola está vacía"

    return self.Q[self.front]

# Este código fue contribuido por Susobhan Akhuli

```

### 4. rear():

Esta operación devuelve el elemento en el extremo trasero de la cola sin eliminarlo.

```python
def rear(queue):
    if queue.empty():
        print("La cola está vacía.")
        return None

    rear_element = None
    while not queue.empty():
        rear_element = queue.get()

    return rear_element

```

### 5. isEmpty():

Esta operación devuelve un valor booleano que indica si la cola está vacía o no.

```python
# La cola está vacía cuando el tamaño es 0
def isEmpty(self):
    return self.size == 0
# Este código fue contribuido por Susobhan Akhuli

```

### 6. isFull():

Esta operación devuelve un valor booleano que indica si la cola está llena o no.

```python
# La cola está llena cuando el tamaño se vuelve igual a la capacidad
def isFull(self):
    return self.size == self.capacity
# Este código fue contribuido por Susobhan Akhuli

```

# Implementación de la Cola

Una cola se puede implementar utilizando las siguientes estructuras de datos:

- Implementación de la Cola utilizando estructura en C/C++
- **[Implementación de la Cola utilizando Arrays](https://www.geeksforgeeks.org/introduction-and-array-implementation-of-queue/)**
- **[Implementación de la Cola utilizando Listas Enlazadas](https://www.geeksforgeeks.org/queue-linked-list-implementation/)**

**Ejemplo:**

```c
// Programa en Python3 para la implementación de la cola usando arrays

# Clase Queue para representar una cola

class Queue:

    # Función __init__

    def __init__(self, capacity):

        self.front = self.size = 0

        self.rear = capacity - 1

        self.Q = [None]*capacity

        self.capacity = capacity

    # La cola está llena cuando el tamaño se vuelve

    # igual a la capacidad

    def isFull(self):

        return self.size == self.capacity

    # La cola está vacía cuando el tamaño es 0

    def isEmpty(self):

        return self.size == 0

    # Función para agregar un elemento a la cola.

    # Cambia el puntero "rear" y el tamaño

    def EnQueue(self, item):

        if self.isFull():

            print("Llena")

            return

        self.rear = (self.rear + 1) % (self.capacity)

        self.Q[self.rear] = item

        self.size = self.size + 1

        print("%s encolado en la cola" % str(item))

    # Función para eliminar un elemento de la cola.

    # Cambia el puntero "front" y el tamaño

    def DeQueue(self):

        if self.isEmpty():

            print("Vacía")

            return

        print("%s desencolado de la cola" % str(self.Q[self.front]))

        self.front = (self.front + 1) % (self.capacity)

        self.size = self.size - 1

    # Función para obtener el frente de la cola

    def que_front(self):

        if self.isEmpty():

            print("La cola está vacía")

        print("El elemento del frente es", self.Q[self.front])

    # Función para obtener el final de la cola

    def que_rear(self):

        if self.isEmpty():

            print("La cola está vacía")

        print("El elemento del final es", self.Q[self.rear])

# Código del programa principal

if __name__ == '__main__':

    queue = Queue(30)

    queue.EnQueue(10)

    queue.EnQueue(20)

    queue.EnQueue(30)

    queue.EnQueue(40)

    queue.DeQueue()

    queue.que_front()

    queue.que_rear()

# Este código fue contribuido por Susobhan Akhuli

```

**Salida:**

```bash
10 encolado en la cola
20 encolado en la cola
30 encolado en la cola
40 encolado en la cola
10 desencolado de la cola
El elemento del frente es 20
El elemento del final es 40

```

**Complejidad temporal:** Todas las operaciones tienen una complejidad temporal de O(1).

**Espacio auxiliar:** O(N)

# Aplicaciones de la Cola

La aplicación de la cola es común. En un sistema informático, puede haber colas de tareas esperando para ser impresas, para acceder al almacenamiento de disco, o incluso en un sistema de tiempo compartido, para usar la CPU. Dentro de un solo programa, puede haber múltiples solicitudes que se mantienen en una cola, o una tarea puede crear otras tareas que deben realizarse a su vez manteniéndolas en una cola.

- Tiene un único recurso y múltiples consumidores.
- Sincroniza entre dispositivos lentos y rápidos.
- En una red, se utiliza una cola en dispositivos como un enrutador/switch y cola de correo.
- Variaciones: desencolar, cola de prioridad y cola de doble extremo de prioridad.
