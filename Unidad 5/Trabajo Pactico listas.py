#1)Crear una lista con las notas de 10 estudiantes.
#•Mostrar la lista completa.
#•Calcular y mostrar el promedio.
#•Indicar la nota más alta y la más baja.

lista_notas=[4,9,8,10,7,9,6,7,8,10]
for notas in lista_notas:
    print(notas,end=" ")
suma=0
for notas in lista_notas:
    suma=suma+notas
promedio=suma/len(lista_notas)
print(f"\nEl promedio es {promedio}")
minimo=min(lista_notas)
maximo=max(lista_notas)
print(f"La nota minima es {minimo} y la maxima es {maximo}")

#2) Pedir al usuario que cargue 5 productos en una lista.
#•Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#•Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos=[]
for p in range(5):
    producto=input(f"ingrese el producto a la lista {p+1}: ")
    productos.append(producto)
print(productos)
productos_ordenados= sorted(productos)
print(productos_ordenados)

producto_eliminado=input("¿Que producto desea eliminar de la lista?: ")

if producto_eliminado in productos:
   productos.remove(producto_eliminado)
else:
    print("El producto ingresado no se encuentra en la lista")
print(productos)

#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#•Crear una lista con los pares y otra con los impares.
#•Mostrar cuántos números tiene cada lista.

import random
numeros=[]

for i in range(15):
    num= random.randint(1,100)
    numeros.append(num)
pares=[]
impares=[]

for num in numeros:
    if num % 2==0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista de numeros:",numeros)
print("Numeros pares:",pares)
print("Numeros impares:",impares)
print(f"La cantidad de pares son: ",len(pares), "y la cantidad de impares son: ",len(impares))

#4)Dada una lista con valores repetidos:
#•Crear una nueva lista sin elementos repetidos.
#•Mostrar el resultado.

lista_original=[1,3,5,3,7,1,9,5,3]
sin_repeticiones=[]
for l in lista_original:
    if l not in sin_repeticiones:
        sin_repeticiones.append(l)

print(lista_original)
print(sin_repeticiones)

#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#•Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#•Mostrar la lista final actualizada.

estudiantes=["Soledad","Mariel","Julieta","Keila","Adrian","Joaquin","Maximiliano","Dante"]
print(estudiantes)

print("¿Desea eliminar o agregar un estudiante?")
opcion=input("Digite A para agregar o E para eliminar: \n").upper()

if opcion== "A":
    nuevo=(input("ingrese el nombre del estudiante que desea agregar: \n")).title()
    if nuevo in estudiantes:
        print("El estudiante ingresado ya se encuentra en la lista")
    else:
        estudiantes.append(nuevo)
elif opcion== "E":
    eliminado=(input("ingrese el nombre estudiante que desea eliminar: \n")).title()
    if eliminado in estudiantes:
        estudiantes.remove(eliminado)
    else:
        print("El estudiante ingresado no se encuentra en la lista")
else:
    print("opcion incorrecta")
print(estudiantes)
