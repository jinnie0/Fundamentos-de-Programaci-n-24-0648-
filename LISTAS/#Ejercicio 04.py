#Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los almacenados en dicho arreglo comienzan en dígito primo

print("-"*5 + "Determinación de números que comiencen con primos" + "-"*5 )

lista= []
lista2= []

while True:
    numero= int(input("Ingrese el número: "))
    lista.append(numero)
    if len(lista)==10:
        break

def primo(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def dig(numero):
    while numero >= 10:
        numero //= 10
    return numero

for x in lista: 
    dig1= dig(x)
    if primo(dig1):
        lista2.append(x)

contador= len(lista2)

print ("Esta es tu lista:", lista)

print ("Los números que comienzan con dígito primo son", contador, "=", lista2)


    