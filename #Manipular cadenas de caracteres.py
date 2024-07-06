#Manipular cadenas de caracteres

while True: 

    continuar= int(input("¿Quieres correr o seguir corriendo el código? (Si=1/No=0):" ))
    
    if continuar==1:

        print ("-"*10 + "Manipulador de texto" + "-" *10)

        texto= input("Ingrese un texto: ")

        count= 0

        print ("Texto en mayúscula:")
        print (texto.upper())

        print ("Texto en minúscula:")
        print (texto.lower())

        print ("Primeros dos caracteres:")
        print (texto[0:2])

        print ("Últimos dos caracteres:")
        print (texto[::-1] [0:2] [::-1])

        print ("Repetición:" )
        if texto[-1] in texto:
            count+= 1
            print ("El último caracter se repite",count, "veces.")
        else:
            print ("El último caracter no se repite.")

        print ("Texto invertido:" )
        print (texto[::-1])
    else:
        break

print ("-" *9 + "Fin del código" + "-"*9)



