# Listas Enlazadas (Linked List)

# Conceptos básicos de las Listas Enlazadas

Una Lista Enlazada es una estructura de datos lineal en la cual los elementos no se almacenan en una ubicación contigua, sino que están enlazados mediante punteros. La Lista Enlazada forma una serie de nodos conectados, donde cada nodo almacena los datos y la dirección del siguiente nodo.

![https://media.geeksforgeeks.org/wp-content/uploads/20220712172013/Singlelinkedlist.png](https://media.geeksforgeeks.org/wp-content/uploads/20220712172013/Singlelinkedlist.png)

**Estructura de un Nodo:** Un nodo en una Lista Enlazada generalmente consta de dos componentes:

**Datos:** Contiene el valor real o los datos asociados con el nodo.

**Puntero Siguiente:** Almacena la dirección de memoria (referencia) del siguiente nodo en la secuencia.

**Cabeza y Cola:** Se accede a la Lista Enlazada a través del nodo cabeza, que apunta al primer nodo de la lista. El último nodo de la lista apunta a NULL o nullptr, lo que indica el final de la lista. A este nodo se le conoce como el nodo cola.

# ¿Por qué se necesita la Lista Enlazada?

A continuación se presentan algunas ventajas de una Lista Enlazada que te ayudarán a entender por qué es necesario conocerla:

- **Estructura de Datos Dinámica:** El tamaño de la memoria puede ser asignado o desasignado en tiempo de ejecución según las operaciones de inserción o eliminación.
- **Facilidad de Inserción/Eliminación:** La inserción y eliminación de elementos son más simples que en los arrays, ya que no es necesario desplazar elementos después de la inserción o eliminación, solo se necesita actualizar la dirección.
- **Uso Eficiente de Memoria:** Como la Lista Enlazada es una estructura de datos dinámica, el tamaño aumenta o disminuye según se requiera, lo que evita el desperdicio de memoria.
- **Implementación:** Se pueden implementar diversas estructuras de datos avanzadas utilizando una Lista Enlazada, como una pila, cola, grafo, mapas hash, etc.

**Ejemplo:**

> En un sistema, si mantenemos una lista ordenada de IDs en un array id[] = [1000, 1010, 1050, 2000, 2040]. Si queremos insertar un nuevo ID 1005, entonces para mantener el orden, tenemos que mover todos los elementos después de 1000 (excluyendo 1000). La eliminación también es costosa con los arrays a menos que se utilicen algunas técnicas especiales. Por ejemplo, para eliminar 1010 en id[], todo lo que está después de 1010 tiene que ser movido, lo cual genera mucho trabajo y afecta la eficiencia del código.
> 

# **Tipos de Listas Enlazadas**:

Principalmente existen tres tipos de Listas Enlazadas:

1. Lista Enlazada Simple
2. Lista Enlazada Doble
3. Lista Enlazada Circular

### **1. Lista Enlazada Simple**

En una Lista Enlazada Simple, cada nodo contiene una referencia al siguiente nodo en la secuencia. La recorrida de una Lista Enlazada Simple se realiza en dirección hacia adelante.

![https://media.geeksforgeeks.org/wp-content/uploads/20220712172013/Singlelinkedlist.png](https://media.geeksforgeeks.org/wp-content/uploads/20220712172013/Singlelinkedlist.png)

**Ejemplo:**

```python
class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None
 
class ListaEnlazadaSimple:
  def __init__(self):
    self.cabeza = None
     
  def agregar_nodo(self, dato):
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = self.cabeza
    self.cabeza = nuevo_nodo
```

### **2. Lista Enlazada Doble**

En una Lista Enlazada Doble, cada nodo contiene referencias tanto al siguiente nodo como al nodo anterior. Esto permite la recorrida en ambas direcciones, hacia adelante y hacia atrás, pero requiere memoria adicional para la referencia hacia atrás.

![https://media.geeksforgeeks.org/wp-content/uploads/20220712180755/Doublylinkedlist.png](https://media.geeksforgeeks.org/wp-content/uploads/20220712180755/Doublylinkedlist.png)

**Ejemplo:**

```python
class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None
    self.anterior = None
 
class ListaDoblementeEnlazada:
  def __init__(self):
    self.cabeza = None
     
  def agregar_nodo(self, dato):
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = self.cabeza
    if self.cabeza is not None:
      self.cabeza.anterior = nuevo_nodo
    self.cabeza = nuevo_nodo
```

### 3. **Lista Enlazada Circular**:

En una Lista Enlazada Circular, el último nodo apunta de nuevo al nodo cabeza, creando una estructura circular. Puede ser una Lista Enlazada Simple o Doble.

![https://media.geeksforgeeks.org/wp-content/uploads/20220712181336/Circularlinkedlist.png](https://media.geeksforgeeks.org/wp-content/uploads/20220712181336/Circularlinkedlist.png)

**Ejemplo:**

```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaCircular:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

    def imprimir_lista(self):
        if not self.cabeza:
            print("La lista está vacía.")
            return

        temp = self.cabeza
        while True:
            print(temp.dato, end=" -> ")
            temp = temp.siguiente
            if temp == self.cabeza:
                break
        print()

# Ejemplo de uso
lista = ListaEnlazadaCircular()
lista.agregar_nodo(1)
lista.agregar_nodo(2)
lista.agregar_nodo(3)
lista.imprimir_lista()
```

# Operaciones en las Listas Enlazadas

1. **[Inserción](https://www.geeksforgeeks.org/insertion-in-linked-list/):** Agregar un nuevo nodo a una Lista Enlazada implica ajustar los punteros de los nodos existentes para mantener la secuencia adecuada. La inserción se puede realizar al principio, al final o en cualquier posición dentro de la lista.
2. **[Eliminación](https://www.geeksforgeeks.org/deletion-in-linked-list/):** Eliminar un nodo de una Lista Enlazada requiere ajustar los punteros de los nodos vecinos para cubrir el espacio dejado por el nodo eliminado. La eliminación se puede realizar al principio, al final o en cualquier posición dentro de la lista.
3. **[Búsqueda](https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/):** Buscar un valor específico en una Lista Enlazada implica recorrer la lista desde el nodo cabeza hasta que se encuentre el valor o se alcance el final de la lista.

# Aplicaciones de las Listas Enlazadas

- Las listas enlazadas se utilizan para implementar pilas y colas.
- Se utilizan para diversas representaciones de árboles y grafos.
- Se utilizan en la **[asignación de memoria dinámica](https://www.geeksforgeeks.org/what-is-dynamic-memory-allocation/)** (lista enlazada de bloques libres).
- Se utilizan para representar **[matrices dispersas](https://www.geeksforgeeks.org/sparse-matrix-representation/)**.
- Se utilizan para la manipulación de polinomios.
- También se utilizan para realizar operaciones aritméticas en enteros largos.
- Se utilizan para encontrar rutas en redes.
- En sistemas operativos, se pueden utilizar en la gestión de memoria, la planificación de procesos y el sistema de archivos.
- Las listas enlazadas se pueden utilizar para mejorar el rendimiento de algoritmos que necesitan insertar o eliminar elementos con frecuencia de grandes colecciones de datos.
- Implementación de algoritmos como la caché LRU, que utiliza una lista enlazada para realizar un seguimiento de los elementos más recientemente utilizados en una caché.

# Aplicaciones de las Listas Enlazadas en el mundo real

- La lista de canciones en un reproductor de música está enlazada con las canciones anteriores y siguientes.
- En un navegador web, las URL de las páginas web anteriores y siguientes están vinculadas a través de los botones de retroceso y avance.
- En un visor de imágenes, las imágenes anteriores y siguientes están vinculadas con la ayuda de los botones de retroceso y avance.
- El cambio entre dos aplicaciones se realiza utilizando "alt+tab" en Windows y "cmd+tab" en Mac. Esto requiere la funcionalidad de una lista enlazada circular.
- En los teléfonos móviles, guardamos los contactos de las personas. Los detalles del nuevo contacto se colocarán en la posición alfabética correcta. Esto se puede lograr mediante una lista enlazada para colocar el contacto en la posición alfabética correcta.
- Las modificaciones que realizamos en los documentos se crean en realidad como nodos en una lista enlazada doble. Podemos utilizar simplemente la opción de deshacer presionando Ctrl+Z para modificar el contenido. Esto se hace mediante la funcionalidad de una lista enlazada.

# Ventajas de las Listas Enlazadas

Las listas enlazadas son una estructura de datos popular en ciencias de la computación y tienen varias ventajas sobre otras estructuras de datos, como los arrays. Algunas de las principales ventajas de las listas enlazadas son:

- Tamaño Dinámico: Las listas enlazadas no tienen un tamaño fijo, por lo que puedes agregar o eliminar elementos según sea necesario, sin tener que preocuparte por el tamaño de la lista. Esto hace que las listas enlazadas sean una excelente opción cuando necesitas trabajar con una colección de elementos cuyo tamaño puede cambiar dinámicamente.
- Inserción y Eliminación Eficientes: Insertar o eliminar elementos en una lista enlazada es rápido y eficiente, ya que solo necesitas modificar la referencia al siguiente nodo, lo que es una operación O(1).
- Eficiencia en Memoria: Las listas enlazadas utilizan solo la cantidad de memoria que necesitan, por lo que son más eficientes en cuanto a memoria en comparación con los arrays, que tienen un tamaño fijo y pueden desperdiciar memoria si no se utilizan todos los elementos.
- Fácil de Implementar: Las listas enlazadas son relativamente simples de implementar y entender en comparación con otras estructuras de datos como árboles y grafos.
- Flexibilidad: Las listas enlazadas se pueden utilizar para implementar varios tipos abstractos de datos, como pilas, colas y diccionarios asociativos.
- Fácil de Navegar: Las listas enlazadas se pueden recorrer fácilmente, lo que facilita encontrar elementos específicos o realizar operaciones en la lista.

# Desventajas de las Listas Enlazadas

Las listas enlazadas son una estructura de datos popular en ciencias de la computación, pero al igual que cualquier otra estructura de datos, también tienen ciertas desventajas. Algunas de las principales desventajas de las listas enlazadas son:

- Tiempo de Acceso Lento: Acceder a elementos en una lista enlazada puede ser lento, ya que necesitas recorrer la lista enlazada para encontrar el elemento que estás buscando, lo cual es una operación O(n). Esto hace que las listas enlazadas sean una mala elección para situaciones en las que necesitas acceder a elementos rápidamente.
- Punteros: Las listas enlazadas utilizan punteros para referenciar al siguiente nodo, lo que puede hacerlas más complejas de entender y utilizar en comparación con los arrays. Esta complejidad puede dificultar la depuración y el mantenimiento de las listas enlazadas.
- Mayor Sobrecarga: Las listas enlazadas tienen una mayor sobrecarga en comparación con los arrays, ya que cada nodo en una lista enlazada requiere memoria adicional para almacenar la referencia al siguiente nodo.
- Ineficiencia en la Caché: Las listas enlazadas son ineficientes en caché porque la memoria no es contigua. Esto significa que cuando recorres una lista enlazada, es poco probable que obtengas los datos que necesitas en la caché, lo que provoca pérdidas de caché y un rendimiento lento.
- Memoria Adicional Requerida: Las listas enlazadas requieren un puntero adicional para cada nodo, lo que ocupa memoria adicional. Esto puede ser un problema cuando trabajas con conjuntos de datos grandes, ya que la memoria adicional necesaria para los punteros puede aumentar rápidamente.

# Conclusión

Las Listas Enlazadas son estructuras de datos versátiles que proporcionan asignación de memoria dinámica y operaciones de inserción y eliminación eficientes. Comprender los conceptos básicos de las Listas Enlazadas es esencial para cualquier programador o entusiasta de la informática. Con este conocimiento, puedes implementar Listas Enlazadas para resolver diversos problemas y ampliar tu comprensión de las estructuras de datos y algoritmos.

# Recursos Adicionales
https://www.geeksforgeeks.org/data-structures/linked-list/?ref=lbp
