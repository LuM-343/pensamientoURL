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

#Ejercicio 3
print("--------------------")
print("Ejercicio 3")

def cuenta_regresiva(n):
    if n<0:
        print("El tiempo se acabo")
    else:
        print(n)
        cuenta_regresiva(n-1)
        
num=int(input("Ingrese un número: "))
cuenta_regresiva(num)
print()

#Ejercicio 4
print("--------------------")
print("Ejercicio 4")

def cuenta_ascendente(n, a=1):
    if a>n:
        print("Cuenta terminada")
    else:
        print(a)
        cuenta_ascendente(n,a+1)
num=int(input("Ingrese un número: "))
cuenta_ascendente(num)
print()

#Ejercicio 5
print("--------------------")
print("Ejercicio 5")

def suma_hasta(n):
    a=0
    for i in range (0,n+1):
        a=a+i
    return a
        
num=int(input("Ingrese un número: "))
print(suma_hasta(num))
print()
