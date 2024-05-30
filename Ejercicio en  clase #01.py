
print("Conoce si tu nombre tiene 3 o más vocales")
vocales=["a","e","i","o","u", "A", "E", "I", "O", "U", "á", "é", "í", "ó", "ú", "Á", "É", "Í"]

nombre= input("Ingrese el nombre: ")

count=0 


for item in nombre:
  if item in vocales:
    
    count+=1

if count>=3:
  print("El nombre",nombre, "tiene", count, "vocales")
else:
  print("El nombre no tiene 3 o más vocales")