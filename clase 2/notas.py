def acumular(arreglo):
    acumulador=0
    for valor in arreglo:
        acumulador=acumulador+valor
    return acumulador

def contar(arreglo, valor_referencial):
    contador=0
    for i in range(len(arreglo)):
        if arrreglo[i]>=valor_referencial:
            contador=contador+1
    return contador

def promediar(arreglo):
    prom=acumular(arreglo)/len(arreglo)
    return prom

def porcentaje(arreglo):
    porc=contadores/len(arreglo)*100
    return porc

def imprimir(arreglo):
    for i in range(len(arreglo)):
        print(arreglo[i])

def escala20(arreglo):
    for i in range(len(arreglo)):
        print(f"{arreglo[i]/5} sobre 20")

#main
notas[80,50,90,95,25,60,70]
cantidad=contar(notas,80)
promedio=promediar(notas)
porcentaje_notas=porcentaje(cantidad,notas)
print(f"Cantidad de notas >= 80 {cantidad} siendo un {round(porcentaje_notas,2)}%")
print(f"Promedio de notas {round(promedio,2)}")
print("Notas registradas")
imprimir(notas)