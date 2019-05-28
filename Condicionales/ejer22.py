#-*-coding:utf-8-*-


''' Leer un número entero de tres dígitos y determinar si el primer dígito es igual al último'''



try: 
	numero = int(raw_input("Digite un numero de tres digitos :"))
	digito1 = numero/100
	digito2 = (numero%100) /10
	digito3 = numero%10


	if numero<=999 and numero>99:


		if  digito1 == digito3: 
			print "el primer digito si es igual a el ultimo digito"

		else:
			print "El numero no tiene numeros iguales"


	else:
		print "El numero debe ser de tres digitos"





except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"