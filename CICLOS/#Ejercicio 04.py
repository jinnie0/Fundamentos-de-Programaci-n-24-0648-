# Leer dos números y mostrar todos los enteros comprendidos entre ellos.

x= int(input("Ingrese el primer número: "))
y= int(input("Ingrese el segundo número: "))

x1=x

while x<y:
    x=x+1
    if x!=y:
        print(x)

print("Esos son todos los números enteros comprendidos entre",x1, "y",y,"."  )


