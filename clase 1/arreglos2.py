meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
print(meses[0]+" /",meses[1]+" /",meses[2]+" /",meses[3]+" /",meses[4]+" /",meses[5]+" /",meses[6]+" /",meses[7]+" /",meses[8]+" /",meses[9]+" /",meses[10]+" /",meses[11])
print("En que mes nacio? ")
mes=int(input("->"))
if mes>0 and mes<=len(meses):
    print(f"Naciste en {meses[mes-1]}")
else:
    print("El año solo tiene 12 meses")