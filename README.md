# Análisis de Complejidad: Quick Sort

## Introducción

El análisis de complejidad es una técnica para caracterizar el tiempo que tarda un algoritmo en función del tamaño de la entrada, de forma independiente a la máquina, el lenguaje de programación y el compilador utilizados. Se emplea para evaluar y comparar las variaciones en el tiempo de ejecución de diferentes algoritmos.

**Quick Sort** es uno de los algoritmos de ordenación más utilizados en la práctica. Su complejidad temporal es **O(n log n)** en el caso promedio, aunque puede degradarse a **O(n²)** en el peor caso. En cuanto a la complejidad espacial, varía entre **O(log n)** en el mejor caso y **O(n)** en el peor caso, debido a particiones desequilibradas que generan un árbol de recursión sesgado con una pila de llamadas proporcional a n.

---

## Análisis de Complejidad Temporal

### Mejor caso: O(N log N)

El mejor caso ocurre cuando el pivote seleccionado divide el arreglo en dos mitades iguales. Definimos:

- `T(K)`: complejidad temporal de Quick Sort sobre K elementos.
- `P(K)`: complejidad temporal para encontrar la posición del pivote entre K elementos.

La recurrencia es:

```
T(N) = 2 · T(N/2) + N · c
```

Expandiendo la recurrencia:

```
T(N) = 2 · (2·T(N/4) + (N/2)·c) + N·c
     = 4 · T(N/4) + 2·c·N

En general:
     = 2^k · T(N/2^k) + k·c·N
```

Cuando `2^k = N`, se tiene `k = log₂N`, por lo tanto:

```
T(N) = N · T(1) + N · log₂N
```

**Complejidad resultante: O(N log N)**

---

### Peor caso: O(N²)

El peor caso ocurre cuando el pivote siempre divide el arreglo en una parte de `N-1` elementos y otra de `0`. La recurrencia es:

```
T(N) = T(N-1) + N · c
     = T(N-2) + (N-1)·c + N·c
     = T(N-2) + 2·N·c - c
     ...
     = T(N-k) + k·N·c - c · (k(k-1)/2)
```

Sustituyendo `k = N`:

```
T(N) = T(0) + N²·c - c · (N(N-1)/2)
     = N² - N(N-1)/2
     = N²/2 + N/2
```

**Complejidad resultante: O(N²)**

---

### Caso promedio: O(N log N)

En la práctica, Quick Sort opera con una complejidad promedio de **O(N log N)**, lo que lo convierte en uno de los algoritmos de ordenación más eficientes para grandes volúmenes de datos.

---

## Casos de Uso

Quick Sort se recomienda principalmente cuando:

- Se requiere ordenar **grandes volúmenes de datos** de forma eficiente.
- El espacio en memoria es limitado, aprovechando su baja complejidad espacial de **O(log n)**.
- Se trabaja con **arreglos en memoria** (no con listas enlazadas), donde el acceso aleatorio es rápido.
- El conjunto de datos no presenta patrones que provoquen el peor caso (como arreglos ya ordenados sin aleatorización del pivote).

> ⚠️ **Precaución:** Quick Sort no es estable (no preserva el orden relativo de elementos iguales) y su rendimiento puede degradarse a O(N²) con malas elecciones del pivote.

---

## Comparativa Teórica: Quick Sort vs. Heap Sort

| Criterio                   | Quick Sort          | Heap Sort           |
|----------------------------|---------------------|---------------------|
| Mejor caso                 | O(N log N)          | O(N log N)          |
| Caso promedio              | O(N log N)          | O(N log N)          |
| Peor caso                  | **O(N²)**           | O(N log N)          |
| Complejidad espacial       | O(log N)            | O(1)                |
| Estabilidad                | No estable          | No estable          |
| Rendimiento en la práctica | **Más rápido**      | Más predecible      |
| Localidad de caché         | Alta                | Baja                |
| Uso preferido              | Arreglos en memoria | Garantía de O(N log N) |

### Conclusión de la comparativa

Aunque Heap Sort garantiza O(N log N) incluso en el peor caso, Quick Sort suele ser **más rápido en la práctica** debido a su mejor localidad de caché y menor número de comparaciones e intercambios constantes. Quick Sort también requiere menos espacio adicional que Heap Sort, ya que un montón (heap) es esencialmente un árbol binario completo con sobrecarga de punteros.

**Recomendación:** Para ordenar arreglos en memoria donde la velocidad práctica es prioritaria, se prefiere Quick Sort. Si se necesita una garantía estricta de O(N log N) en todos los casos, Heap Sort es la mejor opción.

---

## Instrucciones de Ejecución

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. **Requisitos Previos:**
   - Tener instalado [Python 3.x](https://www.python.org/downloads/).

2. **Preparación de Datos:**
   - Asegúrate de que el archivo `numeros.txt` se encuentre dentro de la carpeta `Codigo/`. Este archivo debe contener los números a ordenar (uno por línea).

3. **Ejecución del Algoritmo:**
   - Abre una terminal en la raíz del proyecto.
   - Ejecuta el siguiente comando:
     ```bash
     python Codigo/quicksort.py
     ```

4. **Resultados:**
   - El programa imprimirá en la terminal el tiempo total de ejecución en milisegundos y confirmará que el ordenamiento se ha completado.

---

## Referencias

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
- Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley.
- GeeksforGeeks. (2024). *QuickSort Algorithm*. https://www.geeksforgeeks.org/quick-sort/
