#-*-coding:utf-8-*-


''' Leer un número entero y determinar si termina en 7'''




try:
	numero = int(raw_input("Digite un numero entero: "))


	if numero%10 == 7:
		print "El numero termina en 7"


	else:
		print "el numero no termina en 7"

except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"