#-*-coding:utf-8-*-


'''Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes'''

try: 
	numero1 = int(raw_input("Digite un numero de dos digitos :"))
	numero2 = int(raw_input("Digite otro numero de dos digitos :"))

	
	if numero1>9 and numero1<=99 and numero2>9 and numero2<=99:
		digito1 = numero1 /10 
		digito2 = numero1 %10

		digito_1 = numero2 /10
		digito_2 = numero2 %10


		if digito1 == digito_1:
			print "El primer digito del numero 1 es igual al primer digito del numero 2 "

		elif digito1 == digito_2:
			print "El primer digito del numero 1 es igual al segundo digito del numero 2 "

		elif digito2 == digito_2:
			print " El segundo digito del numero 1 es igual al segundo digito del numero 2"

		elif digito2 == digito_1:
			print " El segudo digito del numero 1 es igual al primer digito del numero 2"

		else:
			print "No hay digitoos comunes"

	else: 	
		print "Los numeros deben ser de dos digitos"

	
		



except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"