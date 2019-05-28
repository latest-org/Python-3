#-*-coding:utf-8-*-

''' Leer un numero entero y determinar si es un numero terminado en 4'''


try:
	numero = int(raw_input("Digite un numero entero: "))

	resultado = numero%10

	if resultado == 4:
		print "El ultimo digito es 4"


	else:
		print "El valor ingresado es diferente a 4"



except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"