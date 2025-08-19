#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print("Hola Mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo
# usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe
# imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas
# print(f…) para realizar la impresión por pantalla. 

nombre= input (" Ingrese su nombre ")
print (f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia
# e imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”,
# el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 

nombre= input ("ingrese su nombre ")
apellido= input ("ingrese su apellido ")
edad= input ("ingrese su edad ")
residencia= input ("ingrese lugar de residencia ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} ")

#4) Crear un programa que pida al usuario el radio de un círculo 
# e imprima por pantalla su área y su perímetro. 

radio= float (input("ingrese el radio del circulo "))
area= 3.14 * radio * radio
perimetro= 2 * 3.14 * radio
print (f"el area es {area} y el perimetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima
#  por pantalla a cuántas horas equivale.  

segundos= int (input(" ingrese los segundos"))
horas= segundos//3600
print ("los segundos ingresados equivalen a ", horas , "horas")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y
# muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1= int(input ("ingrese un numero distinto a 0"))
num2= int(input ("ingrese otro, tambien distinto a 0"))

sumado= num1+num2
restado= num1-num2
multiplicado= num1*num2
dividido= num1//num2
print ("El resultado de suma es ",sumado)
print ("el resultado en resta es ",restado)
print ("El resultado en multiplicación es ",multiplicado)
print ("El resultado en división es ",dividido)

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla
#  su índice de masa corporal.

altura= float(input("ingrese su altura"))
peso= int (input("ingrese su peso"))

masa= (altura**2) /peso
print (f"su masa corporal es de {masa:.2f}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima
#  por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#  𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠   + 32

celsius = int(input("ingrese la temperatura en grados celsius"))
fahrenheit = celsius*(9/5)+32
print (f"El quivalente en fahrenheit es {fahrenheit}")

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla
# el promedio de dichos números. 

num1 = float(input("ingrese un numero"))
num2 = float(input("ingrese otro numero"))
num3 = float(input("ingrese un numero mas"))

promedio = (num1+num2+num3) /3
print (f"el promedio de los numeros ingresados es {promedio:.2}")