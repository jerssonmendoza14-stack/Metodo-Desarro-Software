from tabulate import tabulate
from backend.producto import listarProductos

def mostrarProductos():
    productos = listarProductos()


    if not productos:
        print("No hay productos disponibles.")
        return

    headers = ["ID", "Nombre", "Precio", "Cantidad"]

    print("________________ LISTA DE PRODUCTOS ________________")
    print(tabulate(productos, headers=headers, tablefmt="grid"))


def mostrarProducto():
    while True:
        print("________________ MENU DE PRODUCTO ________________")
        print("1. Listar productos")
        print("2. Salir")   

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrarProductos() 
        elif opcion == "2":
            print("Saliendo del menú de productos.")
            break                   
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")  