# Montículos (Heap)

# ¿Qué es la Estructura de Datos Montículo?

Un montículo (heap) es una estructura especial de datos basada en árboles en la que el árbol es un árbol binario completo.

# Tipos de montículos

Generalmente, los montículos son de dos tipos.

### **Montículo Máximo (Max-Heap):**

En este montículo, el valor del nodo raíz debe ser el mayor entre todos sus nodos hijos, y lo mismo debe ocurrir para sus subárboles izquierdo y derecho también.

> El número total de comparaciones requeridas en el montículo máximo depende de la altura del árbol. La altura del árbol binario completo es siempre logn; por lo tanto, la complejidad temporal también sería O(logn).
> 

### **Montículo Mínimo (Min-Heap):**

En este montículo, el valor del nodo raíz debe ser el más pequeño entre todos sus nodos hijos, y lo mismo debe ocurrir para sus subárboles izquierdo y derecho también.

> El número total de comparaciones requeridas en el montículo mínimo depende de la altura del árbol. La altura del árbol binario completo es siempre logn; por lo tanto, la complejidad temporal también sería O(logn).
> 

![https://media.geeksforgeeks.org/wp-content/uploads/20230315185259/heap.png](https://media.geeksforgeeks.org/wp-content/uploads/20230315185259/heap.png)

# Propiedades del Montículo (Heap):

El montículo (heap) tiene las siguientes propiedades:

- **Árbol Binario Completo:** Un árbol de montículo es un árbol binario completo, lo que significa que todos los niveles del árbol están completamente llenos, excepto posiblemente el último nivel, que se llena de izquierda a derecha. Esta propiedad garantiza que el árbol se representa eficientemente utilizando un arreglo.
- **Propiedad del Montículo:** Esta propiedad garantiza que el elemento mínimo (o máximo) siempre está en la raíz del árbol según el tipo de montículo.
- **Relación Padre-Hijo:** La relación entre un nodo padre en el índice **'i'** y sus hijos se da mediante las fórmulas: hijo izquierdo en el índice **2i+1** e hijo derecho en el índice **2i+2** para una indexación de nodos basada en 0.
- **Inserción y Eliminación Eficientes:** Las operaciones de inserción y eliminación en los árboles de montículo son eficientes. Los nuevos elementos se insertan en la siguiente posición disponible en el nivel más inferior y a la derecha, y se restaura la propiedad del montículo comparando el elemento con su padre e intercambiando si es necesario. La eliminación del elemento raíz implica reemplazarlo con el último elemento y realizar el equilibrado hacia abajo.
- **Acceso Eficiente a los Elementos Extremos:** El elemento mínimo o máximo siempre está en la raíz del montículo, lo que permite un acceso en tiempo constante.

# Operaciones Soportadas por el Montículo (Heap):

> Las operaciones soportadas por el montículo mínimo y el montículo máximo son las mismas. La diferencia es simplemente que el montículo mínimo contiene el elemento mínimo en la raíz del árbol y el montículo máximo contiene el elemento máximo en la raíz del árbol.
> 

### **Heapify (equilibrar):**

Es el proceso de reorganizar los elementos para mantener la propiedad de la estructura de datos montículo. Se realiza cuando un cierto nodo crea un desequilibrio en el montículo debido a algunas operaciones en ese nodo. Toma tiempo **O(log N)** para equilibrar el árbol.

- Para el **montículo máximo,** se equilibra de tal manera que el elemento máximo es la raíz de ese árbol binario.
- Para el **montículo mínimo,** se equilibra de tal manera que el elemento mínimo es la raíz de ese árbol binario.

### Inserción:

- Si insertamos un nuevo elemento en el montículo, dado que estamos agregando un nuevo elemento, esto distorsionará las propiedades del montículo, por lo que necesitamos realizar la operación de **heapify** para que mantenga la propiedad del montículo.

Esta operación también toma tiempo **O(logN)**.

**Ejemplos:**

```bash
Supongamos que inicialmente el montículo (tomando un montículo máximo) es el siguiente:

           8
        /   \\
     4     5
   / \\
1   2

Ahora, si insertamos 10 en el montículo:
             8
        /      \\
      4       5
   /  \\      /
1    2  10

Después de la operación de heapify, el montículo final se verá así:
           10
         /    \\
      4      8
   /  \\     /
1    2  5
```

### Eliminación:

- Si eliminamos un elemento del montículo, siempre eliminamos el elemento raíz del árbol y lo reemplazamos con el último elemento del árbol.
- Dado que eliminamos el elemento raíz del montículo, se distorsionarán las propiedades del montículo, por lo que necesitamos realizar operaciones de heapify para que mantenga la propiedad del montículo.

Esto toma tiempo **O(logN)**.

**Ejemplo:**

```bash
Supongamos que inicialmente el montículo (tomando un montículo máximo) es el siguiente:
           15
         /   \\
      5     7
   /  \\
2     3

Ahora, si eliminamos el 15 del montículo, será reemplazado por el nodo hoja del árbol temporalmente.
           3
        /   \\
     5     7
   /
2

Después de la operación de heapify, el montículo final se verá así:
           7
        /   \\
     5     3
   /
2
```

### getMax (Para montículo máximo) o getMin (Para montículo mínimo):

Encuentra el elemento máximo o el elemento mínimo para el **montículo máximo** o **montículo mínimo**, respectivamente, y como sabemos que los elementos mínimo y máximo siempre serán el nodo raíz mismo para el montículo mínimo y el montículo máximo, respectivamente. Esto toma tiempo **O(1)**.

### removeMin o removeMax:

Esta operación devuelve y elimina el elemento máximo y el elemento mínimo del montículo máximo y el montículo mínimo, respectivamente. En resumen, elimina el elemento raíz del árbol binario del montículo.

# Implementación de la Estructura de Datos Montículo (Heap):

El siguiente código muestra la implementación de un **montículo máximo**.

Entendamos en detalle la función **maxHeapify**:

**maxHeapify** es la función responsable de restaurar la propiedad del Montículo máximo. Organiza el nodo **i** y sus subárboles de manera que se mantenga la propiedad del montículo.

1. Supongamos que tenemos un arreglo, **arr[]**, que representa el árbol binario completo. Los hijos izquierdo y derecho del nodo **i** se encuentran en los índices **2*i+1** y **2*i+2**, respectivamente.
2. Establecemos el índice del elemento actual, **i**, como el 'MÁXIMO'.
3. Si **arr[2 * i + 1] > arr[i]**, es decir, si el hijo izquierdo es mayor que el valor actual, se establece como el 'MÁXIMO'.
4. De manera similar, si **arr[2 * i + 2] > arr[i]**, es decir, si el hijo derecho es mayor que el valor actual, se establece como el 'MÁXIMO'.
5. Intercambiamos el 'MÁXIMO' con el elemento actual.
6. Repetimos los pasos **2 al 5** hasta que se restaure la propiedad del montículo.

```python
# Código Python para representar
# la implementación de un Montículo máximo.

class MonticuloMaximo:

    # Un puntero que apunta a los elementos
    # en el arreglo en el Montículo.

    arr = []

    # Tamaño máximo posible del Montículo.

    maxSize = 0

    # Número de elementos en el
    # Montículo máximo en este momento.

    heapSize = 0

    # Función constructora.

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.arr = [None]*maxSize
        self.heapSize = 0

    # Convirtiendo a un subárbol tomando el
    # índice dado como raíz.

    def MonticuloMaximo(self, i):
        l = self.hijoIzq(i)
        r = self.hijoDer(i)
        mayor = i

        if l < self.heapSize and self.arr[l] > self.arr[i]:
            mayor = l

        if r < self.heapSize and self.arr[r] > self.arr[mayor]:
            mayor = r

        if mayor != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[mayor]
            self.arr[mayor] = temp
            self.MonticuloMaximo(mayor)

    # Devuelve el índice del padre
    # del elemento en el índice 'i'.

    def padre(self, i):
        return (i - 1) // 2

    # Devuelve el índice del hijo izquierdo.

    def hijoIzq(self, i):
        return (2 * i + 1)

    # Devuelve el índice del
    # hijo derecho.

    def hijoDer(self, i):
        return (2 * i + 2)

    # Elimina la raíz que en este caso contiene el
    # elemento máximo.

    def eliminarMax(self):

        # Verifica si el arreglo del Montículo
        # está vacío o no.

        if self.heapSize <= 0:
            return None

        if self.heapSize == 1:
            self.heapSize -= 1
            return self.arr[0]

        # Almacena el elemento máximo
        # para eliminarlo.

        raiz = self.arr[0]
        self.arr[0] = self.arr[self.heapSize - 1]
        self.heapSize -= 1

        # Para restaurar la propiedad
        # del Montículo máximo.

        self.MonticuloMaximo(0)

        return raiz

    # Incrementa el valor de la clave en el
    # índice 'i' a newVal.

    def incrementarClave(self, i, newVal):
        self.arr[i] = newVal

        while i != 0 and self.arr[self.padre(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.padre(i)]
            self.arr[self.padre(i)] = temp
            i = self.padre(i)

    # Devuelve la clave máxima
    # (clave en la raíz) del Montículo máximo.

    def obtenerMax(self):
        return self.arr[0]

    def tamanoActual(self):
        return self.heapSize

    # Elimina una clave en el índice dado i.

    def eliminarClave(self, i):

        # Aumenta el valor de la clave
        # a infinito y luego elimina
        # el valor máximo.

        self.incrementarClave(i, float("inf"))
        self.eliminarMax()

    # Inserta una nueva clave 'x' en el Montículo máximo.

    def insertarClave(self, x):

        # Para verificar si se puede insertar la clave
        # o no.

        if self.heapSize == self.maxSize:
            print("\\nDesbordamiento: No se pudo insertar la clave\\n")
            return

        # La nueva clave se inserta inicialmente al final.

        self.heapSize += 1
        i = self.heapSize - 1
        self.arr[i] = x

        # Se verifica la propiedad del Montículo máximo
        # y si se viola, se restaura.

        while i != 0 and self.arr[self.padre(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.padre(i)]
            self.arr[self.padre(i)] = temp
            i = self.padre(i)

# Programa de prueba para probar las funciones anteriores.
if __name__ == '__main__':

    # Suponiendo que el tamaño máximo del Montículo sea 15.
    h = MonticuloMaximo(15)

    # Pidiendo al usuario que ingrese las claves:

    k, i, n = 6, 0, 6

    print("Ingresó 6 claves: 3, 10, 12, 8, 2, 14 \\n")

    h.insertarClave(3)
    h.insertarClave(10)
    h.insertarClave(12)
    h.insertarClave(8)
    h.insertarClave(2)
    h.insertarClave(14)

    # Imprimiendo el tamaño actual del Montículo.
    print("El tamaño actual del Montículo es " + str(h.tamanoActual()) + "\\n")

    # Imprimiendo el elemento raíz que es en realidad el elemento máximo.
    print("El elemento máximo actual es " + str(h.obtenerMax()) + "\\n")

    # Eliminando la clave en el índice 2.
    h.eliminarClave(2)

    # Imprimiendo el tamaño del Montículo después de la eliminación.
    print("El tamaño actual del Montículo es " + str(h.tamanoActual()) + "\\n")

    # Insertando 2 nuevas claves en el Montículo.
    h.insertarClave(15)
    h.insertarClave(5)

    print("El tamaño actual del Montículo es " + str(h.tamanoActual()) + "\\n")

    print("El elemento máximo actual es " + str(h.obtenerMax()) + "\\n")
```

**Salida:**

```bash
Ingresó 6 claves: 3, 10, 12, 8, 2, 14
El tamaño actual del montículo es 6
El elemento máximo actual es 14
El tamaño actual del montículo es 5
El tamaño actual del montículo es 7
El elemento máximo actual es 15
```

# Aplicaciones de la Estructura de Datos Montículo (Heap):

- **Colas de Prioridad:** Las **[colas de prioridad](https://www.geeksforgeeks.org/priority-queue-set-1-introduction/)** pueden ser implementadas de manera eficiente utilizando Montículos Binarios debido a que admite operaciones insert(), delete() y extractmax(), decreaseKey() en **O(log N)**.
- **Montículo Binomial** y **Montículo de Fibonacci** son variaciones del Montículo Binario. Estas variaciones realizan la operación de unión también en **O(log N)**, la cual es una operación de complejidad O(N) en el Montículo Binario.
- **Estadísticas de Orden:** La estructura de datos Montículo puede ser utilizada para encontrar eficientemente el k-ésimo elemento más pequeño (o más grande) en un arreglo. Puedes consultar este artículo de **[gfg](https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/)** para obtener más información sobre el k-ésimo elemento más pequeño o más grande.

# Ventajas de los Montículos (Heaps):

- Acceso rápido al elemento máximo/mínimo (O(1)).
- Operaciones de inserción y eliminación eficientes (O(log n)).
- Tamaño flexible.
- Puede ser implementado eficientemente como un arreglo.
- Adecuado para aplicaciones en tiempo real.

# Desventajas de los Montículos (Heaps):

- No es adecuado para buscar un elemento que no sea el máximo/mínimo (O(n) en el peor caso).
- Sobrecarga de memoria adicional para mantener la estructura de montículo.
- Más lento que otras estructuras de datos como arreglos y listas enlazadas para operaciones que no involucran colas de prioridad.
