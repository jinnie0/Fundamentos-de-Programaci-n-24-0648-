#Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.

numero= int(input("Ingrese un número entero: "))

lista= []

for x in range (1, numero+1):
    if x%5==0:
        lista.append(x)
print (lista, "son todos los múltiplos de 5 comprendidos entre 1 y el número leído.")
