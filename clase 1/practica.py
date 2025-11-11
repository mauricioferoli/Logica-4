def cargar(arreglo, msj):
    print("-"*30)
    print("Registro de datos")
    for i in range(len(arreglo)):
        print(f"{msj} {i+1}?")
        arreglo[i]=int(input())

def imprimir(arreglo):
    print("="*30)
    print("Datos de arreglo")
    for value in arreglo:
        print(value)  

def det_mayor(arreglo):
    mayor=0
    for i in range(len(arreglo)):
        if arreglo[i]>mayor:
            mayor=arreglo[i]
    return mayor

def mostrar_m(arreglo, valor_referencia):
    print(f"Valores del arreglo = {valor_referencia}")
    contador=0
    for i in range(len(arreglo)):
        if arreglo[i]==valor_referencia:
            print(arreglo[i])
            contador=contador+1
    print(f"En total, hay {contador} valores iguales a {valor_referencia}")

edades=[0,0,0,0,0,0,0,0,0,0]
cargar(edades, "Cual es la edad")
imprimir(edades)
edad_mayor=det_mayor(edades)
print(f"La edad mayor es {edad_mayor}")
mostrar_m(edades, edad_mayor)