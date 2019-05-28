#-*-coding:utf-8-*-


'''Leer dos números enteros de dos dígitos y determinar si la diferencia entre los dos es un número primo'''


try:
	numero1 = int(raw_input("Digite un numero de dos digitos: "))
	numero2 = int(raw_input("Digite un numero de dos digitos: "))
	diferencia1 = numero1 - numero2
	diferencia2 = numero2 - numero1

	if numero1>9 and numero1<=99 and numero2>=10 and numero2<=99:


		if diferencia1%2 >0:
			print "la diferencia es un numero primo"

		elif diferencia2%2 >0:
			print "la diferencia es un numero primo"


		else:
			print "la diferencia no es un numero primo"

	else:
		print "el numero digitado no esta en el rango requerido"




except ValueError:
	print "la cantdad ingresada debe ser un valor numerico"