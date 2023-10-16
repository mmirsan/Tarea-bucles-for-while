contrasena = "HOLA"
acertado = False
while (not acertado):
    contra =input("Escriba la contraseña: ")
    if (contra == contrasena):
     print("LA CONTRASEÑA ES CORRECTA")
     acertado=True
    else:
        print("LA CONTRASEÑA ES INCORRECTA")