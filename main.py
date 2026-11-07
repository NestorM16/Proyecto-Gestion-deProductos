# main.py
import time
import random
from gestion_productos import generar_productos
from ordenamiento import insertion_sort, merge_sort, quick_sort
from busqueda import busqueda_binaria, busqueda_lineal_por_nombre

def main():
    print("="*85)
    print(" SIMULACIÓN COMPLETA: GESTIÓN, ORDENAMIENTO Y BÚSQUEDA DE PRODUCTOS")
    print("="*85)
    
    # 1. Generar los datos base (Parte 1)
    lista_productos = generar_productos()
    print(f"-> Se generaron {len(lista_productos)} productos exitosamente.\n")

    # ==========================================
    # PARTE 2: Ordenamiento y Medición de Tiempos
    # ==========================================
    print("--- EJECUTANDO PARTE 2: ALGORITMOS DE ORDENAMIENTO Y RENDIMIENTO ---")
    
    criterios = [
        {"nombre": "Precio (Ascendente)", "key": lambda p: p.precio, "reverse": False},
        {"nombre": "Calificación Promedio (Descendente)", "key": lambda p: p.calificacionPromedio, "reverse": True}
    ]

    algoritmos = [
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]

    print(f"{'CRITERIO DE ORDENAMIENTO':<38} | {'ALGORITMO':<15} | {'TIEMPO (1000 iteraciones)':<25}")
    print("-" * 85)

    for crit in criterios:
        for nombre_alg, func_alg in algoritmos:
            inicio = time.perf_counter()
            for _ in range(1000):
                _ = func_alg(lista_productos, key=crit["key"], reverse=crit["reverse"])
            fin = time.perf_counter()
            
            tiempo_total = fin - inicio
            print(f"{crit['nombre']:<38} | {nombre_alg:<15} | {tiempo_total:.6f} segundos")

    print("="*85 + "\n")

    # ==========================================
    # PARTE 3.1: Búsqueda por ID (Búsqueda Binaria)
    # ==========================================
    print("--- EJECUTANDO PARTE 3.1: BÚSQUEDA BINARIA POR ID ---")
    
    # Ordenar el arreglo por id usando Quick Sort (requisito para búsqueda binaria)
    productos_ordenados_id = quick_sort(lista_productos, key=lambda p: p.id, reverse=False)
    
    ids_existentes = random.sample(range(1, 51), 10)
    ids_no_existentes = list(range(100, 110))
    
    inicio = time.perf_counter()
    for _ in range(1000):
        for i_id in ids_existentes:
            _ = busqueda_binaria(productos_ordenados_id, i_id)
    tiempo_id_ex = time.perf_counter() - inicio

    inicio = time.perf_counter()
    for _ in range(1000):
        for i_id in ids_no_existentes:
            _ = busqueda_binaria(productos_ordenados_id, i_id)
    tiempo_id_no_ex = time.perf_counter() - inicio

    print(f"IDs existentes probados: {ids_existentes}")
    print(f"Tiempo total (1000 iteraciones x 10 IDs existentes): {tiempo_id_ex:.6f} segundos")
    print(f"IDs no existentes probados: {ids_no_existentes}")
    print(f"Tiempo total (1000 iteraciones x 10 IDs no existentes): {tiempo_id_no_ex:.6f} segundos\n")

    # ==========================================
    # PARTE 3.2: Búsqueda por Nombre (Búsqueda Lineal)
    # ==========================================
    print("--- EJECUTANDO PARTE 3.2: BÚSQUEDA LINEAL POR SUBCADENA ---")
    
    subcadenas_con_resultados = ["Smartphone", "Camisa", "Libro", "Cafetera", "Laptop", "Jean", "Cocina", "Sábanas", "Cámara", "Smartwatch"]
    subcadenas_sin_resultados = ["Helicóptero", "Patineta", "Guitarra", "Microscopio", "Robot", "Zepelín", "Monopatín", "Casco", "Astronauta", "Submarino"]

    inicio = time.perf_counter()
    for _ in range(1000):
        for sub in subcadenas_con_resultados:
            _ = busqueda_lineal_por_nombre(lista_productos, sub)
    tiempo_sub_ex = time.perf_counter() - inicio

    inicio = time.perf_counter()
    for _ in range(1000):
        for sub in subcadenas_sin_resultados:
            _ = busqueda_lineal_por_nombre(lista_productos, sub)
    tiempo_sub_no_ex = time.perf_counter() - inicio

    print(f"Subcadenas con resultados probadas: {subcadenas_con_resultados}")
    print(f"Tiempo total (1000 iteraciones x 10 subcadenas válidas): {tiempo_sub_ex:.6f} segundos")
    print(f"Subcadenas sin resultados probadas: {subcadenas_sin_resultados}")
    print(f"Tiempo total (1000 iteraciones x 10 subcadenas vacías): {tiempo_sub_no_ex:.6f} segundos\n")

    print("="*85)
    print("¡Todas las partes del proyecto se han ejecutado con éxito!")
    print("="*85)

if __name__ == "__main__":
    main()