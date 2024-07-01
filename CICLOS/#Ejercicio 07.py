#Mostrar en pantalla todos los enteros comprendidos entre 1 y 100.

continuar= int(input("¿Quieres saber cuáles son todos los enteros comprendidos entre 1 y 100? (Si=1/No=0): "))



if continuar==1:
    all= []
    for x in range(1, 100):
        all.append(x)
    print(all)

