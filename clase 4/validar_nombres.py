def validar_nombre(msj,min, max, error):
    while True:
        print(msj)
        dato=input()
        if dato.isalpha() and (len(dato)>=min and len(dato)<=max) and dato[0].upper()=="A":
            return dato
        else:
            print(error)

nombre=validar_nombre("Como te llamas?",2,15,"El nombre debe tener entre 2 y 15 letras y debe iniciar con A")
print(f"El nombre inicia con {nombre[0]}")
print(f"A".isupper())
print(f"b".isupper())