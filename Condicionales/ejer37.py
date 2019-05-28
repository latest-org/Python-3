#-*-coding:utf-8-*-



''' Leer dos números enteros y determinar cuál es múltiplo de cuál'''

try:
	numero1 = int(raw_input("Digite un numero entero: "))
	numero2 = int(raw_input("Digite un numero entero: "))

	if numero1%numero2==0:
		print "El primer numero es multiplo del segundo"

	elif numero2%numero1==0:
		print "El Segundo numero es multiplo del primero"

	else:
		print "Los numero no son multiplos entre si"




except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"