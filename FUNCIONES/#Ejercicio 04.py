#Número Par o Impar

print("*"*5 + "Función de pares/impares" +"*"*5 )

def identificar(num):
    if num%2==0:
        return "par"
    else: 
        return "impar"

num= int(input("Ingresa un número entero: "))

resultado= identificar(num)

print (f"El {num} es {resultado}.")