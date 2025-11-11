dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
print(dias)
posicion=int(input("Ingresa el nume del dia que deseas ver -> "))
if posicion>0 and posicion<=len(dias):
    print(dias[posicion-1])
else:
    print("La semana solo tiene 7 dias!")