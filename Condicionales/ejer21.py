#-*-coding:utf-8-*-


'''Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra el mayor dígito'''



try:
	numero1 = int(raw_input("Digite un numero de dos digitos :"))
	numero2 = int(raw_input("Digite otro numero de dos digitos :"))
	numero3 = int (raw_input("Digite un numero mas de dos digitos :"))

	if numero1 and numero2 and numero3 <=99 and numero1 and numero2 and numero3 >9:



		if numero1>numero2 and numero1>numero3:
			print "El primer numero ingresado es el mayor"

		elif numero2>numero1 and numero2>numero3:
			print "El segundo numero ingresado es el mayor"


		elif numero3>numero1 and numero3>numero2:
			print "El tercer numero ingresado es el mayor"




	else:
		print "el numero tiene que ser de dos digitos"







except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"