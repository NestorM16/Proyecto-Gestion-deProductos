# gestion_productos.py

import random

class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float,
                 categoria: str, stock: int, calificacionPromedio: float):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.calificacionPromedio = calificacionPromedio

    def __str__(self):
        return (
            f"ID: {self.id:2} | "
            f"Nombre: {self.nombre:<30} | "
            f"Categoría: {self.categoria:<12} | "
            f"Precio: ${self.precio:>8.2f} | "
            f"Stock: {self.stock:>3} | "
            f"Calificación: {self.calificacionPromedio} ⭐"
        )


def generar_productos():
    categorias_disponibles = ["Electrónica", "Ropa", "Libros", "Hogar"]

    nombres_por_categoria = {
        "Electrónica": [
            "Smartphone",
            "Auriculares Bluetooth",
            "Laptop",
            "Smartwatch",
            "Televisor 4K",
            "Cámara Digital",
            "Altavoz Inteligente"
        ],
        "Ropa": [
            "Camisa Casual",
            "Pantalón Jean",
            "Chaqueta Impermeable",
            "Vestido de Verano",
            "Zapatillas Deportivas",
            "Suéter de Lana"
        ],
        "Libros": [
            "Novela de Ciencia Ficción",
            "Libro de Python Avanzado",
            "Biografía Histórica",
            "Manual de Cocina",
            "Ensayo Filosófico"
        ],
        "Hogar": [
            "Cafetera Eléctrica",
            "Lámpara de Escritorio",
            "Juego de Sábanas",
            "Almohada Viscoelástica",
            "Organizador de Cocina",
            "Licuadora"
        ]
    }

    lista_productos = []

    for i in range(1, 51):

        categoria = random.choice(categorias_disponibles)

        base_nombre = random.choice(
            nombres_por_categoria[categoria]
        )

        nombre = f"{base_nombre} v{random.randint(1, 9)}"

        if categoria == "Electrónica":
            precio = round(random.uniform(49.99, 1200.00), 2)
            stock = random.randint(5, 40)

        elif categoria == "Ropa":
            precio = round(random.uniform(14.99, 89.99), 2)
            stock = random.randint(10, 100)

        elif categoria == "Libros":
            precio = round(random.uniform(9.99, 45.99), 2)
            stock = random.randint(15, 60)

        else:  # Hogar
            precio = round(random.uniform(19.99, 250.00), 2)
            stock = random.randint(8, 50)

        calificacionPromedio = round(
            random.uniform(1.0, 5.0), 1
        )

        producto = Producto(
            i,
            nombre,
            precio,
            categoria,
            stock,
            calificacionPromedio
        )

        lista_productos.append(producto)

    return lista_productos


# Programa principal
if __name__ == "__main__":

    productos = generar_productos()

    print("\nCATÁLOGO DE PRODUCTOS")
    print("=" * 120)

    for producto in productos:
        print(producto)

    print("=" * 120)
    print(f"Total de productos generados: {len(productos)}")