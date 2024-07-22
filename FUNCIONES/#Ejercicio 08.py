# Factorial

print("*"*5 + "Función de Factorial" +"*"*5 )

def factorial(num):
    factor= 1
    while num>0:
        factor*= num
        num-=1
        if num<=0:
            break
    return factor

num=int(input("Ingrese un número entero: "))

resultado= factorial(num)

print(f"El factorial de {num} es {resultado}.")
