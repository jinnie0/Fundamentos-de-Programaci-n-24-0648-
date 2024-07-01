#Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5. 

ter5= 0
cont= 0

continuar= int(input("¿Quieres empezar? (Si=1/No=0): "))


if continuar==1:
    while True:
        numero= int(input("Digite un número: "))
        lastdigit= int(numero%10)
        if lastdigit==5:
            ter5+= numero
            cont+=1

        if numero==0:
            break

promedio= int(ter5/cont)
print (promedio, "Es el promedio de todos los números digitados terminados en 5.")

