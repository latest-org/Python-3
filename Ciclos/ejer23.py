#-*-coding:utf-8-*-



'''Leer un número entero y determinar
si la suma de sus dígitos es también un número primo.'''


try:
	numero= int(raw_input("ingrese un numero: "))
	contador=0 
	digito=0
	suma=0

	while numero>0:
		digito = numero %10
		suma = suma + digito
		numero = numero /10

	print "La suma de los digitos es igual a " "%d"%suma


	for a in range (1,suma+1):
		if (suma%a)==0:
			contador=contador+1

	if contador==2:
		print "El numero es primo"

	else:
		print "el numero no es primo"
		



except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"






