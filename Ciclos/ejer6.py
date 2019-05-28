#-*-coding:utf-8-*-



''' leer un numero entero de tres digitos y mostrar todos los enteros comprendidos
entre 1 y cada uno de los digitos'''


try: 
	numero = int(raw_input("Ingrese un numero de tres digitos: "))
	if numero >=100 and numero <=999:
		digito1 = numero/100
		digito2 = (numero%100) /10
		digito3 = numero%10


		

		print "los numero comprendidos del primer digito son "  

		for a in range (1,digito1+1):
			
			print  "%d"%a
		print "\n"

		print "los numero comprendidos del segundo digito son "
		for b in range (1, digito2+1):
			  
			print  "%d"%b
		print "\n"


		for c in range (1, digito3+1):
			 
			print  "%d"%c
		print "\n"

	else:
		print "El numero ingresado debe ser de 3 digitos"



except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"

