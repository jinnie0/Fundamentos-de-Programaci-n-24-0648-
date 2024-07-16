#Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números con más de 3 dígitos.

lista= []
posiciones= []

while True:
    numero= int(input("Ingrese el número: "))
    lista.append(numero)
    if len(lista)==10:
        break

for i in range(len(lista)):
    if lista[i] > 999:
        posiciones.append(i)

print ("Tu lista es:", lista)

print ("Los números de más de 3 dígitos se encuentran en las posiciones: ", posiciones)








