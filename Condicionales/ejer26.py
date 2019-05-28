 #-*-coding:utf-8-*-



'''Leer un número entero de cuatro dígitos y determinar a cuanto es igual la suma de sus dígitos'''


try:


	numero = int(raw_input("Digite un numero de cuatro digitos :"))
	digito1 = numero/1000
	digito2 = (numero%1000)/100
	digito3 = (numero%100) /10
	digito4 = numero%10
	print "%d"%digito1
	print "%d"%digito2
	print "%d"%digito3
	print "%d"%digito4
	resultado = digito1 + digito2 + digito3 + digito4

	if digito1 + digito2 + digito3 + digito4:
		print "la suma de los digitos es igual a %d"%resultado


	else:
		print "los caracteres ingresado no son numeros"

	





except ValueError:
	print "la cantidad ingresada debe ser un valor numerico"