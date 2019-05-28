#-*-coding:utf-8-*-


'''Leer un número entero de dos dígitos, guardar cada dígito en una variable diferente y luego mostrarlas en pantalla'''


try:
	numero = int(raw_input("Digite un numero de dos digitos: "))
	if numero>9 and numero<=99:
		digito1 = numero/10
		digito2 = numero%10

		print "%d"%digito1
		print "%d"%digito2

	else:
		print "el numero ingresado debe ser de 2 digitos"






except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"