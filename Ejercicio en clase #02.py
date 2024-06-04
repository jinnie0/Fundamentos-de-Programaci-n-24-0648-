#Jinnie Espinosa 24-0648

num1= int(input("Ingresa un número "))
num2= int(input("Ingresa otro número "))

diferencia= abs(num1-num2)

vroom= 1
cont= 0

while vroom <= diferencia:
    if diferencia % vroom == 0:
        cont= cont + 1
    vroom= vroom +1

digits= []
def separar(x):
    while x > 0:
        digits.append(x%10)
        x = x // 10

if 0<num1<99 and 0<num2<99:

    if diferencia%2 == 0 and abs(diferencia) % 10 == 4:
        digit1=int(num1/10)
        digit2=num1%10
        digit3=int(num1/10)
        digit4=num2%10

        suma= (digit1+digit2+digit3+digit4) 
        print("La diferencia es par y termina en 4. La suma de los dígitos de" ,num1, "y" ,num2, "es" ,suma, ".")
        separar(abs(diferencia))
        print("Los dígitos por separado de la diferencia son" ,digits[:], ".")

    elif diferencia%2 == 0 and abs(diferencia) % 10 != 4:
        print("La diferencia es par. La suma de los dígitos de" ,num1, "y" ,num2, "es" ,suma, ".")

    elif cont == 2 and diferencia<10:
        producto= (num1*num2)
        print("La diferencia es igual a un número primo menor que 10. El producto de los dos números es", producto, ".")

    else:
        print("La diferencia de los dos números ingresados no es primo menor que 10 ni par y tampoco termina en 4.")
else:
    print("El o los números ingresados no tienen dos cifras.")