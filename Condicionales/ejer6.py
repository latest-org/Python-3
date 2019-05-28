#-*-coding:utf-8-*-

''' Leer un numero entero de dos digitos menor que 20 y determinar si es primo'''

try:
	 numero = int(raw_input("Ingrese un numero de dos digitos menor que 20: "))

	 if numero>=10 and numero<20:

	 	if (numero==11) or (numero==13) or (numero==17) or (numero==19):
	 		print "El numero es primo"

	 	else:
	 		print "el numero no es primo"

	 else:
	 	print "el numero ingresado no tiene 2 digitos menores que 20"



except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"