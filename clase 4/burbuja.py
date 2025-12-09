def ordenar_asc(lista):
    for i in range(len(lista)):
        for j in range (len(lista)-1):
            if lista[j]>lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux

def imprimir(lista):
    print("Datos registrados")
    for valor in lista:
        print(valor)

nombres=["Julian","Josefina","Petra","Zuly","Humberto","Romelia","Ana"]
numeros=[1520,6850,2510,2360,9630,10452,15,500]
imprimir(numeros)
ordenar_asc(numeros)
imprimir(numeros)