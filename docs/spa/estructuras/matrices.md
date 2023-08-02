# Matriz o Cuadrícula

# ¿Qué es una Matriz?

> Una matriz es un arreglo bidimensional que consta de filas y columnas. Es una disposición de elementos en líneas horizontales o verticales de entradas.
> 

![https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221025113549/Introduction-to-Matrix-Grid.png](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221025113549/Introduction-to-Matrix-Grid.png)

*Introducción a la Matriz o Cuadrícula - Tutoriales de Estructuras de Datos y Algoritmos*

# Declaración de una Matriz o Cuadrícula

La sintaxis para declarar una Matriz o un arreglo bidimensional es muy similar a la de un arreglo unidimensional, y se presenta de la siguiente manera.

```
int arr[numero_de_filas][numero_de_columnas];
```

Sin embargo, produce una estructura de datos que se ve como la siguiente:

![https://media.geeksforgeeks.org/wp-content/uploads/20221010013429/twod-660x252.png](https://media.geeksforgeeks.org/wp-content/uploads/20221010013429/twod-660x252.png)

*Representación de una matriz*

Como se puede observar en la imagen anterior, los elementos están organizados en filas y columnas. Como se muestra en la imagen, la celda x[0][0] es el primer elemento de la primera fila y la primera columna. El valor en el primer par de corchetes representa el número de fila y el valor dentro del segundo par de corchetes representa el número de columna (es decir, x[fila][columna]).

# Inicialización de Matrices o Cuadrículas

Existen dos métodos para inicializar arreglos bidimensionales.

**Método 1**

> int arr[4][3]={1, 2, 3, 4, 5, 6, 20, 80, 90, 100, 110, 120};
> 

**Método 2**

> int arr[4][3]={{1, 2, 3}, {4, 5, 6}, {20, 80, 90}, {100, 110, 120}};
> 

Aquí hay dos métodos de inicialización de elementos durante la declaración. En este caso, el segundo método es preferible porque es más legible y comprensible, de modo que puedes visualizar que **arr[][] comprende** cuatro filas y tres columnas.

# Cómo acceder a los datos en una Matriz o Cuadrícula

Al igual que en los arreglos unidimensionales, las matrices se pueden acceder de manera aleatoria utilizando sus índices para acceder a los elementos individuales. Una celda tiene dos índices, uno para su **número de fila** y otro para su **número de columna**. Podemos usar **X[i][j]** para acceder al elemento que se encuentra en la **i-ésima** fila y la **j-ésima** columna de la matriz.

![https://media.geeksforgeeks.org/wp-content/uploads/20221010013158/2Darray.png](https://media.geeksforgeeks.org/wp-content/uploads/20221010013158/2Darray.png)

*Matriz*

La sintaxis para acceder a un elemento de la matriz que se encuentra en la **i-ésima** fila y la **j-ésima** columna:

```
int valor = X[i][j];
```

# Cómo Imprimir los Elementos de una Matriz o Cuadrícula:

La impresión de elementos de una matriz o un arreglo bidimensional se puede hacer utilizando dos bucles "for".

```bash
arr = [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12] ]

for i in range(0, 3):
    for j in range(0, 4):
        print(arr[i][j], end=" ")
    print("")

# Este código fue contribuido por akashish__
```

**Salida:**

```bash
1 2 3 4
5 6 7 8
9 10 11 12
```

# Algunos problemas básicos en Matrices/Cuadrículas que debes conocer:

### 1. **[Búsqueda en una matriz:](https://www.geeksforgeeks.org/search-element-sorted-matrix/)**

Dada una matriz mat[][] de tamaño N x M, donde cada fila y columna está ordenada en orden creciente, y se proporciona un número X. La tarea es encontrar si el elemento X está presente en la matriz o no.

**Ejemplos:**

> Entrada: mat[][] = { {1, 5, 9},                    {14, 20, 21},                    {30, 34, 43} }       x = 14Salida: SÍEntrada: mat[][] = { {1, 5, 9, 11},                    {14, 20, 21, 26},                    {30, 34, 43, 50} }       x = 42Salida: NO
> 

**Solución:**

Hay muchas formas de resolver este problema, pero discutamos la idea de un enfoque muy ingenuo o de fuerza bruta aquí.

> Una solución simple es comparar uno a uno x con cada elemento de la matriz. Si coincide, devuelve verdadero. Si llegamos al final, devuelve falso. La complejidad temporal de esta solución es O(n x m).
> 

A continuación se muestra la implementación de la idea anterior:

```python
# Código en Python para el enfoque anterior

def buscarEnMatriz(arr, x):

    for i in range(0, 4):
        for j in range(0, 5):
            if arr[i][j] == x:
                return 1
    return 0

x = 8

arr = [[0, 6, 8, 9, 11],
       [20, 22, 28, 29, 31],
       [36, 38, 50, 61, 63],
       [64, 66, 100, 122, 128]]

if buscarEnMatriz(arr, x):
    print("SÍ")
else:
    print("NO")

# Este código fue contribuido por ishankhandelwals.
```

**Salida:**

```bash
SÍ
```

**Complejidad Temporal:** O(M*N), donde M y N son el número de filas y columnas respectivamente.

**Espacio Auxiliar:** O(1)

### 2. **[Programa para imprimir las Diagonales de una Matriz](https://www.geeksforgeeks.org/program-to-print-the-diagonals-of-a-matrix/)**

Dada una matriz cuadrada 2D, imprime las diagonales principal y secundaria.

**Ejemplos:**

> Entrada: 1 2 3 44 3 2 17 8 9 66 5 4 3Salida:Diagonal Principal: 1, 3, 9, 3Diagonal Secundaria: 4, 2, 8, 6Entrada:1 1 11 1 11 1 1Salida:Diagonal Principal: 1, 1, 1Diagonal Secundaria: 1, 1, 1
> 

**Solución:**

> La diagonal principal está formada por los elementos A00, A11, A22, A33.Condición para la Diagonal Principal: La condición fila-columna es fila = columna.La diagonal secundaria está formada por los elementos A03, A12, A21, A30. Condición para la Diagonal Secundaria: La condición fila-columna es fila = númeroDeFilas - columna - 1.
> 

```python
# Programa en Python3 para imprimir las Diagonales de una Matriz

MAX = 100

# Función para imprimir la Diagonal Principal

def imprimirDiagonalPrincipal(mat, n):
    print("Diagonal Principal: ", end="")
    for i in range(0, n):
        for j in range(0, n):
            # Condición para la diagonal principal
            if (i == j):
                print(mat[i][j], ", ", end="")
    print("")

# Función para imprimir la Diagonal Secundaria

def imprimirDiagonalSecundaria(mat, n):
    print("Diagonal Secundaria: ", end="")
    for i in range(0, n):
        for j in range(0, n):
            # Condición para la diagonal secundaria
            if ((i + j) == (n - 1)):
                print(mat[i][j], ", ", end="")
    print("")

# Código de ejecución

n = 4

a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [1, 2, 3, 4],
     [5, 6, 7, 8]]

imprimirDiagonalPrincipal(a, n)
imprimirDiagonalSecundaria(a, n)

# Este código fue contribuido por akashish__
```

---

**Salida:**

```bash
Diagonal Principal: 1, 6, 3, 8,
Diagonal Secundaria: 4, 7, 2, 5,
```

**Complejidad Temporal:** O(n2), ya que hay un bucle anidado involucrado, la complejidad temporal es cuadrada.

**Espacio Auxiliar:** O(1).

### **3. [Ordenar la matriz dada:](https://www.geeksforgeeks.org/sort-given-matrix/)**

Dada una matriz de tamaño n x n, el problema consiste en ordenar la matriz dada en un orden estricto. Aquí, el orden estricto significa que la matriz está ordenada de tal manera que todos los elementos en una fila están ordenados en orden creciente y, para la fila 'i', donde 1 <= i <= n-1, el primer elemento de la fila 'i' es mayor o igual que el último elemento de la fila 'i-1'.

**Ejemplos:**

> Entrada: mat[][] = { {5, 4, 7},                          {1, 3, 8},                         {2, 9, 6} }Salida: 1 2 3             4 5 6             7 8 9
> 

**Solución:**

> La idea para resolver este problema es crear una matriz temporal temp[] de tamaño n^2. Comenzando con la primera fila, copia los elementos de la matriz dada en temp[]. Ordena temp[]. Ahora, uno por uno, copia los elementos de temp[] de regreso a la matriz dada.
> 

A continuación se muestra la implementación:

```python
# Implementación en Python para ordenar la matriz dada

def ordenarMatriz(mat, n):

    # matriz temporal de tamaño n^2
    temp = [0] * (n * n)
    k = 0

    # copia los elementos de la matriz uno por uno
    # en temp[]
    for i in range(n):
        for j in range(n):
            temp[k] = mat[i][j]
            k += 1

    # ordena temp[]
    temp.sort()

    # copia los elementos de temp[] uno por uno
    # en mat[][]
    k = 0
    for i in range(n):
        for j in range(n):
            mat[i][j] = temp[k]
            k += 1

# función para imprimir la matriz dada
def imprimirMatriz(mat, n):
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=' ')
        print("")

# programa de prueba

mat = [[5, 4, 7],
       [1, 3, 8],
       [2, 9, 6]]

n = 3

print("Matriz Original:")
imprimirMatriz(mat, n)

ordenarMatriz(mat, n)

print("\\nMatriz Después de Ordenar:")
imprimirMatriz(mat, n)

# Este código fue contribuido por ishankhandelwals.
```

**Salida:**

```bash
Matriz Original:
5 4 7
1 3 8
2 9 6

Matriz Después de Ordenar:
1 2 3
4 5 6
7 8 9
```

**Complejidad Temporal:** O(n2log2n).

**Espacio Auxiliar:** O(n2), ya que se ha tomado espacio extra n * n.

### 4. **[Rotar una Matriz 180 grados](https://www.geeksforgeeks.org/rotate-matrix-180-degree/)**

Dada una matriz cuadrada, la tarea es girarla 180 grados en sentido antihorario sin usar espacio adicional.

**Ejemplos:**

> Entrada:  1  2  3        4  5  6        7  8  9Salida: 9 8 7         6 5 4         3 2 1Entrada:  1 2 3 4         5 6 7 8         9 0 1 2         3 4 5 6Salida: 6 5 4 3         2 1 0 9         8 7 6 5         4 3 2 1
> 

**Solución:**

> Hay cuatro pasos necesarios para resolver este problema:1- Encontrar la traspuesta de la matriz. 2- Invertir las columnas de la traspuesta. 3- Encontrar la traspuesta de la matriz nuevamente. 4- Invertir las columnas de la traspuesta nuevamente.
> 

**Ilustración:**

> Supongamos que tenemos la matriz siguiente:1  2  3  45  6  7  89  10 11 1213 14 15 16Primero encontramos la traspuesta.1 5 9 132 6 10 143 7 11 154 8 12 16Luego invertimos los elementos de cada columna.4 8 12 163 7 11 152 6 10 141 5  9 13Luego hacemos la traspuesta nuevamente.4 3 2 1 8 7 6 5 12 11 10 916 15 14 13Finalmente, invertimos los elementos de cada columna nuevamente.16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
> 

A continuación se muestra la implementación:

```python
# Programa en Python para rotación izquierda de la matriz en 180 grados

R = 4
C = 4

# Función para rotar la matriz en 180 grados
def columnasInvertidas(arr):
    for i in range(C):
        for j in range(0, int(C / 2)):
            x = arr[j][i]
            arr[j][i] = arr[C - 1 - j][i]
            arr[C - 1 - j][i] = x

# Función para transponer la matriz
def transponer(arr):
    for i in range(R):
        for j in range(i, C):
            x = arr[j][i]
            arr[j][i] = arr[i][j]
            arr[i][j] = x

# Función para mostrar la matriz
def imprimirMatriz(arr):
    for i in range(R):
        for j in range(C):
            print(arr[i][j], end=' ')
        print()

# Función para rotar la matriz en sentido antihorario en 180 grados
def rotar180(arr):
    transponer(arr)
    columnasInvertidas(arr)
    transponer(arr)
    columnasInvertidas(arr)

# Código de ejecución
arr = [[1, 2, 3, 4 ],
       [5, 6, 7, 8 ],
       [9, 10, 11, 12 ],
       [13, 14, 15, 16 ]]

rotar180(arr)

imprimirMatriz(arr)

# Este código fue contribuido por akashish__
```

**Salida:**

```bash
16 15 14 13
12 11 10 9
8 7 6 5
4 3 2 1
```

**Complejidad Temporal:** O(R*C)

**Espacio Auxiliar:** O(1)

### Encontrar elementos únicos en una matriz

Dada una matriz mat[][] con n filas y m columnas, necesitamos encontrar los elementos únicos en la matriz, es decir, aquellos elementos que no se repiten en la matriz o cuya frecuencia es 1.

**Ejemplos:**

> Entrada:  20  15  30  2        2   3   5   30        6   7   6   8Salida: 3  20  5  7  8  15Entrada:  1  2  3          5  6  2        1  3  5        6  2  2Salida: No hay elementos únicos en la matriz
> 

**Solución:**

> La idea es usar el hashing y recorrer todos los elementos de la matriz. Si un elemento está presente en el diccionario, incrementar su contador. De lo contrario, insertar un elemento con valor = 1.
> 

A continuación se muestra la implementación:

```python
# Programa en Python para encontrar elementos únicos
# en una matriz

# Función que calcula los elementos únicos
def unicos(mat, n, m):
    maximum = 0
    flag = 0

    for i in range(n):
        for j in range(m):
            if maximum < mat[i][j]:
                maximum = mat[i][j]

    b = [0] * (maximum + 1)

    for i in range(n):
        for j in range(m):
            y = mat[i][j]
            b[y] += 1

    for i in range(1, maximum+1):
        if b[i] == 1:
            print(i, end=' ')
            flag = 1

    if flag == 0:
        print("No hay elementos únicos en la matriz")

R = 4
C = 4

mat = [[1, 2, 3, 20],
       [5, 6, 20, 25],
       [1, 3, 5, 6],
       [6, 7, 8, 15]]

# Función que calcula elementos únicos
unicos(mat, R, C)

# Este código fue contribuido por lokesh.
```

**Salida:**

```bash
2 7 8 15 25
```

**Complejidad Temporal:** O(m*n) donde m es el número de filas y n es el número de columnas.

**Espacio Auxiliar:** O(máximo de la matriz).
