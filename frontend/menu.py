
from tabulate import tabulate
from backend.producto import listarProductos, consultarProducto


def mostrarProductos():
    productos = listarProductos()

    if not productos:
        print("No hay productos disponibles.")
        return

    headers = ["ID", "Nombre", "Precio", "Cantidad"]

    print("\n________________ LISTA DE PRODUCTOS ________________")
    print(tabulate(productos, headers=headers, tablefmt="grid"))


def consultarProductoPorID():
    id_producto = input("Ingrese el ID del producto que desea consultar: ").strip()

    producto = consultarProducto(id_producto)

    if producto is None:
        print("No se encontró ningún producto con ese ID.")
        return

    headers = ["ID", "Nombre", "Precio", "Cantidad"]

    print("\n________________ PRODUCTO CONSULTADO ________________")
    print(tabulate([producto], headers=headers, tablefmt="grid"))


def mostrarProducto():
    while True:
        print("\n________________ MENU DE PRODUCTO ________________")
        print("1. Listar productos")
        print("2. Consultar producto por ID")
        print("3. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrarProductos()

        elif opcion == "2":
            consultarProductoPorID()

        elif opcion == "3":
            print("Saliendo del menú de productos.")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
