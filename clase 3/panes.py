def buscar_unico(dato, lista):
    encontro=False
    i=0
    while i<len(lista) and not encontro:
        if lista[i]==dato:
            encontro=True
        i=i+1
    return encontro

def cargar(listap):
    while True:
        nombre=input("Nombre del pan-> ").lower()
        existe=buscar_unico(nombre, listap)
        if not existe:
            listap.append(nombre)
        if existe:
            print("Ya se encuentra registrado")
            continue
        resp=input("Presione X para detener el registro").upper()
        if resp=="X":
            break

#main
panes=[]
cargar(panes)