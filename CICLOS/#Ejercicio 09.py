# Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205.


lista= []

continuar= int(input("¿Quieres saber cuáles son todos los números terminados en 6 comprendidos entre 25 y 205? (Si=1/No=0): "))


if continuar==1:
    for x in range(25,205):
        lastdigit= int(x%10)
        if lastdigit==6:
            lista.append(x)
    print(lista)
    print("Estos son todos los números terminados en 6 comprendidos entre 25 y 205.")
