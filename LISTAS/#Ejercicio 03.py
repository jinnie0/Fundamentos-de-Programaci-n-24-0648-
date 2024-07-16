#Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número primo leído.

print("-"*5 + "Determinación del mayor número primo" + "-"*5 )

lista= []
lista2= []

while True:
    numero= int(input("Ingrese el número: "))
    lista.append(numero)
    if len(lista)==10:
        break

def primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for x in lista:
    if primo(x):
        lista2.append(x)

mayor= max(lista2)

print ("Esta es tu lista de primos: ", lista)
print ("El número primo mayor se encuentra en la posición", lista.index(mayor))





    