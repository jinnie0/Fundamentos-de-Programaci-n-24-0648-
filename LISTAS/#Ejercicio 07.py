#Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el promedio entero de los datos de la lista

lista= []
suma= 0

while True:
    numero= int(input("Ingrese el número: "))
    lista.append(numero)
    if len(lista)==10:
        break


for i in lista: 
    suma+=i

promedio= int(suma/len(lista))

print ("Tu lista:", lista)

print ("El promedio entero de los números de tu lista es:", promedio)

