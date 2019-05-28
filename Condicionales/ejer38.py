#-*-coding:utf-8-*-



'''Leer tres números enteros y determinar si el último dígito de los tres números es igual'''


try:
	numero1 = int(raw_input("Digite un numero entero: "))
	numero2 = int(raw_input("Digite un numero entero: "))
	numero3 = int(raw_input("Digite un numero entero: "))

	if numero1%10==numero2%10 and numero1%10==numero3%10:
		print "El ultimo digito de los 3 numeros ingresado son iguales"


	else:
		print "Los numeros ingresados no tienen los ultimos digitos iguales"



except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"


