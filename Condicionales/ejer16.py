#-*-coding:utf-8-*-


'''Leer un número entero de tres dígitos y determinar si al menos dos de sus tres dígitos son Iguales'''


try:
	numero = int(raw_input("Ingrese un numero entero de 3 digitos :"))
	digito1 = numero /100
	digito2 = (numero%100) /10
	digito3 =  numero %10


	if numero>99 and numero<=999:


		if digito1 == digito2 and digito1 != digito3:
			print "El digito 1 y el digito 2 son iguales "

		elif digito2 == digito3 and digito2 != digito1:
			print "El digito 2 y el digito 3 son iguales "

		elif digito1 == digito3 != digito2:
			print " El digito 1 y el digito 3 son iguales "

		elif digito1 == digito2 == digito3:
			print " Los 3 digitos son iguales"

		elif digito1 != digito2 != digito3: 
			print "los 3 digitos son diferentes"



	else: 
		print "El numero debe ser de 3 digitos "






























except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"