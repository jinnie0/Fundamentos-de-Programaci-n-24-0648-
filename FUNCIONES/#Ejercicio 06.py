#Máximo de Tres Números

def máximo(num):
    maxim= max(lista)
    return maxim
    
print("*"*5 + "Función Máximo de Tres Números" +"*"*5 )

lista= []

while True:
    if len(lista)<3:
        num= int(input(f"Ingresa el número {len(lista)+1}: "))
        lista.append(num)
    else:
        break

    
resultado= máximo(num)
print(f"{resultado} es el máximo de estos tres números.")
