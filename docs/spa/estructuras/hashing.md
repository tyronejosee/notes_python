# Hashing (Hashing)

El hashing se refiere al proceso de generar una salida de tamaño fijo a partir de una entrada de tamaño variable utilizando fórmulas matemáticas conocidas como funciones hash. Esta técnica determina un índice o ubicación para el almacenamiento de un elemento en una estructura de datos.

![https://media.geeksforgeeks.org/wp-content/cdn-uploads/20220701174812/Hashing.jpg](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20220701174812/Hashing.jpg)

# Necesidad de la estructura de datos Hash

Cada día, los datos en internet están aumentando exponencialmente y siempre es un desafío almacenar estos datos de manera eficiente. En la programación diaria, esta cantidad de datos puede que no sea tan grande, pero aún así es necesario almacenarlos, acceder a ellos y procesarlos de manera fácil y eficiente. Una estructura de datos muy común que se utiliza para este propósito es la estructura de datos Array (arreglo).

Ahora surge la pregunta de si el Array ya existía, ¿cuál era la necesidad de una nueva estructura de datos? La respuesta a esto está en la palabra "eficiencia". Aunque almacenar en un Array toma tiempo O(1), buscar en él toma al menos tiempo O(log n). Este tiempo parece ser pequeño, pero para un gran conjunto de datos puede causar muchos problemas y, a su vez, hace que la estructura de datos Array sea ineficiente.

Así que ahora estamos buscando una estructura de datos que pueda almacenar los datos y buscarlos en tiempo constante, es decir, en tiempo O(1). Aquí es donde entra en juego la estructura de datos Hashing. Con la introducción de la estructura de datos Hash, ahora es posible almacenar los datos fácilmente en tiempo constante y también recuperarlos en tiempo constante.

# Componentes de Hashing

Hay tres componentes principales en el hashing:

1. **Clave (Key):** Una clave puede ser cualquier cosa, ya sea una cadena de texto o un número entero, que se ingresa como entrada en la función hash, la técnica que determina un índice o ubicación para el almacenamiento de un elemento en una estructura de datos.
2. **Función Hash (Hash Function):** La función hash recibe la clave de entrada y devuelve el índice de un elemento en una matriz llamada tabla hash. El índice se conoce como el índice hash.
3. **Tabla Hash (Hash Table):** La tabla hash es una estructura de datos que asigna claves a valores utilizando una función especial llamada función hash. Hash almacena los datos de manera asociativa en una matriz donde cada valor de datos tiene su propio índice único.

![https://media.geeksforgeeks.org/wp-content/uploads/20220701080941/ComponentsofHashing-660x342.png](https://media.geeksforgeeks.org/wp-content/uploads/20220701080941/ComponentsofHashing-660x342.png)

# ¿Cómo funciona el Hashing?

Supongamos que tenemos un conjunto de cadenas {“ab”, “cd”, “efg”} y queremos almacenarlo en una tabla.

Nuestro objetivo principal aquí es buscar o actualizar los valores almacenados en la tabla rápidamente en tiempo O(1) y no estamos preocupados por el orden de las cadenas en la tabla. Entonces, el conjunto dado de cadenas puede actuar como una clave y la cadena en sí actuará como el valor de la cadena, pero ¿cómo almacenar el valor correspondiente a la clave?

- **Paso 1:** Sabemos que las funciones hash (que son fórmulas matemáticas) se utilizan para calcular el valor hash que actúa como el índice de la estructura de datos donde se almacenará el valor.
- **Paso 2:** Así que asignemos
    - “a” = 1,
    - “b” = 2, ... etc, a todos los caracteres alfabéticos.
- **Paso 3:** Por lo tanto, el valor numérico es la suma de todos los caracteres de la cadena:

> “ab” = 1 + 2 = 3, “cd” = 3 + 4 = 7 , “efg” = 5 + 6 + 7 = 18
> 
- **Paso 4:** Ahora, supongamos que tenemos una tabla de tamaño 7 para almacenar estas cadenas. La función hash que se usa aquí es la suma de los caracteres en **clave mod tamaño de tabla**. Podemos calcular la ubicación de la cadena en la matriz tomando **suma(cadena) mod 7**.
- **Paso 5:** Entonces almacenaremos
    - “ab” en 3 mod 7 = 3,
    - “cd” en 7 mod 7 = 0, y
    - “efg” en 18 mod 7 = 4.

![https://media.geeksforgeeks.org/wp-content/uploads/20220630170237/Example.png](https://media.geeksforgeeks.org/wp-content/uploads/20220630170237/Example.png)

La técnica anterior nos permite calcular la ubicación de una cadena dada mediante el uso de una función hash simple y encontrar rápidamente el valor que se almacena en esa ubicación. Por lo tanto, la idea del hashing parece ser una excelente manera de almacenar pares (clave, valor) de datos en una tabla.

# ¿Qué es una función hash?

La **[función hash](https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/)** crea una asignación entre una clave y un valor, esto se hace mediante el uso de fórmulas matemáticas conocidas como funciones hash. El resultado de la función hash se llama valor hash o hash. El valor hash es una representación de la cadena original de caracteres, pero generalmente es más pequeño que el original.

Por ejemplo: Considera un arreglo como un Mapa donde la clave es el índice y el valor es el valor en ese índice. Entonces, para un arreglo A, si tenemos un índice **i** que será tratado como la clave, podemos encontrar el valor simplemente mirando el valor en A[i].

### Tipos de funciones hash:

Existen muchas funciones hash que utilizan claves numéricas o alfanuméricas. Este artículo se enfoca en discutir diferentes **[funciones hash](https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/)**:

1. *[Método de división.]([https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/#:~:text=1. Division Method,the remainder obtained.)**](https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/#:~:text=1.%20Division%20Method,the%20remainder%20obtained.)**)
2. *[Método de cuadrado medio.]([https://www.geeksforgeeks.org/introduction-to-hashing-data-structure-and-algorithm-tutorials/The mid square method is a very good hashing method. It involves two steps to compute the hash value- Square the value of the key k i.e. k2 Extract the middle r digits as the hash value.)**](https://www.geeksforgeeks.org/introduction-to-hashing-data-structure-and-algorithm-tutorials/The%20mid%20square%20method%20is%20a%20very%20good%20hashing%20method.%20It%20involves%20two%20steps%20to%20compute%20the%20hash%20value-%20%20Square%20the%20value%20of%20the%20key%20k%20i.e.%20k2%20Extract%20the%20middle%20r%20digits%20as%20the%20hash%20value.)**)
3. *[Método de plegamiento.]([https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/#:~:text=3. Digit Folding,carry if any.)**](https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/#:~:text=3.%20Digit%20Folding,carry%20if%20any.)**)
4. **[Método de multiplicación.](https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/)**

### Propiedades de una buena función hash

Una función hash que asigna cada elemento a su propia ranura única se conoce como una función hash perfecta. Podemos construir una función hash perfecta si conocemos los elementos y la colección nunca cambia, pero el problema es que no hay una manera sistemática de construir una función hash perfecta dado un conjunto arbitrario de elementos. Afortunadamente, aún obtendremos eficiencia de rendimiento incluso si la función hash no es perfecta. Podemos lograr una función hash perfecta aumentando el tamaño de la tabla hash para que cada valor posible pueda ser acomodado. Como resultado, cada elemento tendrá una ranura única. Aunque este enfoque es factible para un pequeño número de elementos, no es práctico cuando el número de posibilidades es grande.

Entonces, podemos construir nuestra función hash para hacer lo mismo, pero debemos tener cuidado al construir nuestra propia función hash.

Una buena función hash debe tener las siguientes propiedades:

1. Ser computable eficientemente.
2. Debe distribuir uniformemente las claves (cada posición de la tabla tiene la misma probabilidad para cada clave).
3. Debe minimizar las colisiones.
4. Debe tener un factor de carga bajo (número de elementos en la tabla dividido por el tamaño de la tabla).

### Complejidad de calcular el valor hash usando la función hash

- Complejidad temporal: O(n)
- Complejidad espacial: O(1)

# Problema con el Hashing

Si consideramos el ejemplo anterior, la función hash que utilizamos es la suma de las letras, pero si examinamos la función hash de cerca, el problema puede visualizarse fácilmente: para diferentes cadenas, se genera el mismo valor hash.

Por ejemplo: {“ab”, “ba”} ambos tienen el mismo valor hash, y la cadena {“cd”, “be”} también genera el mismo valor hash, etc. Esto se conoce como **colisión** y crea problemas en la búsqueda, inserción, eliminación y actualización de valores.

# ¿Qué es una colisión?

El proceso de hashing genera un número pequeño para una clave grande, por lo que existe la posibilidad de que dos claves puedan producir el mismo valor. La situación donde la clave recién insertada se asigna a una ubicación ya ocupada y debe ser manejada utilizando alguna técnica de manejo de colisiones.

![https://media.geeksforgeeks.org/wp-content/cdn-uploads/20220706102035/Collision-in-Hashing.png](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20220706102035/Collision-in-Hashing.png)

*¿Qué es una colisión en Hashing?*

# Cómo manejar Colisiones

Existen principalmente dos métodos para manejar colisiones:

1. **Separate Chaining (Encadenamiento Separado):** En este método, cada posición de la tabla hash contiene una lista enlazada o una estructura de datos similar que almacena todos los elementos que tienen el mismo valor hash. Cuando ocurre una colisión, el nuevo elemento se agrega a la lista enlazada en esa posición de la tabla hash.
2. **Open Addressing (Direccionamiento Abierto):** En este método, cuando ocurre una colisión, el nuevo elemento se busca en otras ubicaciones de la tabla hash siguiendo una secuencia específica de posiciones. Esto se hace hasta que se encuentre una ubicación vacía donde el nuevo elemento pueda insertarse.

![https://media.geeksforgeeks.org/wp-content/uploads/20220630152726/Collisionresolutiontechnique.png](https://media.geeksforgeeks.org/wp-content/uploads/20220630152726/Collisionresolutiontechnique.png)

*Técnica de resolución de colisiones*

### 1) **Separate Chaining (Encadenamiento Separado)**

La idea es hacer que cada celda de la tabla hash apunte a una lista enlazada de registros que tienen el mismo valor de la función hash. El encadenamiento es simple, pero requiere memoria adicional fuera de la tabla.

Ejemplo: Se nos ha dado una función hash y debemos insertar algunos elementos en la tabla hash utilizando el método de encadenamiento separado para resolver las colisiones.

```
Función hash = clave % 5,
Elementos = 12, 15, 22, 25 y 37.

```

Veamos el enfoque paso a paso de cómo resolver el problema:

- **Paso 1:** Primero, dibujemos la tabla hash vacía, que tendrá un rango posible de valores hash de 0 a 4 según la función hash proporcionada.

![https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230111174847/step15.png](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230111174847/step15.png)

*Tabla hash*

- **Paso 2:** Ahora insertemos todas las claves en la tabla hash una por una. La primera clave a insertar es 12, que se asigna al número de cubo 2, que se calcula usando la función hash 12%5=2.

![https://media.geeksforgeeks.org/wp-content/uploads/20230719111021/step1.png](https://media.geeksforgeeks.org/wp-content/uploads/20230719111021/step1.png)

*Insertar 12*

- **Paso 3:** Ahora la siguiente clave es 22. Se asignará al número de cubo 2 porque 22%5=2. Pero el cubo 2 ya está ocupado por la clave 12.

![https://media.geeksforgeeks.org/wp-content/uploads/20230719111103/step2.png](https://media.geeksforgeeks.org/wp-content/uploads/20230719111103/step2.png)

*Insertar 22*

- **Paso 4:** La siguiente clave es 15. Se asignará al número de cubo 0 porque 15%5=0.

![https://media.geeksforgeeks.org/wp-content/uploads/20230719111131/step3.png](https://media.geeksforgeeks.org/wp-content/uploads/20230719111131/step3.png)

*Insertar 15*

- **Paso 5:** Ahora la siguiente clave es 25. Su número de cubo será 25%5=0. Pero el cubo 0 ya está ocupado por la clave 15. Entonces el método de encadenamiento separado manejará la colisión creando una lista enlazada para el cubo 0.

![https://media.geeksforgeeks.org/wp-content/uploads/20230719111211/step4.png](https://media.geeksforgeeks.org/wp-content/uploads/20230719111211/step4.png)

*Insertar 25*

De esta manera, se utiliza el método de encadenamiento separado como técnica de resolución de colisiones.

### 2) **Open Addressing (Dirección Abierta)**

En el enfoque de dirección abierta, todos los elementos se almacenan directamente en la tabla hash. Cada entrada de la tabla contiene un registro o NIL. Cuando buscamos un elemento, examinamos las ubicaciones de la tabla una por una hasta que se encuentre el elemento deseado o quede claro que el elemento no está en la tabla.

### 2.a) Linear Probing (Sondeo Lineal)

En el sondeo lineal, la tabla hash se busca secuencialmente a partir de la ubicación original del hash. Si el caso en el que la ubicación que obtenemos ya está ocupada, entonces buscamos la siguiente ubicación.

**Algoritmo:**

> Calcular la clave hash, es decir, clave = datos % tamañoTabla.Si hashTable[clave] está vacío, almacenar el valor directamente mediante hashTable[clave] = datos.Si el índice hash ya tiene algún valor, entonces buscar el siguiente índice utilizando clave = (clave+1) % tamañoTabla. Si el siguiente índice hashTable[clave] está disponible, almacenar el valor allí. En caso contrario, intentar con el siguiente índice.Repetir el proceso anterior hasta que encontremos un espacio disponible.
> 

**Ejemplo:** Consideremos una función hash simple como "clave mod 5" y una secuencia de claves que deben insertarse son 50, 70, 76, 85, 93.

- **Paso 1:** Primero, dibujemos la tabla hash vacía, que tendrá un rango posible de valores hash de 0 a 4 según la función hash proporcionada.

![https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230111173601/step14.png](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230111173601/step14.png)

*Tabla hash*

- **Paso 2:** Ahora insertemos todas las claves en la tabla hash una por una. La primera clave es 50. Se asignará al número de cubo 0 porque 50%5=0. Por lo tanto, insértela en el número de cubo 0.

![https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230111173912/step21.png](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230111173912/step21.png)

*Insertar 50 en la tabla hash*

- **Paso 3:** La siguiente clave es 70. Se asignará al número de cubo 0 porque 70%5=0, pero el cubo 0 ya está ocupado por 50, así que busque el siguiente espacio vacío e insértela.

![https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230111174000/step31.png](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230111174000/step31.png)

*Insertar 70 en la tabla hash*

- **Paso 4:** La siguiente clave es 76. Se asignará al número de cubo 1 porque 76%5=1, pero el cubo 1 ya está ocupado por 70, así que busque el siguiente espacio vacío e insértela.

![https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230111174038/step41.png](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230111174038/step41.png)

*Insertar 76 en la tabla hash*

- **Paso 5:** La siguiente clave es 93. Se asignará al número de cubo 3 porque 93%5=3, así que insértela en el número de cubo 3.

![https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230111174122/step51.png](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230111174122/step51.png)

*Insertar 93 en la tabla hash*

### 2.b) Quadratic Probing (Sondeo Cuadrático)

El sondeo cuadrático es un esquema de dirección abierta en programación de computadoras para resolver colisiones de hash en tablas hash. El sondeo cuadrático opera tomando el índice hash original y agregando valores sucesivos de un polinomio cuadrático arbitrario hasta que se encuentre un espacio abierto.

Una secuencia de ejemplo usando el sondeo cuadrático es:

> H + 12, H + 22, H + 32, H + 42,……………. H + k2
> 

Este método también se conoce como el método de cuadrado medio porque en este método buscamos la i-ésima sonda (ranura) en la i-ésima iteración y el valor de i = 0, 1, . . . n – 1. Siempre comenzamos desde la ubicación hash original. Si solo la ubicación está ocupada, entonces revisamos las otras ranuras.

Si hash(x) es el índice de ranura calculado utilizando la función hash y n es el tamaño de la tabla hash:

> Si la ranura hash(x) % n está llena, entonces intentamos (hash(x) + 12) % n.Si (hash(x) + 12) % n también está lleno, entonces intentamos (hash(x) + 22) % n.Si (hash(x) + 22) % n también está lleno, entonces intentamos (hash(x) + 32) % n.Este proceso se repetirá para todos los valores de i hasta que se encuentre una ranura vacía.
> 

Ejemplo: Consideremos un tamaño de tabla = 7, función hash como Hash(x) = x % 7 y estrategia de resolución de colisiones como f(i) = i2. Insertar = 22, 30 y 50.

- **Paso 1:** Crear una tabla de tamaño 7.

![https://media.geeksforgeeks.org/wp-content/uploads/20220630135032/step1.png](https://media.geeksforgeeks.org/wp-content/uploads/20220630135032/step1.png)

*Tabla hash*

- **Paso 2** – Insertar 22 y 30
    - Hash(25) = 22 % 7 = 1, como la celda en el índice 1 está vacía, podemos insertar fácilmente 22 en la ranura 1.
    - Hash(30) = 30 % 7 = 2, como la celda en el índice 2 está vacía, podemos insertar fácilmente 30 en la ranura 2.

![https://media.geeksforgeeks.org/wp-content/uploads/20220630140632/step3.png](https://media.geeksforgeeks.org/wp-content/uploads/20220630140632/step3.png)

*Insertar clave 22 y 30 en la tabla hash*

- **Paso 3:** Insertar 50
    - Hash(25) = 50 % 7 = 1
    - En nuestra tabla hash, la ranura 1 ya está ocupada. Por lo tanto, buscaremos la ranura 1+1, es decir, 1+1 = 2.
        
        2
        
    - Nuevamente se encuentra ocupada la ranura 2, por lo que buscaremos la celda 1+2, es decir, 1+4 = 5.
        
        2
        
    - Ahora, la celda 5 no está ocupada, por lo que colocaremos 50 en la ranura 5.

![https://media.geeksforgeeks.org/wp-content/uploads/20220630142522/step4.png](https://media.geeksforgeeks.org/wp-content/uploads/20220630142522/step4.png)

*Insertar clave 50 en la tabla hash*

### 2.c) Doble Hashing (Doble Sondeo)

Doble hashing es una técnica para resolver colisiones en tablas hash de dirección abierta. Doble hashing hace uso de dos funciones de hash:

- La primera función de hash es h1(k), que toma la clave y proporciona una ubicación en la tabla hash. Si la nueva ubicación no está ocupada o vacía, entonces podemos colocar fácilmente nuestra clave en esa posición.
- Pero en caso de que la ubicación esté ocupada (colisión), utilizaremos una segunda función de hash h2(k) en combinación con la primera función de hash h1(k) para encontrar una nueva ubicación en la tabla hash.

Esta combinación de funciones de hash tiene la forma:

```
h(k, i) = (h1(k) + i * h2(k)) % n
```

donde:

- i es un número entero no negativo que indica el número de colisión,
- k = elemento/clave que está siendo hasheado,
- n = tamaño de la tabla hash.

**Complejidad del algoritmo de Doble Hashing:**

```
Complejidad temporal: O(n)
```

**Ejemplo:** Insertar las claves 27, 43, 692 y 72 en una tabla hash de tamaño 7, donde la primera función de hash es h1(k) = k mod 7 y la segunda función de hash es h2(k) = 1 + (k mod 5).

- **Paso 1:** Insertar 27
    - 27 % 7 = 6, la ubicación 6 está vacía, así que insertamos 27 en la ranura 6.

![https://media.geeksforgeeks.org/wp-content/uploads/20220630163738/step2.png](https://media.geeksforgeeks.org/wp-content/uploads/20220630163738/step2.png)

*Insertar clave 27 en la tabla hash*

- **Paso 2:** Insertar 43
    - 43 % 7 = 1, la ubicación 1 está vacía, así que insertamos 43 en la ranura 1.

![https://media.geeksforgeeks.org/wp-content/uploads/20220630163859/step2.png](https://media.geeksforgeeks.org/wp-content/uploads/20220630163859/step2.png)

*Insertar clave 43 en la tabla hash*

- **Paso 3:** Insertar 692
    - 692 % 7 = 6, pero la ubicación 6 ya está ocupada y esto es una colisión.
    - Así que necesitamos resolver esta colisión utilizando el doble sondeo.

```
hnew = [h1(692) + i * h2(692)] % 7
= [6 + 1 * (1 + 692 % 5)] % 7
= 9 % 7
= 2

Ahora, como 2 es una ranura vacía,
podemos insertar 692 en la 2ª ranura.
```

![https://media.geeksforgeeks.org/wp-content/uploads/20221202114800/step3.png](https://media.geeksforgeeks.org/wp-content/uploads/20221202114800/step3.png)

*Insertar clave 692 en la tabla hash*

- **Paso 4:** Insertar 72
    - 72 % 7 = 2, pero la ubicación 2 ya está ocupada y esto es una colisión.
    - Por lo tanto, necesitamos resolver esta colisión usando doble hashing.

```
hnew = [h1(72) + i * (h2(72)] % 7
= [2 + 1 * (1 + 72 % 5)] % 7
= 5 % 7
= 5,

Ahora, como 5 es una ranura vacía,
podemos insertar 72 en la quinta ranura.
```

![https://media.geeksforgeeks.org/wp-content/uploads/20221202114839/step4.png](https://media.geeksforgeeks.org/wp-content/uploads/20221202114839/step4.png)

*Insertar la clave 72 en la tabla hash*

# ¿Qué significa el Factor de Carga (Load Factor) en el Hashing?

El **factor de carga** en una tabla hash se puede definir como el número de elementos que contiene la tabla hash dividido por el tamaño de la tabla hash. El factor de carga es el parámetro decisivo que se utiliza cuando queremos volver a aplicar la función hash anterior o cuando queremos agregar más elementos a la tabla hash existente.

El factor de carga nos ayuda a determinar la eficiencia de la función hash, es decir, nos indica si la función hash que estamos utilizando está distribuyendo las claves uniformemente o no en la tabla hash.

La fórmula para calcular el factor de carga es:

```
Factor de Carga = Total de elementos en la tabla hash / Tamaño de la tabla hash
```

# ¿Qué es el Rehashing?

Como sugiere el nombre, el rehashing significa volver a aplicar la función hash. Básicamente, cuando el factor de carga aumenta más allá de su valor predefinido (el valor predeterminado del factor de carga es 0.75), la complejidad aumenta. Para superar esto, el tamaño del arreglo se incrementa (se duplica) y todos los valores se vuelven a aplicar la función hash y se almacenan en el nuevo arreglo de tamaño doble para mantener un factor de carga bajo y una complejidad baja.

# Aplicaciones de la estructura de datos Hash

- Hash se utiliza en bases de datos para la indexación.
- Hash se utiliza en estructuras de datos basadas en disco.
- En algunos lenguajes de programación como Python, JavaScript, el hash se utiliza para implementar objetos.

# Aplicaciones en tiempo real de la estructura de datos Hash

- Hash se utiliza para el mapeo de caché para un acceso rápido a los datos.
- Hash se puede utilizar para la verificación de contraseñas.
- Hash se utiliza en criptografía como un resumen del mensaje.
- Algoritmo Rabin-Karp para el emparejamiento de patrones en una cadena.
- Cálculo del número de subcadenas diferentes de una cadena.

# Ventajas de la estructura de datos Hash

- Hash proporciona una mejor sincronización que otras estructuras de datos.
- Las tablas de hash son más eficientes que los árboles de búsqueda u otras estructuras de datos.
- Hash proporciona tiempo constante para las operaciones de búsqueda, inserción y eliminación en promedio.

# Desventajas de la estructura de datos Hash

- Hash es ineficiente cuando hay muchas colisiones.
- Las colisiones de hash no se evitan prácticamente para un gran conjunto de claves posibles.
- Hash no permite valores nulos.

# Conclusión

A partir de la discusión anterior, concluimos que el objetivo del hashing es resolver el desafío de encontrar un elemento rápidamente en una colección. Por ejemplo, si tenemos una lista de millones de palabras en inglés y deseamos encontrar un término en particular, usaríamos hashing para localizarlo y encontrarlo de manera más eficiente. Sería ineficiente verificar cada elemento en las millones de listas hasta que encontremos una coincidencia. El hashing reduce el tiempo de búsqueda al restringir la búsqueda a un conjunto más pequeño de palabras al principio.
