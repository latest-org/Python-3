#-*-coding:utf-8-*-
'''leer un numero entero de dos digitos y determinar si es primo y ademas si es negativo'''


try:
	numero = int(raw_input("Digite un entero de dos digitos numero: "))

	if numero > 9 and numero <= 99 or numero < -9 and numero >= -99: 
		digito1 = numero %2
		digito2 = numero %3
		resultado = numero/numero 


		if digito1 != 0 and digito2 !=0 and resultado == 1 and numero < 0:
			print "el numero %d"%  " es un numero negativo"

		elif digito1 != 0 and digito2 !=0 and  resultado == 1 and numero > 0:
			print "el numero %d"%numero + " es un numero primo positivo"


		else: 
			print "el numero %d"%numero  + " no es un numero primo"




except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"