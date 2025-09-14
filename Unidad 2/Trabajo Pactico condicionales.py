#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#  deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 
edad= int (input("Ingrese su edad"))
if (edad)>=18 and (edad)>0:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario 
# deberá mostrar el mensaje “Desaprobado”. 
nota= float (input("Ingrese su nota"))
if (nota)>=0 and (nota)<=10:
    if (nota)>=6:
        print("Aprobado")
    else:
        print("desaprobado")    
else:
    print("ha ingresado una nota invalida")
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número
#par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario,
#imprimir por pantalla "Por favor, ingrese un número par". 
#Nota: investigar el uso del operador de módulo (%) en Python para evaluar 
#si un número es par o impar. 
numero= int(input("Ingrese un numero par"))
if (numero % 2 == 0):
    print ("ha ingresado un numero par")
else:
    print("por favor,ingrese un numero par")
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.
edad= int(input("Ingrese su edad"))
if (edad <12) and (edad)>0:
    print ("eres niño")
elif(edad >=12) & (edad<18):
    print("Eres Adolescente")
elif (edad >=18) & (edad <30):
    print(" Eres Adulto/a Joven")
else:
    print("Eres Adulto Mayor")
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string. 
contraseña= str(input("Ingrese su contraseña"))
if len(contraseña)>=8 and len(contraseña)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña entre 8 y 14 caracteres")
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
# Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
#mediana es mayor que la moda. 
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
#la mediana es menor que la moda. 
#● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
#Definir la lista numeros_aleatorios de la siguiente forma: 
#import random 
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
from statistics import mode, median, mean 
import random 
numeros_aleatorios=[random.randint(1, 100) for i in range(50)]

moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)

if (media > mediana) and (mediana > moda):
    print("sesgo positivo")
elif (media < mediana) and (mediana < moda):
    print("sesgo Negativo")
elif (media == mediana) and (mediana==moda):
    print("Sin sesgo")
else:
    print("los valores no coinciden")
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase= str(input("ingrese su frase aqui: "))

vocales= "aeiou"
exclamacion="!"
if frase[-1].lower() in vocales:
    print (frase+exclamacion)
else:
    print (frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado 
#por pantalla.#Nota: investigue uso de las funciones upper(), lower() y title() de Python para 
#convertir entre mayúsculas y minúsculas.
nombre=str (input("escriba su nombre: "))
opcion= int(input("elija una opcion: "))
if opcion==1:
    print (nombre.upper())
elif opcion==2:
    print (nombre.title())
elif opcion==3:
    print (nombre.lower())
else:
    print("opcion invalida")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes
# categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud=int(input("ingrese la magnitud del terremoto: "))
if (magnitud) <3:
    print("muy leve (imperceptible)")
elif (magnitud)>=3 and (magnitud)<4:
    print("leve (ligeramente perceptible)")
elif (magnitud)>=4 and (magnitud)<5:
    print("moderado (sentido por personas,pero no causa daños)")
elif (magnitud)>=5 and (magnitud)<6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif (magnitud)>=6 and (magnitud)<7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    (magnitud)>=7
    print("Extremo (puede causar graves daños a escala)")

#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
#El programa deberá utilizar esa información para imprimir por pantalla si el usuario 
#se encuentra en otoño, invierno, primavera o verano.

hemisferio= str(input("norte/sur: "))
dia=int(input("ingrese el dia: "))
mes=str(input("ingrese el mes: "))
if hemisferio=="norte":
    if(dia>=21 and dia<=31 and mes=="diciembre") or mes =="enero"or mes =="febrero"or (dia>=1 and dia <=20 and mes =="marzo"):
        print("estas en invierno") 
elif hemisferio=="sur":
    if(dia>=21 and dia<=31 and mes=="diciembre") or mes =="enero"or mes =="febrero"or (dia>=1 and dia <=20 and mes =="marzo"):
        print("estas en verano")
if hemisferio=="norte":
    if(dia>=21 and dia<=31 and mes=="marzo") or mes =="abril"or mes =="mayo"or (dia>=1 and dia <=20 and mes =="junio"):
        print("estas en primavera")
elif hemisferio=="sur":
    if(dia>=21 and dia<=31 and mes=="marzo") or mes =="abril"or mes =="mayo"or (dia>=1 and dia <=20 and mes =="junio"):
        print("estas en otoño")
if hemisferio=="norte":
    if(dia>=21 and dia<=31 and mes=="junio") or mes =="julio"or mes =="agosto"or (dia>=1 and dia <=20 and mes =="septiembre"):
        print("estas en verano")
elif hemisferio=="sur":
    if(dia>=21 and dia<=31 and mes=="junio") or mes =="julio"or mes =="agosto"or (dia>=1 and dia <=20 and mes =="septiembre"):
        print("estas en invierno")
if hemisferio=="norte":
    if(dia>=21 and dia<=31 and mes=="septiembre") or mes =="octubre"or mes =="noviembre"or (dia>=1 and dia <=20 and mes =="diciembre"):
        print("estas en otoño")
elif hemisferio=="sur":
    if(dia>=21 and dia<=31 and mes=="septiembre") or mes =="octubre"or mes =="noviembre"or (dia>=1 and dia <=20 and mes =="diciembre"):
        print("estas en primavera")