def numero (anos,interes,inversion):
    for i in range(anos):
        inversion = inversion * (1 + interes/100)
    print("EL CAPITAL GANADO ES " + str(round(inversion, 2)))

        
anos = int(input("INTRODUCE LOS AÑOS:"))
interes = int(input("INTRODUCE EL INTERES:"))
inversion = int(input("INTRODUCE LA INVERSION:"))

numero(anos,interes,inversion)