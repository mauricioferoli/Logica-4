nombre["","",""]
salarios[0]*3
ciudad[""]*3
hijos[0]*3

def cargar(arreglo_n,arreglo_s,arreglo_c,arreglo_h):
    for i in range(len(arreglo_n)):
        print(f"Registrando el trabajador {i+1}")
        arreglo_n[i]=input("Nombre -> ")
        arreglo_s[i]=float(input("Cuanto gana? -> "))
        arreglo_c[i]=input("Donde vive? -> ")
        arreglo_h[i]=int(input("Cuantos hijos tiene? -> "))

def acumular(arreglo):
    acumulador=0
    for valor in arreglo:
        acumulador=acumulador+valor
    return acumulador

def promediar(arreglo):
    prom=acumular(arreglo)/len(arreglo)
    return prom

def imprimir():
    print("Trabajadores ")

#COMPLETAR