# Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números negativos hay.

lista= []
contador= 0

while True:
    numero= int(input("Ingrese el número: "))
    lista.append(numero)
    if len(lista)==10:
        break

for i in lista: 
    if i<0:
        contador+=1

print ("Tu lista:", lista)

print ("Cantidad de números negativos en tu lista:", contador)