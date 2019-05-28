#-*-coding:utf-8-*-




'''Leer un número entero y determinar cuántas veces tiene el dígito 1'''



try:
	numero = int(raw_input("ingrese un numero: "))
	cont=0 

	while numero>0:
		digito = numero%10
		numero = numero/10
		
	
		if digito ==1:
			cont +=1

	print "%d"%cont



except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"