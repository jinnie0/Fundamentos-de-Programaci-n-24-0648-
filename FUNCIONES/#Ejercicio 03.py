#Área de un Rectángulo

def área_rectángulo(base, altura):
    área= base*altura
    return área

print("*"*5 + "Función de área de rectángulos" +"*"*5 )

base= int(input("Ingresa la base de tu rectángulo en metros: "))
altura= int(input("Ingresa la altura de tu rectángulo en metros: "))

resultado= área_rectángulo(base, altura)

print (f"El área de tu rectángulo es {resultado} metros cuadrados.")

