#Filtrar elementos 

lista= [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

pares = [element for element in lista if element % 2 == 0]
print(pares)

impares= [element for element in lista if element % 2 != 0]
print(impares)
