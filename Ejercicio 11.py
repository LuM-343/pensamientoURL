#Luis Manuel Velásquez González
#Ejercicio 1
#Calculadora del tiempo en caida libre
import math
class ExperimentoFisico():
    def realizarExperimento(self):
        pass
        
class CaidaLibre (ExperimentoFisico):
    def __init__(self, altura, gravedad):
        self.altura=altura
        self.gravedad=gravedad
    
    def calcularTiempo(self):
        try:
            tiempo=math.sqrt(2 * self.altura / self.gravedad)
            return tiempo
        except ValueError:
            return("La altura no puede ser negativa")
        except ZeroDivisionError:
            return("La gravedad no puede ser 0")
try:
    altura=float(input("Ingrese la altura: "))
    gravedad=float(input("Ingrese la gravedad: "))
    ejercicio1=CaidaLibre(altura,gravedad)
    print(f"El tiempo es de {ejercicio1.calcularTiempo()}")
except ValueError:
    print("Datos no válidos")
