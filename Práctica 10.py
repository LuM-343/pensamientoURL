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




#Luis Manuel Velásquez González, Caret: 1502325
#Ejercicio 2
#Centro de datos

class Persona:
    def __init__(self, nombre, edad, dpi):
        self.nombre=nombre
        self.edad=edad
        self.dpi=dpi
        
    def Datos_Basicos(self):
        print("---------------")
        print("Datos básicos")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"DPI: {self.dpi}")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, dpi, anio, carrera):
        super().__init__(nombre, edad, dpi)
        self.anio=anio
        self.carrera=carrera
        
    def Datos_Generales(self):
        super().Datos_Basicos()
        print("--Datos específicos--")
        print("Profesión: estudiante")
        print(f"Carrera: {self.carrera}")
        print(f"Año de ingreso a la U: {self.anio}")
        
class Docente(Persona):
    def __init__(self, nombre, edad, dpi, curso, titulo):
        super().__init__(nombre, edad, dpi)
        self.curso=curso
        self.titulo=titulo
        
    def Datos_Generales(self):
        super().Datos_Basicos()
        print("--Datos específicos--")
        print("Profesión: docente")
        print(f"Curso que da: {self.curso}")
        print(f"Título: {self.titulo}")
        
class Administrativo(Persona):
    def __init__(self, nombre, edad, dpi, area, oficina):
        super().__init__(nombre, edad, dpi)
        self.area=area
        self.oficina=oficina
        
    def Datos_Generales(self):
        super().Datos_Basicos()
        print("--Datos específicos--")
        print("Profesión: administrativo")
        print(f"Area de atención: {self.area}")
        print(f"Oficina: {self.oficina}")
        
estudiante1=Estudiante("Juan Cruz", 18, 152314521001, "Ingenieria en sistemas", 2025)
estudiante1.Datos_Generales()

docente1=Docente("Luis Hernandez", 25, 25141236514002, "Pensamiento computacional", "Ingeniero en Sistemas")
docente1.Datos_Generales()

administrativo1=Administrativo("Pedro Peres", 45, 142385147150013, "Artes", "A108-B")
administrativo1.Datos_Generales()
