#-*-coding:utf-8-*-


''' Leer un numero entero de dos digitos y determinar a cuanto es igual la suma de sus digitos'''


try:
	 numero = int(raw_input("Digite un numero de dos digitos: "))

	 if numero >= 10 and numero<=99:

		 digito1 = numero %10
		 digito2 = numero /10 
		 resultado = digito1 + digito2
		 print "la suma de los 2 digitos es %d"%resultado


	 else:
	 	print "el numero digitado no tiene 2 digitos"





except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"