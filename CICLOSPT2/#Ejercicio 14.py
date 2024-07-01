# Mostrar en pantalla los primeros 20 múltiplos de 3.

continuar= int(input("¿Quieres conocer los primeros 20 múltiplos de 3? (Si=1/No=0): "))

lista= []

if continuar==1:

    for x in range(3, 61):
        lista.append(x)
    print(lista, "son los primeros 20 múlitplos de 3.")
else:
    print("Fin del programa.")