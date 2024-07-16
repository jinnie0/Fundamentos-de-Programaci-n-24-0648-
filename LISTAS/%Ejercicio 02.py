#Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número par leído.

print("-"*5 + "Determinación del mayor número par" + "-"*5 )

lista= []
lista2= []

while True:
    numero= int(input("Ingrese el número: "))
    lista.append(numero)
    if len(lista)==10:
        break

for x in lista: 
    if x%2==0:
        lista2.append(x)

mayor_par= max(lista2)

print ("Esta es tu lista: ", lista)

print ("El número mayor par tiene la posición", lista.index(mayor_par), ".")
    