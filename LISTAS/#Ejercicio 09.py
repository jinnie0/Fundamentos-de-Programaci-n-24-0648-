# Leer 10 números enteros, almacenarlos en una lista y calcular la factorial a cada uno de los números leídos almacenándolos en otra lista.

lista= []
factoriales= []

while True:
    numero= int(input("Ingrese el número: "))
    lista.append(numero)
    if len(lista)==10:
        break

for x in lista:
    factorial= 1
    while x>0:
        factorial*= x
        x-=1
    else:
        factoriales.append(factorial)

print ("Tu lista:", lista)

print ("Las factoriales de los números en tu lista:", factoriales)







