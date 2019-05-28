#-*-coding:utf-8-*-

'''leer un numero entero de dos digitos y determinar si un digito es multiplo del otro'''



try:
	numero= int(raw_input("Ingrese un numero entero de dos digitos: "))
	digito1 = numero / 10
	digito2 = numero % 10 
	numero1 = digito1%digito2
	numero2 = digito2%digito1

	if numero>9 and numero<=99:

		if numero1 == 0:
			print "El digito uno es multplo del numero 2   "
		
		elif numero2 == 0: 
			print "El digito dos es multiplo del numero 1" 

		elif numero1 !=0 and numero2 !=0:
			print "ninguno de los digitos es multiplos"


		else: 
			print "el numero debe ser de dos digitos"

	



except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"
