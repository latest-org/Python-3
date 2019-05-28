 #-*-coding:utf-8-*-


'''Leer un número entero de tres dígitos y determinar si alguno de sus dígitos es igual a la suma de los otros dos'''


try:
	numero = int(raw_input("Digite un numero de tres digitos :"))
	digito1 = numero/100
	digito2 = (numero%100) /10
	digito3 = numero%10



	if numero>99 and numero<=999:


		if digito1== digito2 + digito3:
			print "la suma de el digito dos y el digito 3 es igual al digito 1"

		elif digito2== digito1 + digito3:
			print "la suma de el digito uno y el digito 3 es igual al digito 2"

		elif digito3== digito1 + digito2:
			print "La suma de el digito uno y el digito dos es igual al digito 3"


		else:
			print "El numero ingresado no cumple con lo requerido"


	else: 
		print "el numero debe ser de tres digitos"








except ValueError:
	print " La cantdad ingresada debe ser un valor numerico"


