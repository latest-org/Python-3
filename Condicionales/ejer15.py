#-*-coding:utf-8-*-


'''Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus dígitos'''

try:
	 numero = int(raw_input("Digite un numero entero de tres digitos :"))
	 digito1 = numero/100
	 digito2 = (numero%100) / 10
	 digito3 = numero%10
	 resultado = digito1 + digito2 + digito3

	 print "1: %d"%digito1
	 print "2: %d"%digito2
	 print "3: %d"%digito3


	 if numero>99 and numero<=999:


	 	if digito1 + digito2 + digito3:
	 		print " la suma de los 3 digitos es de %d"%resultado




	 else: 
	 	print "El numero debe ser de 3 digitos "





except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"