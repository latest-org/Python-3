#-*-coding:utf-8-*-



'''Leer un número entero menor que mil y determinar cuántos dígitos tiene'''


try:
	numero = int(raw_input("Digite un numero menor que mil: "))


	if numero >0 and numero <=1000:

		if numero<10:
			print "el numero ingresado tiene 1 digito"

		elif numero>=10 and numero <=99:
			print "el numero ingresado tiene 2 digitos"

		elif numero>=100 and numero <=999:
			print "el numero ingresado tiene 3 digitos"


		else:
			print "la cantidad ingresada debe ser un valor numerico"


	else: 
		print "el numero debe ser menor que mil"




except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"
