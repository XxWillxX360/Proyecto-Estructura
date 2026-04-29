# Proyecto-Estructura
El análisis de complejidad se define como una técnica para caracterizar el tiempo que tarda un algoritmo en función del tamaño de la entrada (independientemente de la máquina, el lenguaje y el compilador). Se utiliza para evaluar las variaciones en el tiempo de ejecución de diferentes algoritmos.

La complejidad temporal de Quick Sort es O(n log n) en promedio , pero puede llegar a ser O(n^2) en el peor de los casos . La complejidad espacial de Quick Sort en el mejor de los casos es O(log n) , mientras que en el peor de los casos , se convierte en O(n) debido a una partición desequilibrada que provoca un árbol de recursión sesgado que requiere una pila de llamadas de tamaño O(n).

# Análisis de complejidad temporal en el mejor caso de Quick Sort: O(N * logN)
T(K): Complejidad temporal del quicksort de K elementos.
P(K): Complejidad temporal para encontrar la posición del pivote entre K elementos.

El mejor caso se da cuando seleccionamos el pivote como la media. Entonces, aquí

T(N) = 2 * T(N / 2) + N * constante

Ahora T(N/2) también es 2*T(N/4) + N/2 * constante. Entonces,

T(N) = 2*(2*T(N / 4) + N / 2 * constante) + N * constante 
= 4 * T(N / 4) + 2 * constante * N.

Entonces, podemos decir que

T(N) = 2 k * T(N / 2 k ) + k * constante * N

entonces, 2 k = N 
k = log 2 N

Entonces T(N) = N * T(1) + N * log 2 N . Por lo tanto, la complejidad temporal es O(N * logN) .

# Análisis de complejidad temporal en el peor de los casos de Quick Sort: O(N 2 ) .
El peor caso ocurrirá cuando el arreglo se divida en dos partes, una parte que consta de N-1 elementos y la otra, y así sucesivamente. Entonces,

T(N) = T(N - 1) + N * constante 
= T(N - 2) + (N - 1) * constante + N * constante = T(N - 2) + 2 * N * constante - constante 
= T(N - 3) + 3 * N * constante - 2 * constante - constante 
. . . 
= T(N - k) + k * N * constante - (k - 1) * constante - . . . - 2*constante - constante 
= T(N - k) + k * N * constante - constante * (k*(k - 1))/2

Si sustituimos k = N en la ecuación anterior, entonces

T(N) = T(0) + N * N * constante - constante * (N * (N-1)/2) 
= N 2 - N*(N-1)/2 
= N 2 /2 + N/2

Por lo tanto, la complejidad en el peor de los casos es O( N² )

# Casos de uso (¿Cuándo es mejor usarlo?).
se utiliza principalmente cuando se requiere ordenar grandes volúmenes de datos de manera eficiente y rápida, siendo uno de los algoritmos más rápidos en la práctica con una complejidad promedio de \(O(n \log n)\).

Quicksort puede tener algunas desventajas, pero es el algoritmo de ordenación más rápido y eficiente disponible. Quicksort tiene una O(log n)complejidad espacial baja, lo que lo convierte en una excelente opción para situaciones donde el espacio es limitado.

Aunque el tiempo de ejecución en el peor de los casos siempre es el mismo, Quicksort suele ser más rápido que HeapSort (nlogn). Quicksort ocupa menos espacio que HeapSort debido a que un montón es prácticamente un árbol binario completo con la sobrecarga de punteros. Por lo tanto, a la hora de ordenar matrices, se prefiere Quicksort. 

# comparativa teórica contra otro método.
Quicksort puede tener algunas desventajas, pero es el algoritmo de ordenación más rápido y eficiente disponible. Quicksort tiene una O(log n)complejidad espacial baja, lo que lo convierte en una excelente opción para situaciones donde el espacio es limitado.

Aunque el tiempo de ejecución en el peor de los casos siempre es el mismo, Quicksort suele ser más rápido que HeapSort (nlogn). Quicksort ocupa menos espacio que HeapSort debido a que un montón es prácticamente un árbol binario completo con la sobrecarga de punteros. Por lo tanto, a la hora de ordenar matrices, se prefiere Quicksort.