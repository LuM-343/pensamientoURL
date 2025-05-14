#Laboratorio 12
#Ejercicio Único
#Luis Manuel Velásquez González

# Número de días a registrar
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Datos simulados de 1 semana de paciente
niveles_azucar = [130, 160, 95, 175, 160] # mg/dL
niveles_sal = [2000, 2400, 1800, 2400, 2700] # mg
presion = [115, 130, 110, 125, 175] # mmHg
azucarprom=0
salprom=0
presionprom=0

print("**************************************************")
print("      Hospital Regional de Huehuetenango")
print("Diagnostico de Presión, azucar y sal en sangre")
print("**************************************************")

for i in range(0,len(dias)):
    print();print("-------------------------")
    print(f"Diagnostico día {dias[i]}")
    azucarprom=azucarprom+niveles_azucar[i]
    salprom=salprom+niveles_sal[i]
    presionprom=presionprom+presion[i]
    if niveles_azucar[i]<70:
        print(f"- ¡ALERTA! Su azúcar en sangre es muy baja, {niveles_azucar[i]} mg/dL, requiere atención médica")
    elif niveles_azucar[i]>140:
        print(f"- ¡ALERTA! Su azúcar en sangre es muy alta, {niveles_azucar[i]} mg/dL, requiere atención médica")
    else:
         print(f"- Su azúcar en sangre es saludable, {niveles_azucar[i]} mg/dL")
        
    if niveles_sal[i]<2300:
        print(f"- Su consumo de sal es saludable, {niveles_sal[i]} mg")
    else:
        print(f"- ¡ALERTA! Su consumo de sal no saludable, {niveles_sal[i]} mg, requiere atención médica") 
        
    if presion[i]<120:
        print(f"- Su presión sistólica es normal, {presion[i]} mmHg")
    elif presion[i]>=120 and presion[i]<130:
        print(f"- ¡Alerta presión elevada!, {presion[i]} mmHg, requiere atención médica")
    elif presion[i]>=130 and presion[i]<140:
        print(f"- ¡ALERTA! Hipertensión Etapa 1, {presion[i]} mmHg, requiere atención médica")
    else:
        print(f"- ¡¡EMERGENCIA!! Hipertensión Etapa 2, {presion[i]} mmHg, busque atención médica inmediatamente")
        
print();print("--------------------")
print("Promedios de la semana")
print(f"*| El promedio de azucar en sangre es de {azucarprom/len(dias)} mg/dL")
print(f"*| El promedio de consumo de sal es de {salprom/len(dias)} mg")
print(f"*| El promedio de la presión sistólica es de {presionprom/len(dias)} mmHg")
