def cargar(arreglo):
    for i in range(len(arreglo)):
        print(f"Ingrese el mes {i+1}")
        dato=input()
        arreglo[i]=dato
        #arreglo[i]=input

def imprimir(arreglo):
    for value in arreglo:
        print(value)    

def imprimir_while(arreglo):
    i=0
    while i<len(arreglo):
        print(arreglo[i])
        i=i+1    
nombres=["Ana","Jose","Luis","Oscar","Fernando","Rafael","Silvia"]
meses=["","","","","","","","","","","",""]
print("Meses del año")
imprimir_while(nombres)
cargar(nombres)
imprimir_while(nombres)

    