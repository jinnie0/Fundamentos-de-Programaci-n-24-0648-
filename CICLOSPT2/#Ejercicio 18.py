#Generar los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1.


continuar= int(input("¿Quieres empezar? (Si=1/No=0): "))

if continuar==1:

    lista= []
    numero=10

    if numero==10:
        lista.append(numero)

    while numero>1:
        numero= numero-1
        lista.append(numero)

    lista.reverse()
    print (lista)