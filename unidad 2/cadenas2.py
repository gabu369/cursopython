#Ejercicios 2 Cadenas

cadena_1 = input("Ingrese la primera cadena: ")
cadena_2 = input("Ingrese la segunda cadena: ")
print ("Las cadenas ingresadas son {}, {}\n".format(cadena_1,cadena_2))
cadena_final=cadena_1+cadena_2
operacion=input(("Seleccione una operacion a realizar\n1.{}\n2.{}\n3.{}\n4.{}\n5.{}\n6.{}\n7.{}\n8.{}\n9.{}\n10.{}\n>>>>".format("Len","min(c)","max(c)","uper()","lower()","title","split","replace","count","join")))
print ("La operacion es ",operacion)
print (len(cadena_final)) if operacion=='1' else None
print (min(cadena_final)) if operacion=='2' else None
print (max(cadena_final)) if operacion=='3' else None
print ((cadena_final).upper()) if operacion=='4' else None 
print ((cadena_final).lower()) if operacion=='5' else None
print ((cadena_final).title()) if operacion=='6' else None
print ((cadena_final).split('a')) if operacion=='7' else None
print ((cadena_final).replace('a','1')) if operacion=='8' else None
print ((cadena_final).count('a')) if operacion=='9' else None
print (cadena_1.join(cadena_2)) if operacion=='10' else None
