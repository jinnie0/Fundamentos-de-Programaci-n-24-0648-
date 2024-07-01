#Leer un número entero y mostrar todos los enteros comprendidos entre 1 y el número leído.

x= int(input("Escribe un número: "))

while x>1:
    x= x-1
    print (x)

print("Esos son todos los números comprendidos entre 1 y el número que escribiste.")  