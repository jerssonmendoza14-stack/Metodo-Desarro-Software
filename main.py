# from backend.producto import listarProductos

# productos = listarProductos()

# print(productos)

from backend.producto import consultarProducto

producto = consultarProducto("10")

print(producto)