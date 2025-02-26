num=int(input("Ingrese el número de 5 dígitos: "))
a=0
b=0
c=0
d=0
x=0

if(num>9999) and (num<100000):
    dig1=num%10
    dig2=(num%100)//10
    dig3=(num%1000)//100
    dig4=(num%10000)//1000
    dig5=(num//10000)
    
    if (dig1>=dig2):
        a=dig1
        c=dig2
    else:
        a=dig2
        c=dig1
        
    if (dig3>=dig4):
        b=dig3
        d=dig4
    else:
        b=dig4
        d=dig3
        
    if(c>b):
        x=b
        b=c
        c=x
        
    if(d>a):
        x=a
        a=d
        d=x
        
    if (a>=b):
        a=a
    else:
        x=a
        a=b
        b=x
    
    if (c>=d):
        c=c
    else:
        x=c
        c=d
        d=x
    if (dig5<=d):
        print(f"El orden de los números en descendente es el siguiente: {a},{b},{c},{d},{dig5}")
        print(f"El orden de los números en ascendente es el siguiente: {dig5},{d},{c},{b},{a}")
    elif (dig5<=c):
        print(f"El orden de los números en descendente es el siguiente: {a},{b},{c},{dig5},{d}")
        print(f"El orden de los números en ascendente es el siguiente: {d},{dig5},{c},{b},{a}")
    elif (dig5<=b):
        print(f"El orden de los números en descendente es el siguiente: {a},{b},{dig5},{c},{d}")
        print(f"El orden de los números en ascendente es el siguiente: {d},{c},{dig5},{b},{a}")
    elif (dig5<=a):
        print(f"El orden de los números en descendente es el siguiente: {a},{dig5},{b},{c},{d}")
        print(f"El orden de los números en ascendente es el siguiente: {d},{c},{b},{dig5},{a}")
    elif (dig5>=a):
        print(f"El orden de los números en descendente es el siguiente: {dig5},{a},{b},{c},{d}")
        print(f"El orden de los números en ascendente es el siguiente: {d},{c},{b},{a},{dig5}")
else:
    print("Número no válido")
