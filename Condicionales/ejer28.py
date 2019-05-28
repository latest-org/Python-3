 #-*-coding:utf-8-*-




'''Leer un número entero menor que 50 y positivo y determinar si 
es un número primo'''



try:
	numero = int(raw_input("Digite un numero menor que 50 pero mayor a 0 :"))

	if numero >0 and numero<50:

		if (numero==2) or (numero==3) or (numero==5) or (numero==7) or (numero==11) or (numero==13) or (numero==17) or (numero==19) or (numero==23) or (numero==29) or (numero==31) or (numero==37) or (numero==41) or (numero==43) or (numero==47):
			print "el numero es primo"


		else:
			print " el numero ingresado no es primo "

 

		

	else:
		print "El numero ingresado no esta en el rango requerido"




except ValueError:
	print "la cantidad ingresada debe ser un valor numerico"