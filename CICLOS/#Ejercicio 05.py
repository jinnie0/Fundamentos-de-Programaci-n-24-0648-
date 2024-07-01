#Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.

x= int(input("Ingrese el primer número: "))
y= int(input("Ingrese el segundo número: "))

x1=x

while x<y:
    x=x+1
    dig= int(x%10)
    if x!=y and dig==4:
        print(x)

print("Esos son todos los números enteros terminados en 4 comprendidos entre",x1, "y",y, "."  )


