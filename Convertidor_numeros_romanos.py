#Luis Manuel Velásquez González Carne 1502325
#Programa que regresa los números a romanos en rango del 1-9
print("Bienvenido al convertidor de números Romanos")
print("Solo usar números del 1 al 9")
num=int(input("Ingrese su número\n"))

if (num>=1 and num<=9): 
    if (num<=3 and num>=1):
        resultado = num*'I'
        print(f"El número {num} en Romano es: {resultado}")
    elif (num>=5 and num<=8):
        resultado='V'+((num-5)*'I')
        print(f"El número {num} en Romano es: {resultado}")
    elif num==4:
        resultado= 'IV'
        print(f"El número {num} en Romano es: {resultado}")
    elif num==9:
        resultado='IX'
        print(f"El número {num} en Romano es: {resultado}")
else:
    print("Número fuera de rango")
