 #-*-coding:utf-8-*-


'''Leer un número entero de cuatro dígitos y determinar cuántos dígitos
pares tiene '''



try:
	numero = int(raw_input("Digite un numero de cuatro digitos :"))

	if numero >999 and numero<=9999:
		digito1 = numero/1000 
		digito2 = (numero%1000) /100
		digito3 = numero%100 /10
		digito4 = numero%10


		if digito1%2==0 and digito2%2==0 and digito3%2==0 and digito4%2==0:
			print "Todos los digitos son pares"

		elif digito1%2==0 and digito2%2==0 and digito3%2!=0 and digito4%2==0:
			print "El digito 1, El digito2, Y el digito 4 son pares"

		elif digito1%2==0 and digito2%2==0 and digito3%2==0 and digito4%2!=0:
			print "el digito 1, el digito 2 Y el digito 3 son pares"

		elif digito1%2!=0 and digito2%2==0 and digito3%2==0 and digito4%2==0:
			print "El digito 2, el digito 3 y el digito 4 son pares"

		elif digito1%2==0 and digito2%2!=0 and digito3%2==0 and digito4%2==0:
			print "EL digito 1, el digito 3 y el digito 4 son pares"

		elif digito1%2!=0 and digito2%2==0 and digito3%2!=0 and digito4%2==0:
			print " El digito 2 y el digito 4 son pares"

		elif digito1%2==0 and digito2%2!=0 and digito3%2==0 and digito4%2!=0:
			print " El digito 1 y el Digito 3 son pares"

		elif digito1
		%2==0 and digito2%2==0 and digito3%2!=0 and digito4%2!=0:
			print "el digito 1 y el digito 2 son pares "

		elif digito1%2!=0 and digito2%2==0 and digito3%2==0 and digito4%2!=0:
			print " el digito 2 y el digito 3 son pares"

		elif digito1%2==0 and digito2%2!=0 and digito3%2!=0 and digito4%2==0:
			print " el digito 1 y el digito 4 son pares"

		elif digito1%2==0 and digito2%2!=0 and digito3%2!=0 and digito4%2!=0:
			print  "Solo el digito 1 es par"

		elif digito1%2!=0 and digito2%2==0 and digito3%2!=0 and digito4%2!=0:
			print " Solo el digito 2 es par "

		elif digito1%2!=0 and digito2%2!=0 and digito3%2==0 and digito4%2!=0:
			print "Solo el digito 3 es par"

		elif digito1%2!=0 and digito2%2!=0 and digito3%2!=0 and digito4%2==0:
			print "Solo el digito 4 es par"





		else:
			print "Ningun digito es par"






	else:
		print "El numero debe tener 4 digitos"



except ValueError:
	print "El valor ingresado debe ser un valor numerico"