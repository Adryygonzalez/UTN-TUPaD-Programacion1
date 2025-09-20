#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for i in range(0,101,+1):
    print (i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene. 

cantidad=0
numero=int(input("ingrese un numero 0 para cortar: "))
while numero!=0:
   numero=int(input("ingrese un numero 0 para cortar: "))
   cantidad= cantidad+1
print("la cantidad de digitos que contiene es : ",cantidad) 

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.

numero_inicio=int(input("ingrese un valor de inicio: "))
numero_fin=int(input("ingrese un valor de fin: "))
suma=0
for i in range(numero_inicio +1, numero_fin):
    suma= suma+i
print(f"la suma de los valores entre",numero_inicio, "y",numero_fin, "excluyendo ambos valores es: ",suma)


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.
num=int
suma=0
while num!=0:
    num=int(input("ingrese numeros enteros  e ingrese 0 para finalizar: "))
    suma= suma+num
print("el total es: ",suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

print("adivina el numero que esta entre 0 y 9")
import random
numero_secreto = (random.randint(0, 9))
intentos=0
while intentos!=numero_secreto:
    print (input("ingrese un intento: "))
    intentos=intentos+1
    if intentos==numero_secreto:
        break
print (f"Felicidades, has adivinado el numero secreto y se necesito",intentos,"intentos para adivinarlo")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100,0,-2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

suma=0
numero_fin=int(input("ingrese un numero positivo de fin: "))
for i in range(0,numero_fin):
    suma= suma+i
print("La suma de los numeros entre 0 y",numero_fin,"es: ",suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares=0
impares=0
negativos=0
positivos=0

for i in range(0,101):
    numero=int(input("ingrese un numero: "))
    if numero >= 0:
        positivos= positivos+1
    else:
        numero<0
        negativos=negativos+1
    if numero % 2==0:
        pares=pares+1
    else:
        impares=impares+1
print("El total de numeros pares son: ",pares,)
print("El total de numeros impares son: ",impares,)
print("El total de numeros positivos son: ",positivos,)
print("El total de numeros negativos son: ",negativos,)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

suma=0
for i in range(0,5,):
   numeros_enteros=int(input("ingrese un numero entero: "))
   suma=suma+numeros_enteros

print("la media es: ",suma/5)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero=(input("ingrese un numero: "))
invertido=""
for digito in (numero):
    invertido=digito+invertido
print(invertido)