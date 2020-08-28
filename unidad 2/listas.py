#Ejercicio 1

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

# Ejercicio 2
pares = []
cadena_teclado = input("Ingrese valores a la lista separados por espacio: ")
pares = cadena_teclado.split()
print ("La lista ingresada es ",pares)
indice = int (input("Que indice desea cambiar considerando que comienza en 0: "))
valor = input("Ingrese el valor nuevo: ")
pares[indice]=valor
print ("La lista modificada es {}. Sublista 1: {} Sublista 2: {}".format(pares,pares[:int(len(pares)/2)],pares[int(len(pares)/2):]))

## Ejercicio 3

lista = []
cadena_teclado_1 = input("Ingrese valores a la lista separados por espacio: ")
lista = cadena_teclado_1.split()
print ("La lista ingresada es ",lista)
valor_nuevo = input("Ingrese un valor nuevo a la lista: ")
lista.append(valor_nuevo)
print ("La lista con el valor nuevo es ",lista)
valor_eliminado = input("Ingrese el valor que desea borrar: ")
lista.remove(valor_eliminado)
print ("La lista con el valor eliminado es  ",lista)
valor_indice = int(input("Ingrese el valor del indice a insertar: "))
valor = input("Ingrese el valor a insertar: ")
lista.insert(valor_indice,valor)
print ("La lista con el valor nuevo es ",lista)

lista_enteros = []
cadena_teclado_2 = input("Ingrese valores enteros a la lista separados por espacio: ")
lista_enteros = list(map(int, cadena_teclado_2.split()))
print ("La lista ingresada es ",lista_enteros)
valor_nuevo = int(input("Ingrese un valor nuevo a la lista: "))
lista_enteros.append(valor_nuevo)
print ("La lista con el valor nuevo es ",lista_enteros)
valor_eliminado = int(input("Ingrese el valor que desea borrar: "))
lista_enteros.remove(valor_eliminado)
print ("La lista con el valor eliminado es  ",lista_enteros)
valor_indice = int(input("Ingrese el valor del indice a insertar: "))
valor = int(input("Ingrese el valor a insertar: "))
lista_enteros.insert(valor_indice,valor)
print ("La lista con el valor nuevo es ",lista_enteros)

lista_flotante = []
cadena_teclado_3 = input("Ingrese valores flotantes a la lista separados por espacio: ")
lista_flotante = list(map(float, cadena_teclado_3.split()))
print ("La lista ingresada es ",lista_flotante)
valor_nuevo = float(input("Ingrese un valor nuevo a la lista: "))
lista_flotante.append(valor_nuevo)
print ("La lista con el valor nuevo es ",lista_flotante)
valor_eliminado = float(input("Ingrese el valor que desea borrar: "))
lista_flotante.remove(valor_eliminado)
print ("La lista con el valor eliminado es  ",lista_flotante)
valor_indice = int(input("Ingrese el valor del indice a insertar: "))
valor = float(input("Ingrese el valor a insertar: "))
lista_flotante.insert(valor_indice,valor)
print ("La lista con el valor nuevo es ",lista_flotante)
