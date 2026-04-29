import time
import sys

# Aumentamos el límite de recursividad para manejar listas grandes
sys.setrecursionlimit(100000)

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        # Usamos el elemento central como pivote para evitar el peor caso 
        # en listas que ya podrían estar parcialmente ordenadas
        pivote = lista[len(lista) // 2]
        izq = [x for x in lista if x < pivote]
        centro = [x for x in lista if x == pivote]
        der = [x for x in lista if x > pivote]
        
        return quicksort(izq) + centro + quicksort(der)

def procesar_ordenamiento(nombre_archivo):
    try:
        # Lectura del archivo
        with open(nombre_archivo, "r") as f:
            # Convertimos cada línea en un entero
            numeros = [int(linea.strip()) for linea in f]
        
        print(f"Ordenando {len(numeros)} números...")

        # Medición del tiempo
        inicio = time.time()
        lista_ordenada = quicksort(numeros)
        fin = time.time()

        # Cálculo del tiempo en milisegundos
        tiempo_ms = (fin - inicio) * 1000

        print(f"Ordenamiento completado.")
        print(f"Tiempo de ejecución: {tiempo_ms:.2f} ms")
        
        return lista_ordenada

    except FileNotFoundError:
        print("Error: El archivo 'numeros.txt' no fue encontrado.")
    except ValueError:
        print("Error: El archivo contiene datos que no son números válidos.")

# Ejecución del programa
# Asegúrate de que el archivo se llame 'numeros.txt' y esté en la misma carpeta
procesar_ordenamiento("numeros.txt")
