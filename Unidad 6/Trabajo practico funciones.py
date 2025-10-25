#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla 
#el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    return("Hola Mundo!")

print(imprimir_hola_mundo())

#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return(f"Hola {nombre}!")

nombre=str(input("ingrese nu nombre: "))
print(saludar_usuario(nombre))

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima:
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre,apellido,edad,residencia):
    return(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre=str(input("ingrese nu nombre: "))
apellido=str(input("ingrese su apellido: "))
edad=int(input("ingrese su edad: "))
residencia=str(input("ingrese el lugar que reside: "))

print(informacion_personal(nombre,apellido,edad,residencia))


#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return 3.14 * radio * radio
def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio=float(input("ingrese el radio: "))

print(f"el area del circulo es: {calcular_area_circulo(radio):.2f} y su perimetro es: {calcular_perimetro_circulo(radio):.2f}")


#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos//3600

segundos=int(input("ingrese los segundos: "))

print(f"los segundos ingresados, equivalen a {segundos_a_horas(segundos)} horas")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar 
#de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for x in range(1,11):
        print(f"{numero} x {x} = {numero*x}")

numero=int(input("ingrese el numero que desea saber su tabla de multiplicar: "))

tabla_multiplicar (numero)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de 
# sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a,b):
    return a+b,a-b,a*b,a//b

num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))

resultado=operaciones_basicas(num1,num2)
print("el resultado de las operaciones sumar,restar, multiplicar y dividir son: ", resultado)

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso,altura):
    return (altura**2) /peso

peso=float(input("ingrese su peso en kilogramos"))
altura=float(input("ingrese su altura en metros"))

print(f"el indice de masa corporal es: {calcular_imc(peso,altura):.2f}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius* 9/5)+32

temp_celsius=float(input("ingrese la temperatura en grados celsius: "))

print (f"Los grados celsius ingresados son equivalentes a {celsius_a_fahrenheit(temp_celsius)} en fahrenheit")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. 
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a,b,c):
    promedio= float(a+b+c)/3
    return promedio

num1=float(input("ingrese el primer numero: "))
num2=float(input("ingrese el segundo numero: "))
num3=float(input("ingrese el tercer numero: "))

print(f"el promedio de los numeros ingresados es: {calcular_promedio(num1,num2,num3):.2f}")