lista = []

valor = input ("Ingrese un valor:")
lista.append(valor)
valor_1 = int(input ("Ingrese un valor entero:"))
lista.append(valor_1)
valor_2 = float(input ("Ingrese un valor flotante:"))
lista.append(valor_2)
valor_3 = bool(input ("Ingrese un valor booleano:"))
lista.append(valor_3)
valor_4 = list(input ("Ingrese elementos a la sub-lista: "))
lista.append(valor_4)

print(type(lista))
print("La lista tiene los siguientes datos: ",lista)
