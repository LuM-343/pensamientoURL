#Ejercicio 1
print("Ejercicio No.1")
print()
texto=str(input("Ingrese su oración:"))
text=texto.split()
num=(len(text))-1
print(f"La primera palabra es: {text[0]}. La última palabra es: {text[num]}.")


#Eliminar los espacios repetidos de una cadena
print("Ejercicio No.2")
print()
texto=str(input("Ingrese su oración:"))
text=texto.split()
clean_text =" ".join(text)
print(clean_text)


#Extraer el dominio de un correo
print("Ejercicio No.3")
print()
correo=str(input("Ingrese el correo:"))
email=correo.split("@")
print(email[1])


#verifica si tiene la extensión correcta (ej. .pdf).
print("Ejercicio No.4")
print()
doc=str(input("Ingrese su documento:"))
name_doc=doc.split(".")
extension = name_doc[1]
val=False
val=bool(name_doc[1]=="pdf")
print(val)


#Invertir el orden de las palabras
print("Ejercicio No.5")
print()
texto=str(input("Ingrese su oración:"))
text=texto.split()
revez_text =text[::-1]
revez_texto= " ".join(revez_text)
print(revez_texto)


#Copia barata de ChatGPT
print("Ejercicio No.6")
print()
poema_alegria="Entonces, entendemos la esencia del aromo y toda la certeza que es causa de la fe. Es fábrica la mente, ¡qué dicha que tenemos! Es fuerte y es potente, del cielo, lo mejor. Vivimos por la gracia y eso, eso lo sabemos,ahora caminemos unidos y en amor."
poema_amor="Y es tan divina tu presencia que el solo verte dislumbra mi corazon, me quedo ciego ante el mundo, es tan corta mi comprensión, no se como hablarte, solo tengo la convicción que debo amarte"
poema_desamor="No entiendo esta soleda, por que la vida es tan cruel, cual es la desdichada necesidad de amar, que sentido tiene el dar, si siempre se perderá, solo la soledad será mi compañia, solo los tristes suspiros de la ciudad sin alma."
cancion_tecun="Tecun Umán Príncipe Quiche Bravo capitán Héroe Nacional Tecun Umán Hoy te canto yo Quiero recordar Tu gloria otra vez. En las selvas y montañas En los valles siempre estás. Imponente tu  figura Hijo amado del Quetzal"
poema_padre="A Dios doy gracias por ser mi padre. Por tus reproches y consejos. Por el bien que me enseñaste y de mi ser siempre cuidaste. Por ser padre bondadoso, lleno de paz y sabiduría. Porque amas la verdad. Justicia y rectitud en demasía. Por ser mi padre amado y enseñarme la caridad."


texto=str(input("Sobre que tema necesitas que escriba: "))

if ("desamor" in texto) and ("poema" in texto):
    print("Escribí este poema de desamor para ti")
    print(poema_desamor)
elif ("alegria" in texto) and ("poema" in texto):
    print("Escribí este poema de alegria para ti")
    print(poema_alegria)
elif ("tecun" in texto) and ("canción" in texto):
    print("Escribí este poema patrio para ti")
    print(cancion_tecun)
elif ("amor" in texto) and ("poema" in texto):
    print("Escribí este poema de amor para ti")
    print(poema_amor)
elif ("padre" in texto) and ("poema" in texto):
    print("Escribí este poema sobre los padres para ti")
    print(poema_padres)
else:
    print("Error, servidor no disponible")
