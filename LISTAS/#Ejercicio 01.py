#Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número leído.

lista= []

while True:
    numero= int(input("Ingrese el número: "))
    lista.append(numero)
    if len(lista)==10:
        break

mayor= max(lista)


print ("Esta es tu lista: ", lista)

print ("El número mayor es: ", mayor, "en la posición", lista.index(mayor))
    

