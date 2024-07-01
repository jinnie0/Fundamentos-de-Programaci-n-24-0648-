#Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído.

numero= int(input("Ingrese un número entero: "))

suma= 0
factorial= 1

for x in range (1, numero+1):
    factorial*= x
    suma+= factorial
print ("La sumatoria de todas las factoriales de", numero, "es", suma)
