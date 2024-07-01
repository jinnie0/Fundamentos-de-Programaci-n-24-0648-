#Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído

x= int(input("Ingresa un número entero: "))

dividendo=x

while x>1:
    x=x-1
    if dividendo%x==0:
        print(x)

print("Esos son todos los divisores exactos comprendidos entre 1 y el número leído.")