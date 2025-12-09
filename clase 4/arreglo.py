import validar_num as f

def cargar(lista, lista_c):
    print("Registro de datos")
    while True:       
        edad=f.validar_num_rango("Ingrese la edad",12,25,"La edad debe estar entre 12 y 25")
        cedula=f.leer_cadenaNum("Ingresa tu cedula",7,8,"La cedula debe tener solo numeros entre 7 y 8 digitos")
        lista.append(edad)
        lista_c.append(cedula)
        resp=input("X para detener").upper()
        if resp=="X":
            break

def imprimir(lista):
    print("Datos registrados")
    for valor in lista:
        print(valor)

edades=[]
cedula=[]
cargar(edades)
imprimir(edades)