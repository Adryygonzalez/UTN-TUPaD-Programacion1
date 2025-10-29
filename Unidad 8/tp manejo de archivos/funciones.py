def mostrar_productos():
    with open("productos.txt", "r") as lista_productos:
        for articulo in lista_productos:
            nombre,precio,cantidad=articulo.strip().split(",")
            print(f"Producto: {nombre} | Precio: $ {precio} Stock: {cantidad} Unidades")
def añadir_producto():
    nombre=input("Ingrese el nuevo producto: ")
    precio=input("Ingrese el precio: ")
    cantidad=input("Ingrese la cantidad en stock : ")
    with open("productos.txt","a") as agregar:
        agregar.write(f"{nombre},{precio},{cantidad}\n")
    print("producto añadido exitosamente")