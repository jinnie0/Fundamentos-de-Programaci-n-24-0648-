#Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar cuántos divisores exactos tiene este último número entre los valores almacenados en la lista.

lista= []
divisores= []

while True:
    numero= int(input("Ingrese el número: "))
    lista.append(numero)
    if len(lista)==10:
        break

entero= int(input("Ingresa un número entero: "))

for x in lista: 
    if entero%x==0:
        divisores.append(x)

print("Tu lista:", lista)

print ("La cantidad dde divisores exactos de", entero, "contenidos en tu lista es", len(divisores))

print("Estos son:", divisores)