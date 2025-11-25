nombres=["Anita","Carlos","Diangela","Pedrito","Samuel"]
notas1=[80,80,70,80,50]
notas2=[90,85,60,80,85]
sexos=["F","M","F","M","M"]
edades=[17,20,16,19,15]
total=[0]*5
promedios=[0]*5

def procesar(arreglo_n1,arreglo_n2,arreglo_t,arreglo_p):
    for i in range(len(nombre)):
        arreglo_t[i]=arreglo_n1[i]+arreglo_n2[i]
        arreglo_p[i]=(arreglo_n1[i]+arreglo_n2[i])/2

def imprimir(arreglo_n,arreglo_n1,arreglo_n2,arreglo_t,arreglo_p):
    print("Listado de calificaciones")
    for i in range(len(arreglo_t)):
        print(f"Estudiante: {arreglo_n[i]}, tiene N1: {arreglo_n1}")
        print(f"N2: {arreglo_n2[i]}, sumando un total de: {arreglo_t}")
        print(f"Promedio de notas: {arreglo_p[i]}")

procesar(notas1,notas2,total)
imprimir(nombres,notas1,notas2,total,promedios)