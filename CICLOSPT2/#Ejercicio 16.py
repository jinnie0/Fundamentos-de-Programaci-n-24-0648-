#Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos.

x= int(input("¿Cuántos primeros múltiplos de 2 quiere? "))

y= int(input("¿Cuántos primeros múlitplos de 5 quiere? "))

suma2=0
suma5=0

multiplos= 2*x
for i in range (2, multiplos+1):
    if i%2==0:
        suma2= suma2+i
promedio2= int(suma2/x)


multiplos= 5*y
for z in range (5, multiplos+1):
    if z%5==0:
        suma5= suma5+z
promedio5= int((suma5/y))


if promedio5<promedio2:
    print ("El promedio de los múltiplos de 2 es mayor que el de los múltiplos de 5. Promedio de 5=" ,promedio5, "y Promedio de 2=", promedio2)
elif promedio5==promedio2:
    print ("Los dos promedios tienen el mismo valor. Promedio de 5=" ,promedio5, "y Promedio de 2=", promedio2)
else:
    print ("El promedio de los múltiplos de 5 es mayor que el de los múltiplos de 2. Promedio de 5=" ,promedio5, "y Promedio de 2=", promedio2)