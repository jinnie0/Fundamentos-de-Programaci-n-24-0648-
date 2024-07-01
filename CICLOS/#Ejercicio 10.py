#Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído.

numero= int(input("Ingrese un número: "))
suma= 0

for x in range(1,numero+1):
    suma+= x

print("La suma de los enteros comprendidos entre el 1 y el número que ingresaste es", suma)


    
