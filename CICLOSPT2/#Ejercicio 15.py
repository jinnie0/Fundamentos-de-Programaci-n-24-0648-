#Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.

continuar= int(input("¿Quieres conocer la suma de los primeros 20 múltiplos de 3? (Si=1/No=0): "))

suma= 0

if continuar==1:
    for x in range (3, 61):
        if x%3==0:
            suma+= x
    print (suma)
else:
    print ("Fin del programa.")

