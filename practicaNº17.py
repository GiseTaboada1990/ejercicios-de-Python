"""
Ejercicio 17:
a) Definir una función que permita el ingreso de números por teclado hasta ingresar el 0,
y retorne esa lista.
b) Definir una función que reciba como parámetro una lista de números y retorne como
resultado el promedio.
c) Definir una función que reciba como parámetro una lista de números y retorne como
resultado la suma de los números.
d) Definir una función que reciba como parámetro una lista de números y retorne el
número más grande de la lista (máximo).
e) Definir una función que reciba como parámetro una lista de números y retorne el
número más pequeño de la lista (mínimo).
f) Definir una función denominada porcentaje, que tenga 2 parámetros formales, que
representan el total y un valor y retorna el porcentaje de ese valor respecto del total.

Utilizar las funciones definidas anteriormente para construir un programa que permita elegir
una opción del siguiente menú, el cuál debe mostrarse permanentemente hasta que se
elija la opción 7:
1. Ver el promedio de los números
2. Ver la suma de los números
3. Ver la cantidad de números
4. Ver el número máximo
5. Ver el número mínimo
6. Calcular porcentaje
7. Salir
"""
def ingresoDenumeros():
    num=int(input("(Finaliza cuando ingresa 0) Ingrese un número: "))
    lista=[]
    while num != 0:
        lista.append(num)
        num=int(input("(Finaliza cuando ingresa 0) Ingrese un número: "))
    return lista

lista_numeros= ingresoDenumeros()

def promedio(num):
    if len(num)>0:
        suma= sum(num)
        prom= suma/ len(num)
        return ("El promedio es " + str(prom))
    else:
        print("No hay numeros para promediar")
def suma(num):
    if len(num)>0:
        sumaDelaLista= sum(num)
        return ("La sumatoria de los números de la lista es: "+ str(sumaDelaLista))
    else:
        print("No hay numeros para sumar")

def elMayor(num):
    if len(num)>0:
        mayor= num[0]
        for n in num:
            if n > mayor:
                mayor= n
        return "El mayor es " + str(mayor)
    else:
        print("La lista de numeros esta vacía")

def elMenor(num):
    if len(num)> 0:
        menor= num[0]
        for n in num:
            if n < menor:
             menor = n
        return "El menor es " + str(menor)
    else:
        print("La lista de numeros esta vacía")

def porcentaje(num,val):
    if num != 0:
        porcent= (val*100)/num
        return "El valor corresponde al " + str(porcent)+ "% de " + str(num)
    else:
        print("Ingrese numeros distintos de 0")
def opciones():
    print("1. Ver el promedio de los números")
    print("2. Ver la suma de los números")
    print("3. Ver la cantidad de números")
    print("4. Ver el número máximo")
    print("5. Ver el número mínimo")
    print("6. Calcular porcentaje")
    print("7. Salir")

def menu():
    opciones()
    opcion= int(input("Ingrese una opción del menú: "))
    while opcion != 7:
        if opcion == 1 :
            print(promedio(lista_numeros))
        elif opcion == 2:
            print(suma(lista_numeros))
        elif opcion == 3:
            print("La cantidad de números es: " + str(len(lista_numeros)))
        elif opcion == 4:
            print(elMayor(lista_numeros))
        elif opcion == 5:
            print(elMenor(lista_numeros))
        elif opcion == 6:
            total= int(input("Ingrese el total: "))
            valor= int(input("Ingrese el valor que quiere calcular: "))
            print(porcentaje(total, valor))
        else: 
            print("La opcion ingresada no corresponde al menú")
        opciones()
        opcion= int(input("Ingrese una opción del menú: "))

menu()
    
#Ejercicio 1: Escribir un programa que muestre la tabla de multiplicar de un número
#introducido por teclado por el usuario.
    
def tablaMultiplicar():
    numero= int(input("Ingrese un numero: "))
    
    for n in range(1,11):
    
        print(str(numero) + " x " + str(n) + " = " + str(n * numero))

tablaMultiplicar()

def sumatoria():
    m= int(input("Ingrese un numero: "))
    suma=0
    for n in range(m + 1):
        suma = suma + n
    print("La sumatoria de 0 a " + str(m) + " es " + str(suma))

sumatoria()
#Ejercicio 3: Escribir un programa que muestre la tabla de los códigos ASCII. Los códigos
#ASCII van de 0 a 255

def codASCII():
    for n in range(256):
        print("El codigo ASCII en la posicion " + str(n)+ " es:  " + str(chr(n)))
codASCII()

def letrasEnASCII():
    print("El programa finaliza cuando ingresa la palabra 'fin'")
    letra= input("Ingrese una letra: ")
    if len(letra) < 2:
        while letra.upper() != "fin".upper():
            print("La letra "+ letra.upper() +" se encuentra en la posicion " + str(ord(letra)) + " del codigo ASCII")
            letra = input("Ingrese una letra: ")
    else:
        print("Solo se puede ingresar una letra a la vez")
        
letrasEnASCII()