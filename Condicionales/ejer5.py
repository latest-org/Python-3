#-*-coding:utf-8-*-

''' leer un numero entero de 2 digitos y determinar si ambos digitos son pares'''



try:
	numero = int(raw_input("Digite un numero de dos digitos: "))

	if numero>= 10 and numero <=99:
		digito1 = numero/ 10
		digito2 = numero% 10 

	if digito1%2 ==0 and digito2%2 ==0:
		print "el numero es par"



	else: 
		print "el numero no es par"



except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"