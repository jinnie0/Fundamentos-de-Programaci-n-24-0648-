# Mostrar en pantalla todos los pares comprendidos entre 20 y 200.

continuar= int(input("¿Quieres saber cuáles son todos los pares comprendidos entre 2 y 200? (Si=1/No=0): "))

x= range(2,200)

if x%2==0:
    pares=[]
    for x in range(2, 200):
        pares.append(x)
    print(pares)