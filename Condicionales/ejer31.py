 #-*-coding:utf-8-*-





'''Leer un número entero y determina si es igual a 10'''

try:
	numero = int(raw_input("Digite un numero entero :"))


	if numero==10:
		print "el numero ingresado es igual a 10"



	else:
		print " el numero ingresado no es igual a 10"



except ValueError:
	print "la cantidad ingresada debe ser un valor numerico"