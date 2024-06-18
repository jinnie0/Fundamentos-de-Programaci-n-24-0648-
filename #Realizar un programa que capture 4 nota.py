
#Realizar un programa que capture 4 notas

promedios= []

continuar = True

while continuar:
    
  nombrematricula= input("Ingrese el nombre y matrícula del estudiante: ")

  print("Ahora ingrese las notas del estudiante: ")

  nota1= float(input("Ingrese la primera nota: "))
  nota2= float(input("Ingrese la segunda nota: "))
  nota3= float(input("Ingrese la tercera nota: "))
  nota4= float(input("Ingrese la primera nota: "))

  if nota1<0 or nota2<0 or nota3<0 or nota4<0:
    print("Las notas ingresadas no son validas. No se pueden valores en negativo.")
    continuar= False
  else:
    promedio= int((nota1+nota2+nota3+nota4)/4)

    promedios.append({"nombre y matrícula": nombrematricula, "promedio": promedio})

  otro= int(input("¿Desea ingresar otro estudiante? (Si=1, No=0): "))
  if otro==0:
    continuar=False
  else:
    continuar=True 


print("Las datos de el o los estudiantes son:" ,promedios,)

SiNo= input("¿Desea continuar con el programa? (Si=1, No=0)")

if SiNo== 1:
  continuar= True
else:
  print ("Gracias por usar el programa.")
  
            
