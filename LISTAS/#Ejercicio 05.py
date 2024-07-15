#Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares.


lista= []
lista2= []
cont= 0

while True:
    numero= int(input("Ingrese el número: "))
    lista.append(numero)
    if len(lista)==10:
        break

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in lista:
    if es_primo(i):
        lista2.append(i)

def contar_digitos_pares(num):
    cont = 0
    while num > 0:
        dig = num % 10
        if dig % 2 == 0:
            cont += 1
        num //= 10
    return cont

ma_digitos_pares = -1
posicion_max = -1

for i, num in enumerate(lista):
    if es_primo(num):
        digitos_pares = contar_digitos_pares(num)
        if digitos_pares > ma_digitos_pares:
            ma_digitos_pares = digitos_pares
            posicion_max = i

print("Lista de números:", lista)
if posicion_max != -1:
    print("El número primo con mayor cantidad de dígitos pares está en la posición:", posicion_max)
else:
    print("No hay números primos en la lista.")





