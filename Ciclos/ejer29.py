#-*-coding:utf-8-*-




'''Leer un número entero y determinar a cuánto es igual el primero de sus dígitos.'''




try: 
	numero = int(raw_input("Ingrese un numero: "))
	cont =0

	while numero>0:
		for a in range (cont): 
			digito = numero%10

		numero = numero/10
		cont = cont +1

	print "%d"%digito





except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"