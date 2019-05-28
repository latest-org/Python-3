 #-*-coding:utf-8-*-


'''Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al penúltimo'''


try:
	numero = int(raw_input("Digite un numero de cuatro digitos :"))

	if numero<=9999 and numero>999:
		digito1 = numero/1000
		digito2 = (numero% 1000) /100
		digito3 = numero%100 /10
		digito4 = numero%10


		print "%d"%digito1
		print "%d"%digito2
		print "%d"%digito3
		print "%d"%digito4


		if digito2== digito3:
			print "El digito 2 y el digito 3 son iguales "



		else:
			print " El numero ingresado no tiene digitos iguales"

	else:
		print "El numero ingresado debe tener 4 digitos"







except ValueError:
	print "la cantidad ingresada debe ser un valor numerico"