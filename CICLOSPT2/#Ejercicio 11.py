#Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro.

numero= int(input("Ingrese un número entero de dos dígitos: "))

enteros= []

if  10<=numero<100:
    dig1= int(int(numero/10)%10)
    dig2= int(numero%10)
    if dig2<dig1:
        for x in range (dig2, dig1+1):
            enteros.append(x)
        print (enteros, "Son los números comprendidos entre los dos dígitos del número que ingresaste.")
    elif dig1<dig2:
        for x in range (dig1, dig2+1):
            enteros.append(x)
        print(enteros, "Son los números comprendidos entre los dos dígitos del número que ingresaste.")    
    else:
        print("Los dígitos del número ingresado son iguales.")
    
    
