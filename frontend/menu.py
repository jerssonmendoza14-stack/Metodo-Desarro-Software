

from tabulate import tabulate
from backend.producto import (
    listarProductos,
    consultarProducto,
    crearProducto,
    actualizarProducto,
    eliminarProducto
)


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


# NUEVA FUNCION: REGISTRAR PRODUCTO
def registrarProducto():
    print("\n________________ REGISTRAR PRODUCTO ________________")

    ID = input("Ingrese el ID del producto: ").strip()
    nombre = input("Ingrese el nombre del producto: ").strip()

    if not ID or not nombre:
        print("El ID y el nombre son obligatorios.")
        return

    try:
        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))

        if precio < 0 or cantidad < 0:
            print("El precio y la cantidad no pueden ser negativos.")
            return

    except ValueError:
        print("Ingrese valores numéricos válidos.")
        return

    resultado = crearProducto(ID, nombre, precio, cantidad)

    if resultado:
        print("Producto registrado correctamente.")
    else:
        print("Ya existe un producto con ese ID.")


# NUEVA FUNCION: ACTUALIZAR PRODUCTO
def actualizarProductoPorID():
    print("\n________________ ACTUALIZAR PRODUCTO ________________")

    ID = input("Ingrese el ID del producto que desea actualizar: ").strip()

    producto = consultarProducto(ID)

    if producto is None:
        print("No se encontró ningún producto con ese ID.")
        return

    print("\nProducto encontrado:")
    print(tabulate([producto[1:]], headers=["ID", "Nombre", "Precio", "Cantidad"], tablefmt="grid"))

    nombre = input("Ingrese el nuevo nombre: ").strip()

    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    try:
        precio = float(input("Ingrese el nuevo precio: "))
        cantidad = int(input("Ingrese la nueva cantidad: "))

        if precio < 0 or cantidad < 0:
            print("El precio y la cantidad no pueden ser negativos.")
            return

    except ValueError:
        print("Ingrese valores numéricos válidos.")
        return

    resultado = actualizarProducto(ID, nombre, precio, cantidad)

    if resultado:
        print("Producto actualizado correctamente.")
    else:
        print("No fue posible actualizar el producto.")


# NUEVA FUNCION: ELIMINAR PRODUCTO
def eliminarProductoPorID():
    print("\n________________ ELIMINAR PRODUCTO ________________")

    ID = input("Ingrese el ID del producto que desea eliminar: ").strip()

    producto = consultarProducto(ID)

    if producto is None:
        print("No se encontró ningún producto con ese ID.")
        return

    print("\nProducto seleccionado:")
    print(tabulate([producto[1:]], headers=["ID", "Nombre", "Precio", "Cantidad"], tablefmt="grid"))

    confirmacion = input("¿Está seguro de eliminarlo? (S/N): ").strip().upper()

    if confirmacion == "S":
        resultado = eliminarProducto(ID)

        if resultado:
            print("Producto eliminado correctamente.")
        else:
            print("No fue posible eliminar el producto.")
    else:
        print("Eliminación cancelada.")


# MENU PRINCIPAL
def mostrarProducto():
    while True:
        print("\n________________ MENU DE PRODUCTO ________________")
        print("1. Listar productos")
        print("2. Consultar producto por ID")
        print("3. Registrar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrarProductos()

        elif opcion == "2":
            consultarProductoPorID()

        elif opcion == "3":
            registrarProducto()

        elif opcion == "4":
            actualizarProductoPorID()

        elif opcion == "5":
            eliminarProductoPorID()

        elif opcion == "6":
            print("Saliendo del menú de productos.")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
