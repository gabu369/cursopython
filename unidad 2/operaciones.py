valor_1 = int (input("Ingresa el dato 1: \n")) # Se realiza un convert a entero
valor_2 = int (input("Ingresa el dato 2: \n"))
print("Valores ingresados a={}, b={}".format(valor_1,valor_2))

operacion=input(("\nSeleccione una operacion a realizar\n1.{}\n2.{}\n3.{}\n4.{}\n5.{}\n".format("Suma","Resta","Multiplicacion","Division","Todas")))
print ("La operacion es ",operacion)

# Mi forma
#print (valor_1 + valor_2) if operacion=='1' else print (valor_1 - valor_2) if operacion=='2' else print (valor_1 * valor_2) if operacion=='3' else print (valor_1 / valor_2) if operacion=='4' else print ("suma:",valor_1 + valor_2,"resta:",valor_1 - valor_2,"multplicacion:",valor_1 * valor_2,"division:",valor_1 / valor_2) if operacion=='5' else None 

# Otra Forma de Hacerlo
suma = (valor_1 + valor_2) 
resta = (valor_1 - valor_2)
multiplicacion = (valor_1 * valor_2)
division = (valor_1 / valor_2) 

print("La suma de los numeros a:{} + b:{} = {}".format(valor_1,valor_2,suma)) if operacion=='1' else ""
print("La resta de los numeros a:{} - b:{} = {}".format(valor_1,valor_2,resta)) if operacion=='2' else ""
print("La multiplicacion de los numeros a:{} * b:{} = {}".format(valor_1,valor_2,multiplicacion)) if operacion=='3' else ""
print("La division de los numeros a:{} / b:{} = {}".format(valor_1,valor_2,division)) if operacion=='4' else ""
print("Suma:{}\nResta:{}\nMultiplicacion:{}\nDivision:{}".format(suma,resta,multiplicacion,division)) if operacion=='5' else ""
