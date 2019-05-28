#-*-coding:utf-8-*-

'''Leer dos números enteros y determinar
si la diferencia entre los dos es un número par'''




try:
	numero1 = int(raw_input("Digite un numero entero: "))
	numero2 = int(raw_input("Digite un numero entero: "))
	diferencia1 = numero1 - numero2
	diferencia2 = numero2 - numero1


	if diferencia1%2==0:
		print "la diferencia es un numero par"

		if diferencia2%2==0:
			print "la diferencia es un numero par"

	else:
		print "la diferencia no es un numero par"




except ValueError:
	print "la cantdad ingresada debe ser un valor numerico"

