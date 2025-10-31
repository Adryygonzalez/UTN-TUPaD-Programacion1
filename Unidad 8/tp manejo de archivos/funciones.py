import os

def mostrar_listas(productos):
     for producto in productos:
        print(f"Nombre: {producto["Nombre"]} | Precio: {producto["Precio"]} | Cantidad: {producto["Cantidad"]}")


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

def cargar_listas():
    productos=[]
    if not os.path.exists("productos.txt"):
        print("No existe productos.txt")
        return []
    with open("productos.txt","r") as lista_productos:
        for articulo in lista_productos:
            nombre,precio,cantidad=articulo.strip().split(",")
            producto={
                "Nombre":nombre,
                "Precio":precio,
                "Cantidad":cantidad
            }
            productos.append(producto)
        mostrar_listas(productos)
        return productos

def buscar_producto(lista):
    if len(lista)==0:
        print("no hay elementos en la lista, debe cargarlos primero")
        return
    buscar= input("Ingrese el nombre del producto que desea buscar:\n")

    encontrado=False
    
    for producto in lista:
        if producto["Nombre"].lower() == buscar.lower():
            print("Producto encontrado, los datos son: ")
            print(f"Nombre: {producto["Nombre"]} | Precio: {producto["Precio"]} | Cantidad: {producto["Cantidad"]}")
            encontrado=True
            break
    if not encontrado:
        print("Producto no existente")

def sobreescribir(productos):
    if len(productos)==0:
        print("no hay elementos en la lista, debe cargarlos primero")
        return
    with open("producto.txt","w") as archivo:
        for producto in productos:
            archivo.write(f"{producto["Nombre"]},{producto["Precio"]},{producto["Cantidad"]}\n")



        

