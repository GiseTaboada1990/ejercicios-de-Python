""""
Ejercicio 6:
Nos contratan para realizar un sistema para una editorial. Se recibe un texto y se desea obtener la
siguiente información:
- La longitud total del texto.
- La cantidad de palabras componen el texto.
- La cantidad de oraciones que componen el texto.
- La cantidad de palabras que comienzan con vocal o con consonante, dependiendo del
valor ingresado por el usuario.
- Buscar una palabra ingresada por el usuario y retornar la cantidad de veces que se
encuentra en el texto.
- La cantidad de palabras que comienzan con mayúscula.
- La cantidad de caracteres que son números.
- La cantidad de palabras que comienzan con vocal y la cantidad de palabras que
comienzan con consonante.
- Imprimir todas las palabras que terminan en infinitivo (terminadas en ar er o ir).

def redaccion():
    text= input("Ingrese el texto: ")
    return text
def longitud_del_texto(texto):
    return len(texto)

def palabras_del_texto(texto):
    separador= " ,.-_;:¡!?¿"
    palabra=""
    suma= []
    for x in texto:
        if x not in separador:
            palabra = palabra + x
        else:
            suma.append(palabra)
            palabra= ""
    suma.append(palabra)
    for i in suma:
        if i == "":
            suma.remove(i)
    print(suma)
    return suma

def oraciones(texto):
    oracion=""
    lista_oraciones=[]
    for x in texto:
        if x != ".":
            oracion= oracion + x
        else:
            lista_oraciones.append(oracion)
            oracion= ""
    lista_oraciones.append(oracion)
    for i in lista_oraciones:
        if i == "":
            lista_oraciones.remove(i)
    print(lista_oraciones)
    return len(lista_oraciones)

def vocales(palabra):
    vocales= "aeiou"
    lista=[]
    for x in palabra:
        if x[0].lower() in vocales:
            lista.append(x)
    print(lista)
    return len(lista)
def consonates(palabra):
    consonate= "bcdfghjklmnñpqrstvwxyz"
    lista=[]
    for x in palabra:
        if x[0].lower() in consonate:
            lista.append(x)
    print(lista)
    return len(lista)

def tipo_de_inicial(tipo):
    if tipo == "v".lower():
        print(vocales(palabras))
    elif tipo == "c".lower():
        print(consonates(palabras))
    else: 
        print("Opcion incorrecta. Debe ingresar v ó c")

def search_word(texto,word):
    list_of_words=[]
    for x in texto:
        if word.lower() == x.lower():
            list_of_words.append(x)
    if len(list_of_words)>0:
        return "Se encontraron " + str(len(list_of_words)) +" palabras igual a "+"'"+ word+"'" +" en el texto."
    else:
        return "No se encontró esa palabra en el texto."
def mayusculas(mayus):
    inicial="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    list=[]
    for x in mayus:
        if x[0] in inicial:
            list.append(x)
    print(list)
    return len(list)
def numeros(texto):
    num="0123456789"
    list=[]
    for x in texto:
        if x in num:
            list.append(x)
    print(list)
    return len(list)
def infinitivo(palabra):
    list=[]
    infinitive=["ar","er","ir"]
    for x in palabra:
        if (x[-2] + x[-1] ) in infinitive:
            list.append(x)
    print(list)
    return len(list)
#Ejecuciones
redaccion="Hola gise, como estas. hola Gise Tenes que estudiar historia. Ahora podes descansar. Gise, hola, como estas naci el 07 08 1990. Comer, dormir."
#redaccion=redaccion()
print(longitud_del_texto(redaccion))
print(oraciones(redaccion))
palabras= palabras_del_texto(redaccion)
print(len(palabras))
inicial= input("Ingrese v para visualizar la cantidad de palabras que inician con vocal o c para las que inician con consonante: ")
tipo_de_inicial(inicial.lower())
wrd= input("Ingrese una palabra: ")
print(search_word(palabras, wrd.lower()))
print(mayusculas(palabras))
print(numeros(redaccion))
print(infinitivo(palabras))

#Ejercicio 12

def numMasAlto():
    lista= [1, 14, 56, 43, 23, 46, 58, 123, 67]
    posicion=-1
    numero=[]
    for n in lista:
        if n > posicion:
         posicion= n
         numero=n
    return numero
print(numMasAlto())
"""
#3)Realice un programa a través el cual pueda ingresar información de vinos. De cada vino se conoce su nombre, año 
#de cosecha, tipo de uva y su valor de costo. La carga finaliza cuando se ingresa 'XXX'
#Luego deberá contar cuantos vinos son de la cosecha 2000 o superior.
#También indicar el valor total de todos los vinos del tipo 'Malbec'
#Por ultimo calcular promedio del valor de los vinos ingresados anteriormente donde su año de cosecha esté en el rango
#2010 a 2022.
#Nota general: Se requiere utilizar funciones y el uso de un menú para realizar las invocaciones correspondientes.

