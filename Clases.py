#Luis Manuel Velásquez González, Caret: 1502325
#Ejercicio 1
#Veterinaria

class Animal:
    def __init__(self, nombre, edad, peso, problema):
        self.nombre=nombre
        self.edad=edad
        self.peso=peso
        self.problema=problema
        
    def Datos_Basicos(self):
        print("---------------")
        print("Datos básicos")
        print(f"El paciente se llama {self.nombre}")
        print(f"Tiene una edad de: {self.edad} años")
        print(f"Pesa {self.peso} kg y nos visita por {self.problema}")
        
class Perro(Animal):
    def __init__(self, nombre, edad, peso, problema, raza, altura):
        super().__init__(nombre, edad, peso, problema)
        self.raza=raza
        self.altura=altura
    
    def Dosis(self):
        dosis=(self.peso*self.altura)/10
        print(); print("-------------------")
        print(f"La dosis para el perro {self.nombre} es de {dosis}")
        
    def Ficha_medica(self):
        print();print("--------------------")
        print("Ficha Médica")
        print(f"Es un perro de raza {self.raza}")
        print(f"De altura {self.altura} cm")
        super().Datos_Basicos()
        
class Gato(Animal):
    def __init__(self, nombre, edad, peso, problema, color, pelaje):
        super().__init__(nombre, edad, peso, problema)
        self.color=color
        self.pelaje=pelaje
    
    def Dosis(self):
        dosis=(self.peso*self.edad)/5
        print(); print("-------------------")
        print(f"La dosis para el gato {self.nombre} es de {dosis}")
        
    def Ficha_medica(self):
        print();print("--------------------")
        print("Ficha Médica")
        print(f"Es un gato de color {self.color}")
        print(f"Con un pelaje {self.pelaje}")
        super().Datos_Basicos()
        
class Ave(Animal):
    def __init__(self, nombre, edad, peso, problema, plumaje, canto):
        super().__init__(nombre, edad, peso, problema)
        self.plumaje=plumaje
        self.canto=canto
    
    def Dosis(self):
        dosis=(self.peso*5)/self.edad
        print(); print("-------------------")
        print(f"La dosis para el ave {self.nombre} es de {dosis}")
        
    def Ficha_medica(self):
        print();print("--------------------")
        print("Ficha Médica")
        print(f"Es un ave de plumaje {self.plumaje}")
        print(f"Con un canto {self.canto}")
        super().Datos_Basicos()

class Reptil(Animal):
    def __init__(self, nombre, edad, peso, problema, cambioPiel, largo):
        super().__init__(nombre, edad, peso, problema)
        self.cambioPiel=cambioPiel
        self.largo=largo
    
    def Dosis(self):
        dosis=(self.peso*self.largo)*1.5
        print(); print("-------------------")
        print(f"La dosis para el reptil {self.nombre} es de {dosis}")
        
    def Ficha_medica(self):
        print();print("--------------------")
        print("Ficha Médica")
        print(f"Es un reptil de largo {self.largo}")
        print(f"Que cambio  piel hace {self.cambioPiel}cm")
        super().Datos_Basicos()
        

print("*************Perro****************")
perro1=Perro("Max",10, 45, "dolor en el oido", "pastor aleman", 15)
perro1.Datos_Basicos()
perro1.Dosis()
perro1.Ficha_medica()
print();print()

print("*************Gato****************")
gato1=Gato("Meshitam", 5, 10, "Grita mucho", "negro", "largo")
gato1.Datos_Basicos()
gato1.Dosis()
gato1.Ficha_medica()
print();print()

print("*************Ave****************")
ave1=Ave("Calin", 6, 3, "No vuela", "largo y colorido", "fuerte")
ave1.Datos_Basicos()
ave1.Dosis()
ave1.Ficha_medica()
print();print()

print("*************Reptil****************")
reptil1=Reptil("Pepe", 7, 6, "No come bie", "2 meses", 15)
reptil1.Datos_Basicos()
reptil1.Dosis()
reptil1.Ficha_medica()
