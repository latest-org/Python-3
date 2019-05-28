#-*-coding:utf-8-*-



'''Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos'''


try: 
	numero1 = int(raw_input("Digite un numero entero de dos digitos :"))
	numero2 = int(raw_input("Digite otro numero entero de dos digitos :"))
	digito1 = numero1/10 	
	digito2 = numero1%10
	digito_1 = numero2/10
	digito_2 = numero2%10
	resultado = digito1 + digito2 + digito_1 + digito_2

	if numero1>9 and numero1<=99 and numero2>9 and numero2<=99:

		if  digito1 + digito2 + digito_1 + digito_2:
			print "La suma de todos los digitos es  %d"%resultado



	else: 
		print "los numeros deben ser de dos digitos "




except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"