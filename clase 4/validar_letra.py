def validar_letra(msj, letra1, letra2, error):
    while True:
        print(msj)
        letra=input().upper()
        if len(letra)>1:
            print("Solo debe ingresar una letra")
            continue
        if letra==letra1 or letra==letra2:
            return letra
        else:
            print(error)

sexo=validar_letra("Ingrese su genero F/M","F","M","El sexo debe ser F o M")