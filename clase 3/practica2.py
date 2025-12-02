#???????????????????????????????????????????????????

def buscar_contar(dato, lista):
    encontro=False
    i=0
    posicion=-1
    while i<len(lista)and not encontro:
        if lista[i]==dato:
            encontro=True
            posicion=i
        i=i+1
    return encontro, posicion 

def busqueda(lista, lista_e, lista_c):
    print("Cual es el nombre a buscar")
    name=input
    cantidad, existe=buscar_contar(name, lista)
    if cantidad>0:



#main
nombres=[""]*5
edades=[0]*5
correos=[""]*5

cargar(nombres, edades, correos)
busqueda(nombres, edades, correos)