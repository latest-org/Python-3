#-*-coding:utf-8-*-




''' Leer un número entero y determinar cuál es el mayor de sus dígitos'''



try:
	numero = int(raw_input("Ingrese un numero: "))
	mayor = 0 

	while numero>0:
		digito = numero%10
		numero = numero/10

		if mayor<digito:
			mayor = digito
	print "%d"%mayor 
	




except ValueError:
	print "la cantidad ingresada debe ser un valor numerico"