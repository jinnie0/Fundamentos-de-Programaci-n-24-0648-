#Contar Vocales

print("*"*5 + "Contar Vocales" +"*"*5 )

lista= ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

palabra= input("Ingrese una palabra o texto: ")

palabra= palabra.lower()

def conteo_vocales(palabra):
    cont= 0
    for x in palabra:
        if x in lista:
            cont+= 1
    return cont

resultado= conteo_vocales(palabra)

print(f"Hay {resultado} vocales en lo que ingresaste.")
