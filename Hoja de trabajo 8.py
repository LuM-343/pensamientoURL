#ejercicio 1
print("-----------------------------------------------------------")
print("Ejercicio No. 1")
print("Obtener los multiplos de un número")
n=int(input("Ingrese hasta que multiplo desea conocer: "))
base=int(input("Ingrese el número del que se sacaran los multiplos: "))
multiplos=[]

for i in range (1,n+1):
    multiplos.append((i*base))
print(multiplos)

#ejercicio 2
print("-----------------------------------------------------------")
print("Ejercicio No. 2")
print("Captura de nombres de usuario")
n=int(input("Ingrese la cantidad de nombres a ingresar:"))
nombres=[]
largo=[]
for i in range (0,n):
    nombre=str(input(f"Ingrese el nombre No.{(i+1)}:"))
    nombres.append(nombre)
    largo.append(len(nombre))
print(nombres)
print(largo)

#Escenario 1
print("-----------------------------------------------------------")
print("Escenario No. 1")
print("Encuesta de atención al cliente")
n=int(input("Ingrese la cantidad de personas encuestadas:"))
personas=[]
respuestas=[]
excelente=0
muyBuena=0
buena=0
regular=0
mala=0
suma=0
print("¿Cómo calificria nuestro servicio?")
print("Siendo 5 excelente, 4 muy buena, 3 buena, 2 regular y 1 malo")
for i in range (0,n):
    print()
    encuesta=int(input("Ingrese su respuesta: "))
    personas.append((i+1))
    respuestas.append(encuesta)
    
print(personas)
print(respuestas)

for i in range (0,len(personas)):
    if respuestas[i]==5:
        suma=suma+5
        excelente+=1
    elif respuestas[i]==4:
        suma=suma+4
        muyBuena+=1
    elif respuestas[i]==3:
        suma=suma+3
        buena+=1
    elif respuestas[i]==2:
        suma=suma+2
        regular+=1
    elif respuestas[i]==1:
        suma=suma+1
        mala+=1

print("Cantidad de respuestas")        
print(f"Excelente: {excelente}")
print(f"Muy buena: {muyBuena}")
print(f"Buena: {buena}")
print(f"Regular: {regular}")
print(f"Mala: {mala}")

resultados=[mala, regular, buena, muyBuena, excelente]
mayor=max(resultados)
print()
print("El mayor es:")
if mayor==mala:
    print(f"Mala con {mala}")
elif mayor==regular:
    print(f"Regular con {regular}")
elif mayor==buena:
    print(f"Buena con {buena}")
elif mayor==muyBuena:
    print(f"Muy buena con {muyBuena}")
elif mayor==excelente:
    print(f"Excelente con {excelente}")
    
prom=suma/n
print()
print(f"El promedio de respuestas es {prom}")
r=0
for i in range (0,n):
    if respuestas[i]<prom:
        r+=1
porcentaje= (r*100)/n
print(f"El {porcentaje}% dio una calificación menor al promedio")
print("Fin")
