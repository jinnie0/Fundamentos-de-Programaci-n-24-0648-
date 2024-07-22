#Función de Suma

def sumar(num1, num2, num3):
    suma= num1+ num2+ num3
    return suma

print("*"*5 + "Función de suma" +"*"*5 )
num1= int(input("Ingresa el primer número: "))
num2= int(input("Ingresa el segundo número: "))
num3= int(input("Ingresa el tercer número: "))


resultado= sumar(num1, num2, num3)

print (f"La suma de los números que ingresaste es {resultado}")
