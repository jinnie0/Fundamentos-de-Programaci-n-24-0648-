#Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.

numero= int(input("Ingrese un número entero de 3 dígitos: "))

if 99<numero<1000:
    dig1=int(int(numero/100)%10)
    dig2=int(int(numero/10)%10)
    dig3= int(numero%10)
    if dig1==1:
        print("El primer dígito es 1.")
    elif dig2==1:
        print("El segundo dígito es 1.")
    elif dig3==1:
        print("El tercer dígito es 1.")
    else:
        print("Ninguno de los dígitos es 1.")