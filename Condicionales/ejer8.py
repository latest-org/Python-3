#-*-coding:utf-8-*-


''' Leer un numero entero de dos digitos y determinar si sus 2 digitos son primos'''



try: 
	numero=int(raw_input("Digite un numero entero de dos digitos: "))

	
	if numero>=10 and numero<=99:
		
		digito1 = numero / 10
		digito2 = numero%10 


		division2_digito1 = digito1 % 2
		division_digito1 = digito1 / digito1


		division2_digito2 = digito1 % 2
		division_digito2 = digito2 / digito2

	

		if  division2_digito1!=0 and division_digito1== 1:            
			print "el primer digito es primo"
		else: 
			print "el primer digito no es primo"

		if division2_digito2 !=0 and division2_digito2==1:
			print "el segundo digito es primo"
		else:
			print "el segundo digito no es primo"

	else:
		print "el numero ingresado no es de 2 digitos"







except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"