def validar_positivo(msj):
    while True:
        print(msj)
        dato=int(input())
        if dato>0:
            return dato
        else:
            print("Ingrese valor mayor a cero")
def validar_posi(msj):
    num=-1
    while not num>0:
        print(msj)
        num=int(input())
        if num>0:
            break
        else:
            print("El numero debe ser mayo que 0")
    return num

edad=validar_posi("Ingresa tu edad")
print(edad)