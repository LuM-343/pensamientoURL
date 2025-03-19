#Cajero Automático con 3000 de saldo

print("Bienvenido al cajero automático de Luis Manuel")
saldo=3000
intentos=3
salir=1
condicion=bool(saldo==0 or intentos==0 or salir=="0")

while condicion==False:
    print("--------------------------------------------------")
    print(f"Saldo disponible: {saldo}")
    retiro=float(input("Ingrese el monto a retirar:"))
    print()
    if retiro>saldo:
        intentos-=1
        if intentos==0:
            print("Saldo insuficiente, no le quedan más intenos, se finalizara sesión")
        else:
            print(f"Saldo insuficiente. Solo le quedan {intentos} intentos")
            salir=input("Presione 0 para salir o cualquier otro número para continuar: ")
    else:
        saldo-=retiro
        if saldo>0:
            print(f"Transacción exitosa. Saldo disponible: Q{saldo}")
        else:
            print("Transacción exitosa, saldos agotados, se finalizará sesión")

        if saldo>0 and intentos>0 and not(salir==0):
            print("¿Desea salir del cajero?")
            salir=input("Presione 0 para salir o cualquier otro número para continuar: ")

    condicion=bool(saldo==0 or intentos==0 or salir=="0")
    print()

print("Sesión en cajero finalizada")