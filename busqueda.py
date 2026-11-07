# busqueda.py

def busqueda_binaria(arr, id_buscado):
    """
    Busca un producto por su id usando Búsqueda Binaria.
    El arreglo DEBE estar previamente ordenado por id.
    Retorna el objeto Producto si lo encuentra, o None si no existe.
    """
    izquierda = 0
    derecha = len(arr) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio].id == id_buscado:
            return arr[medio]
        elif arr[medio].id < id_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
            
    return None


def busqueda_lineal_por_nombre(arr, subcadena):
    """
    Busca productos cuyo nombre contenga la subcadena especificada (case-insensitive).
    Retorna una lista con todos los productos coincidentes.
    """
    subcadena_lower = subcadena.lower()
    resultados = []
    
    for producto in arr:
        if subcadena_lower in producto.nombre.lower():
            resultados.append(producto)
            
    return resultados