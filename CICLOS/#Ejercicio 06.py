#Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos.

diccionario= {}
listdig1= []
listdig2= []
listdig3= []

x= int(input("Ingrese un número entero de tres dígitos: "))

if 99<=x<999:
    dig1= int(int(x/100))
    dig2= int(int(x/10)%10)
    dig3= int(x%10)

    while 1<dig1:
        dig1=dig1-1
        if dig1!=1:
            listdig1.append (dig1)

    while 1<dig2:
        dig2=dig2-1
        if dig2!=1:
            listdig2.append (dig2)

    while 1<dig3:
        dig3=dig3-1
        if dig3!=1:
            listdig3.append (dig3)

diccionario["Números del primer dígito"]= listdig1
diccionario["Números del segundo dígito"]= listdig2
diccionario["Números del tercer dígito"]= listdig3

print(diccionario)
print ("Esos son todos los enteros comprendidos entre 1 y cada uno de los dígitos.")
