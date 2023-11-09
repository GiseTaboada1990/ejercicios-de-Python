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
"""
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