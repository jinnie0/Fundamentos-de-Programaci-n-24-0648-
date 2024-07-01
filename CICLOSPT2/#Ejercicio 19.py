#Leer un número entero y mostrar en pantalla su tabla de multiplicar.

numero= int(input("Ingrese un número entero: "))

cont=0

for cont in range (1, 13):
    resultado= numero*cont
    print (numero, "x", cont, "=" ,resultado)
        