def carga_de_datos():
    vinos=[]
    nombre=input("Ingrese el nombre del vino: ")
    while nombre != "XXX":
        año= int(input("Ingrese el año de la cosecha: "))
        tipo= input("Ingrese el tipo de uva: ")
        precio= float(input("Ingrese el costo del vino: "))
        vinos.append([nombre, año, tipo, precio])
        nombre=input("Ingrese el nombre del vino: ")
    return vinos

def cosechas_despues_2000(vinos2000):
    after2000= []
    for v in vinos2000:
        if v[1] >= 2000:
            after2000.append(v)
    if len(after2000)>0:
        print("Hay " + str(len(after2000))+ " vinos que son de cosechas después del año 2000")
    else:
        print("No hay vinos de cosecha a partir del año 2000")

def tiposMalbec(vinosMalbec):
    malbec=[]
    for v in vinosMalbec:
        if v[2].lower()== "Malbec".lower():
            malbec.append(v)
    return malbec

def valor_total_malbec(malb):
    suma=0
    for v in malb:
        suma= suma + v[3]
    return suma
def promedioDelRango(vinos2010a2022):
    suma=0
    vin=[]
    for v in vinos2010a2022:
        if v[1]>=2010 and v[1]<=2022:
            suma= suma + v[3]
            vin.append(v)
    prom= suma/len(vin)
    return prom
#ejecuciones
#bodegaDeVinos= carga_de_datos()
bodegaDeVinos=[["Elemento",2001,"malbec",2050],["cosecha tardia",2010,"Cabernet",1500],["Luigi Vosca",1995,"malbec",11550],["Benjamin Nieto",2017,"Cabernet",6500],["Santa Julia",2016,"blanco dulce",2600]]
tipM= tiposMalbec(bodegaDeVinos)

#Menú
def opcionesMenu():
    print("1-Lista de todos los vinos")
    print("2-Cantidad de vinos a partir del año 2000")
    print("3-Valor total de los vinos Malbec")
    print("4-Promedio del valor de los vinos entre los años 2010 a 2022")
    print("5-Salir")

opcionesMenu()
opciones= input("Ingrese una opción del menú: ")
while opciones != "5":
    if opciones == "1":
        for x in bodegaDeVinos:
            print(x[0],"-Año de cosecha: "+ str(x[1]),"-"+ x[2], "- $"+str(x[3]))
    elif opciones == "2":
        cosechas_despues_2000(bodegaDeVinos)
    elif opciones == "3":
        print("El costo del valor total de vinos de tipo Malbec es: " + str(valor_total_malbec(tipM)))
    elif opciones == "4":
        print("El promedio es: "+ str(promedioDelRango(bodegaDeVinos)))
    else:
        print("La opción ingresada no corresponde al menú")
    opcionesMenu()
    opciones= input("Ingrese una opción del menú: ")
    