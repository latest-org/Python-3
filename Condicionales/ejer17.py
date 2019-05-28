#-*-coding:utf-8-*-


'''Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito'''


try:
	numero = int(raw_input(" Ingrese un numero entero de tres digitos :"))
	digito1 = numero/100
	digito2 = (numero%100) /10
	digito3 = numero%10

	if numero>99 and numero<=999:


		if digito1>digito2 and digito1>digito3:
			print "El mayor digito esta en la primera poscicion "

		elif digito2>digito1 and digito2>digito3:
			print "El mayor digito esta en la segunda posicion "

		elif digito3>digito1 and digito3>digito2:
			print " el mayor digito esta en la tercera posicion"

		elif digito1==digito2==digito3:
			print "los 3 digitos son iguales"



	else:
		print "el numero ingresado debe tener 3 digitos"






except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"	