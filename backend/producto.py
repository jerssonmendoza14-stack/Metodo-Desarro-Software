from backend.hoja_producto import obtenerHojaProductos
from backend.excel import guardarHoja

hoja = obtenerHojaProductos()

def listarProductos():
    filas = []

    refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)

    for refFila in refFilas:
        valores = []

        for celda in refFila:
            valores.append(celda.value)

        filas.append(valores)

    return filas

def consultarProducto(id_producto, soloValores=True):
    refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
    refFilasEnum = enumerate(refFilas)

    for idx, refFila in refFilasEnum:
        if refFila[0].value == id_producto:
            if soloValores:
                valores = []
                valores.append(idx)

                for celda in refFila:
                    valores.append(celda.value)

                return valores
            else:
                return refFila
    else:
        return None

def crearProducto(ID, nombre, precio, cantidad):
    if consultarProducto(ID) != None:
        return False

    producto = [ID, nombre, precio, cantidad]
    
    hoja.append(producto)
    
    guardarHoja(hoja)
    
    return True

def eliminarProducto(ID):
    producto = consultarProducto(ID)

    if producto == None:
        return False

    hoja.delete_rows(producto[0] + 2)

    guardarHoja(hoja)

    return True

def actualizarProducto(ID, nombre, precio, cantidad):
    nuevosProductos = [ID, nombre, precio, cantidad]

    refFila = consultarProducto(ID,False)

    if refFila == None:
        return False

    for celda, nuevoValor in zip(refFila, nuevosProductos):
        celda.value = nuevoValor

    guardarHoja(hoja)
    return True
