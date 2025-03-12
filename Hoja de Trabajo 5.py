#Ejercicio 1 
print("----------------------------")
print("Ejercicio 1")
consumo=float(input("Ingrese su consumo de agua em metros cúbicos: "))
people=int(input("Ingrese el número de habitantes en el apartamento:"))
tarifa=0
costo=0
if consumo<15:
    tarifa=5
elif consumo<=30 and consumo>=15:
    if people>3:
        tarifa=4
    elif people==3:
        tarifa=4.5
    else:
        tarifa=5
        
else:
    if people>5:
        tarifa=4
    elif (people%2==0):
        tarifa=4
    else:
        tarifa=4.2

costo=tarifa*consumo
print(f"El costo del consumo de agua es de Q{costo}")

print("----------------------------")
print("Ejercicio 2")

year=int(input("Ingrese el año de su vehículo:"))
placa=input("Ingrese la placa de su vehículo en el formato de placas guatemaltecas 000AAA:")

if (len(placa)==6):
    if year>=2001:
        placalist=list(placa)
        last=int(placalist[2])
        
        if ((last%2)==0):
            print("-El véhiculo no puede circular los lunes")
            if (year%2==0):
                print("-El vehículo no puede circular los sábados hasta el medio día")
        elif (last%2==1):
            print("-El véhiculo no puede circular los viernes")
            if (year%2==0):
                print("-El vehículo no puede circular los sábados hasta el medio día")
    else:
        print("-El vehículo debe ir a un mantenimiento obligatorio")
else:
    print("placa no válida")
