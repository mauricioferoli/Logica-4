def leer_cadenaNum(msj, min, max, error):
    while True:
        print(msj)
        dato=input()
        if dato.isdigit() and (len(dato)>=min and len(dato)<=max):
            return dato
        else:
            print(error)

cedula=leer_cadenaNum("Ingresa tu cedula",7,8,"La cedula debe tener solo numeros entre 7 y 8 digitos")