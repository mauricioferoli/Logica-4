def cargar (lista_n, lista_e, lista_c):
    while True:
        name=input("Como se llame el paciente?")
        lista_n.append(name)
        edad=int(input("Cuantos años tiene el paciente?"))
        lista_e.append(edad)
        email=input("Correo-> ").lower()
        lista_c.append(email)
        resp=input("Presione X para detener el registro").upper()
        if resp=="X":
            break

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

def menu():
    print("1) Registrar pacientes")
    print("2) Ver listado de pacientes")
    print("3) Buscar pacientes")
    print("4) Salir")
    print("Seleccione una opcion")
    opcion=int(input("-> "))
    return opcion
       
#main
nombres=[]
edades=[]
correos=[]
while True:
    opcion=menu()
    match opcion:
        case 1:
            cargar(nombres, edades, correos)
        case 2:
            imprimir(nombres, edades, correos)
        case 3:
            busqueda(nombres, edades, correos)
        case 4:
            print("Haste luego")
        case _:
            print("Opcion invalida")
    if opcion==4:
        break