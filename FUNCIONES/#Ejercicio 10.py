# Números Primos

print("*"*5 + "Función de Números Primos" +"*"*5 )

def primo(num):
    for x in range(2, num-1):
        if num % x == 0:
            return "no es primo"
    return "es primo"


num= int(input("Ingresa un número: "))

resultado= primo(num)

print (f"{num} {resultado}.")