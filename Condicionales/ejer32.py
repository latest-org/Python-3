 #-*-coding:utf-8-*-


''' Leer un número entero y determinar si es múltiplo de 7'''



try:
	 numero = int(raw_input("Digite un numero entero: "))



	 if numero%7==0: 
	 	print "el numero ingresado es multiplo de 7"


	 else:
	 	print "el numero ingresado no es multiplo de 7"






except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"
