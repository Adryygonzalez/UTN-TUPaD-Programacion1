#1) Dado el diccionario precios_frutas 
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
#1450} 
#Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"]= 1500
precios_frutas["Pera"]= 2300

print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"]= 1500
precios_frutas["Pera"]= 2300

#Precios actualizados
precios_frutas['Banana']=1330
precios_frutas['Manzana']= 1700
precios_frutas['Melón']= 2800

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios.

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"]= 1500
precios_frutas["Pera"]= 2300

#Precios actualizados
precios_frutas['Banana']=1330
precios_frutas['Manzana']= 1700
precios_frutas['Melón']= 2800
#Lista de keys
print(precios_frutas.keys())

#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos_telefonicos=dict()

for contacto in range(0,6):
    contacto=input("Ingrese el contacto: ")
    for numero in range(0,1):
        numero=input("Ingrese el numero: ")
        contactos_telefonicos[contacto]=numero
while True:
    consulta=input("Ingrese el nombre del asociado: ")
    if consulta not in contactos_telefonicos:
        print("El nombre ingresado no existe, intente de nuevo")
        continue
    break
print(contactos_telefonicos[consulta])

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

texto=str(input("Ingrese la frase: "))
frase=texto.split()
palabras_unicas=set(frase)
print(palabras_unicas)

cantidad_palabras={}
for palabra in frase:
    if palabra in cantidad_palabras:
        cantidad_palabras[palabra]+=1
    else:
        cantidad_palabras[palabra]=1
print(cantidad_palabras)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos_y_notas={}

for i in range(3):
    nombre= input("Ingrese el nombre del alumno: ")
    nota1=float(input(f"Ingrese la primer nota de {nombre}: "))
    nota2=float(input(f"Ingrese la segunda nota de {nombre}: "))
    nota3=float(input(f"Ingrese la tercer nota de {nombre}: "))
    tuplas=(nota1,nota2,nota3)
    alumnos_y_notas[nombre]=(tuplas)

for alumno,notas in alumnos_y_notas.items():
    promedio = (notas[0] + notas[1] + notas[2]) / 3
    print(f"el alumno/a {alumno}, tiene un promedio de: {promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {6,2,3,5,9,10}
parcial_2 = {2,5,6,4,8,10}

aprobaron_ambos = parcial_1 & parcial_2
aprobaron_solo_uno = parcial_1 ^ parcial_2
aprobaron_al_menos_uno = parcial_1 | parcial_2

print(f"Los estudiantes que aprobaron ambos parciales son : {aprobaron_ambos}")
print(f"Los que aprobaron solo un parcial son: {aprobaron_solo_uno}")
print(f"Y los que aprobaron al menos uno son: {aprobaron_al_menos_uno}")


#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

productos_y_stocks={'tomate': 180, 'lechuga': 120, 'morrón': 560, 'ajo': 100}

consulta_producto=input("ingrese el producto: ").strip().lower()


if consulta_producto in productos_y_stocks:
    
    print(f"Hay {productos_y_stocks[consulta_producto]} unidades en stock")
    cantidad=int(input("ingrese la cantidad: "))
    productos_y_stocks[consulta_producto]+=cantidad
    print(f"se actualizo el stock de {consulta_producto} en {productos_y_stocks[consulta_producto]} unidades")
else:
    print(f"Ha ingresado un producto nuevo")
    cantidad_stock=int(input("Ingrese su stock"))
    productos_y_stocks[consulta_producto]= cantidad_stock
    print(f"se ingreso nuevo producto {consulta_producto} con {productos_y_stocks[consulta_producto]} unidades")

print("----------------------------------------------")

print("Cantidad actual de productos con su stock")

for producto,cantidad in productos_y_stocks.items():
    print(f"{producto} : {cantidad} unidades")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
#Permití consultar qué actividad hay en cierto día y hora. 

agenda={
    
    ("Lunes","9:30"):"Reunion equipo de trabajo",
    ("Martes","18:30"):"estudiar para el parcial",
    ("Miercoles","20:00"):"Reunion en la iglesia",
    ("Jueves","19:30"):"No hay actividad",
    ("Viernes","21:15"):"No hay actividad"
}




while True:
    
    consulta_dia=input("Ingrese el dia de la actividad: ").capitalize()
    consulta_hora=input("Ingrese el horario: ")
    horarios=(consulta_dia,consulta_hora)
    if horarios not in agenda:
        print("los datos ingresados no existen, intente nuevamente")
        continue
    else:
        print(f"El dia {consulta_dia} hay {agenda[horarios]}")
    break
#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores. 

capitales_paises={}
paises_capitales={
    "Argentina":"Buenos Aires",
    "Brasil":"Rio de Janeiro",
    "Inglaterra": "Londres",
    "Portugal":"Lisboa"
}
print("--Paises con capìtales--")
print(paises_capitales)

print("--Capitales con Paises--")
for p,c in paises_capitales.items():
    capitales_paises[c]=p
print(capitales_paises)
