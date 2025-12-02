def cargar(lista_n, lista_e, lista_c):
    while True:
        name=input("Como se llame el paciente?")
        lista_n.append(name)
        edad=input("Cuantos años tiene el paciente?")
        lista_e.append(edad)
        email=input("Correo-> ").lower()
        lista_c.append(emial)
        resp=input("Presione X para detener el registro").upper()
        if resp=="X":
            break

def imprimir(lista_n, lista_e, lista_c):
    print("LISTA DE PACIENTES")
    for i in range (len(lista_c)):
        print(f"Paciente: {lista_n[i]} tiene {lista_e[i]} y su correo es {lista_c[i]}")

#main
nombre=[]
edades=[]
correos=[]

cargar(lista_n, lista_e, lista_c)
imprimir(lista_n, lista_e, lista_c)