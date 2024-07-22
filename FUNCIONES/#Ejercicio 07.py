# Palíndromo

print("*"*5 + "Función de Palíndromo" +"*"*5 )

def palíndromo(palabra):
    if palabra[::-1]==palabra:
        return "es palíndromo"
    else:
        return "no es palíndromo"
    
palabra= input("Ingrese una palabra: ")

resultado= palíndromo(palabra)

print (f"{palabra} {resultado}.")
        