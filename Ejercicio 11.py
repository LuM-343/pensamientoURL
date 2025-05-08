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


#Ejercicio 2
#Calculadora
import math

class OperacionCientifica ():
    def __init__(self, numUno, numDos):
        self.numUno=numUno
        self.numDos=numDos
        
    def Calcular(self):
        try:
            print(f"Suma= {self.numUno+self.numDos}")
            print(f"Resta= {self.numUno-self.numDos}")
            print(f"Multiplicación= {self.numUno*self.numDos}")
            print(f"División= {self.numUno/self.numDos}")
        except TypeError:
            print("Datos no válidos")
        except ZeroDivisionError:
            print("No se puede dividir por 0")
            
class RaizCuadrada (OperacionCientifica):
    def __init__(self, numUno, numDos):
        super().__init__(numUno, numDos)
    
    def Operar(self):
        try:
            raiz=math.sqrt(self.numUno)
            print(raiz)
        except TypeError:
            print("Datos no válidos")
        except ValueError:
            print("El numero no puede ser negativo")

class Potencia (OperacionCientifica):
    def __init__(self, numUno, numDos):
        super().__init__(numUno, numDos)
    
    def Operar(self):
        try:
            potencia=self.numUno**self.numDos
            print(potencia)
        except TypeError:
            print("Datos no válidos")
            
class Logaritmo (OperacionCientifica):
    def __init__(self, numUno, numDos):
        super().__init__(numUno, numDos)
    
    def Operar(self):
        try:
            logaritmo= math.log(self.numUno,self.numDos)
            print(logaritmo)
        except TypeError:
            print("Datos no válidos")
        except ValueError:
            print("El numero no puede ser negativo")
            
class Factorial (OperacionCientifica):
    def __init__(self, numUno, numDos):
        super().__init__(numUno, numDos)
    
    def Operar(self):
        try:
            factorial= math.factorial(self.numUno)
            print(factorial)
        except TypeError:
            print("Datos no válidos")
        except ValueError:
            print("El numero no puede ser negativo")
            

uno=RaizCuadrada(-49,5)
uno.Calcular()
uno.Operar()

dos=Potencia(2,3)
dos.Operar()

tres=Logaritmo(1000,10)
tres.Operar()

cuatro=Factorial(6.2,1)
cuatro.Operar()
