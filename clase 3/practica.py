def cargar (lista_n, lista_e, lista_c):
    for i in range(len(lista_c)):
        lista_n[i]=input("Como se llama el paciente").lower()
        lista_e[i]=int(input("Cuantos años tiene?"))
        lista_c[i]=input("Email-> ")

def imprimir(lista_n, lista_e, lista_c):
    print("LISTA DE PACIENTES")
    for i in range (len(lista_c)):
        print(f"Paciente: {lista_n[i]} tiene {lista_e[i]} y su correo es {lista_c[i]}")

def buscar(dato, lista):
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
    print("Nombre del paciente que desea buscar")
    name=input().lower()
    existe, indice=buscar(name, lista)
    if existe:
        print(f"El paciente {name} se encuentra registrado en el indice {indice}")
        print(f"tiene {lista_e[indice]} y su correo es {lista_c[indice]}")
    else:
        print(f"{name} NO esta registrado")

#main
nombres=[""]*5
edades=[0]*5
correos=[""]*5

cargar(nombres, edades, correos)
busqueda(nombres, edades, correos)