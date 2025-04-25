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

def suma_hasta(n,a=0, b=0):
    if a > n:
        return b
    else:
        return suma_hasta(n,a + 1, b + a)
        
num=int(input("Ingrese un número: "))
print(suma_hasta(num))
print()

#Ejercicio 6
print("--------------------")
print("Ejercicio 6")

def factorial(n,a=1, b=1):
    if a > n:
        return b
    else:
        return factorial(n,a + 1, b*a)
        
num=int(input("Ingrese un número: "))
print(factorial(num))
print()

#Ejercicio 7
print("--------------------")
print("Ejercicio 7")

def min_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        primer_elemento = lista[0]
        resto = min_lista(lista[1:])
        
        # Compara el primer elemento con el mínimo del resto de la lista
        if primer_elemento < resto:
            return primer_elemento
        else:
            return resto

lista = [5, 3, 8, 1, 2]
print(min_lista(lista))
print()

#----------------------------------------------------------
# Segunda parte Laboratorio Luis Manuel Velásquez González
import time
def adivina_el_numero(numero, intentos, tiempo_inicio):
    print ()
    respuesta= int (input("Escribe tu número: "))
    if intentos==1:
        print()
        print(f"Perdiste, el número secreto era {numero}")
        tiempo_final=time.time()
        print(f"Tardaste {int(tiempo_final-tiempo_inicio)} segundos y no adivinaste, ¡que malo!")
    elif numero == respuesta:
        print()
        print (f"Correcto el número secreto es {numero}")
        tiempo_final=time.time()
        print (f"Tardaste {int(tiempo_final-tiempo_inicio)} segundos en adivinarlo")
    else:
        print("Número incorrecto, prueba otra vez")
        adivina_el_numero(numero, intentos-1, tiempo_inicio)
        
#Configurar el juego
print("-------------------------------------------------")
print ("Configuración del Juego")
numero_secreto=int(input("Ingrese el número a adivinar, del 1 al 100: "))

intentos=int(input("Ingrese la cantidad de intentos a tener: "))
print("-------------------------------------------------")
print()

# Iniciar el juego con 5 intentos
print("Bienvenido al juego de Adivina el Número.")
print("Elige un número entre 1 y 100.")
print("¡Buena suerte!")
adivina_el_numero(numero_secreto, intentos, time.time() )
