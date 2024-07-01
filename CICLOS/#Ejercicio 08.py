# Mostrar en pantalla todos los pares comprendidos entre 20 y 200.

lista= []

continuar= int(input("¿Quieres saber cuáles son todos los pares comprendidos entre 2 y 200? (Si=1/No=0): "))


if continuar==1:

    for x in range(20,200):
        if x%2==0: 
            lista.append(x)
    print (lista)
    print ("Estos son todos los números pares comprendidos entre 20 y 200.")
