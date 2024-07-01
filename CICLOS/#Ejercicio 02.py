#Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.

x= int(input("Ingrese un número entero: "))


while x>1:
    x=x-1
    if x%2==0:
        print(x)
        
print("Esos son todos los enteros pares entre el 1 y el número que escribiste.")