#Hoja de Trabajo No. 13
#Luis Manuel Velásquez González
#Ejecercio único
print("*"*30);print("Bienvenido al Juego de la Vida")
print("*"*30);print()
matriz= [
 [0,0,0,0,0,0,0,1,1,0],
 [0,1,1,0,0,0,0,0,0,0],
 [0,1,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,1,0],
]

def imprimir_tablero(matriz):
    for fila in matriz:
        print(fila)

def siguiente_generacion(matriz):
    nueva_generacion=[]
    for i in range (0, len(matriz)):
        fila=[]
        for j in range (0,  len(matriz[i])):
            r=0
            if j==0:
                if matriz[i][j+1]==1:
                    r=1
                else:
                    r=0
            elif j==(len(matriz[i])-1):
                if matriz[i][j-1]==1:
                    r=1
                else:
                    r=0
            else:
                if (matriz[i][j-1]==1 and matriz[i][j+1]==1) or (matriz[i][j-1]==0 and matriz[i][j+0]==0):
                    r=0
                else:
                    r=1
            fila.append(r)
        nueva_generacion.append(fila)
    return (nueva_generacion)

print("Generación 0:")
imprimir_tablero(matriz)

generacion_1 = siguiente_generacion(matriz)
print();print("Generación 1:")
imprimir_tablero(generacion_1)

generacion_2 = siguiente_generacion(generacion_1)
print();print("Generación 2:")
imprimir_tablero(generacion_2)
