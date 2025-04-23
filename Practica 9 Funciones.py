#Luis Manuel Velásquez González 1502325
#Ejercicio 1
print("--------------------")
print("Ejercicio 1")

def es_par_o_impar (n):
    if n%2==0:
        print("Es un número par")
    else:
        print ("Es un número impar")
        
num=int(input("Ingrese un numero: "))
es_par_o_impar(num)
print()

#Ejercicio 2
print("--------------------")
print("Ejercicio 2")
listado=[5,5,4,4,3,3,2]

def suma_lista(lista):
    a=0
    for i in range (0,len(lista)):
        a=a+lista[i]
    return a
    
print(suma_lista(listado))
print()
