# Unidad 3 - Sentencias de Control
print ("Bienvenido al menu interactivo")
while True:
    opcion = input("¿Qué quieres hacer? Escribe una opción\n\t1) Saludar\n\t2) Sumar dos números\n\t3) Salir\n")
    if opcion == '1' :
        print ("Hola, espero que lo estés pasando bien.")
    elif opcion == '2':
        valor_a = int(input("Introduce el primer número: "))
        valor_b = int(input("Introduce el segundo número: "))
        print ("El resultado de la suma es: ",(valor_a+valor_b))
    elif opcion == '3':
        print ("¡Hasta luego! Ha sido un placer ayudarte.")
        break
    else:
       print ("Comando desconocido, vuelve a intentarlo.")


# Solicitar que se ingrese un arreglo de enteros y de la lista: al par multiplicar por 10 y al impar por 5. Presentar el nuevo arreglo.
lista_enteros = []
cadena_teclado_2 = input("Ingrese valores enteros a la lista separados por espacio: ")
lista_enteros = list(map(int, cadena_teclado_2.split()))
print ("La lista ingresada es ",lista_enteros)
indice=0
for lista in lista_enteros:
    if (lista%2==0):
        lista_enteros[indice] *= 10 
    else:
        lista_enteros[indice] *= 5
    print ("[{}]:[{}]".format(indice,lista_enteros[indice]))
    indice+=1

print ("Nueva lista: ",lista_enteros)