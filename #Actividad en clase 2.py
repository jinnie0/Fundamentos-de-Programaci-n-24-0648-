#Actividad en clase 2 

datos= "oso, perro, 10, 5 son animales".split (", ")

# oso es un palindormo
# perro no es un palindromo
# tenemos 5 osos
# tenemos 10 perros
# oso y perro son animales

if datos[0]==datos[0][::-1]:
    print (datos[0][0].swapcase() + datos[0][1:],"es palíndromo.")
else:
    print (datos[0][0].swapcase() + datos[0][1:],"no es palíndromo.") 

if datos[1]==datos[1][::-1]:
    print (datos[1][0].swapcase()+ datos[1][1:],"es palíndromo.")
else:
    print (datos[1][0].swapcase()+ datos[1][1:],"no es palíndromo.") 


print ("Tenemos", datos[3] [0:1], datos[0]+ "s.")
print ("Tenemos", datos[2] ,datos[1]+ "s.")

print (datos[0][0].swapcase()+datos[0][1:], "y", datos[1], datos[3][2:]+".")