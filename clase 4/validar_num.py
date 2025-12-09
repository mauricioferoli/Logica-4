def validar_num_rango(msj, min, max, error):
    while True:
        print(msj)
        numero=int(input())
        if numero>=min and numero<=max:
            return numero
        else:
            print(error)

def leer_cadenaNum(msj, min, max, error):
    while True:
        print(msj)
        dato=input()
        if dato.isdigit() and (len(dato)>=min and len(dato)<=max):
            return dato
        else:
            print(error)