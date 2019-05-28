#-*-coding:utf-8-*-



'''Leer un número entero y determinar a cuánto 
es igual la suma de sus dígitos'''


try:
	numero= int(raw_input("ingrese un numero: "))
	contador=0 
	digito=0
	suma=0

	while numero>0:
		digito = numero %10
		numero = numero /10
		suma = suma + digito
		

	print "La suma de los digitos es igual a " "%d"%suma


	



except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"