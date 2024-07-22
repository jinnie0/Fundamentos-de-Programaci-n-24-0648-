#Conversión de Grados Celsius a Fahrenheit

print("*"*5 + "Función de Celsius a Fahrenheit" +"*"*5 )

def conversión(celsius):
    F= ((9/5) * celsius) + 32
    return F



celsius= int(input("Ingresa los grados Celsius a convertir: "))

resultado= conversión(celsius)

print(f"{celsius} grados Celsius son {resultado} grados Fahrenheit.")