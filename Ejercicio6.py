class Producto:
    def __init__(self, nombre, precio, año, marca):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        self.marca = marca

    def __str__(self):
        return f"{self.nombre} ({self.marca}), Año: {self.año}, Precio: ${self.precio}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el catálogo.")
        else:
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if productos_filtrados:
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No se encontraron productos del año {año}.")

    def buscar_por_nombre(self, nombre):
        productos_encontrados = [producto for producto in self.productos if nombre.lower() in producto.nombre.lower()]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

# Crear objetos de tipo Producto
producto1 = Producto("Cartera", 165, 2024, "Cartier")
producto2 = Producto("Saco", 250, 2023, "Zara")
producto3 = Producto("Pantalon", 80, 2022, "HyM")

# Crear un objeto de tipo Catalogo y agregar los productos
catalogo = Catalogo()
catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

# Mostrar todos los productos del catálogo
print("Todos los productos del catálogo:")
catalogo.mostrar_productos()

# Filtrar productos por año
print("\nProductos del año 2022:")
catalogo.filtrar_por_año(2022)

# Buscar productos por nombre
print("\nBuscar productos con el nombre 'Saco':")
catalogo.buscar_por_nombre("Saco")

# Ejemplo adicional: Buscar productos por marca
print("\nBuscar productos con la marca 'Pantalon':")
catalogo.buscar_por_nombre("Pantalon")
