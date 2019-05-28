#-*-coding:utf-8-*-

''' Mostrar en pantalla la tabla 
de multiplicar del número 5. '''


try:

	for a in range (1,50+1):
		if a%5==0:
			print "%d"%a


except ValueError:
	print "La cantidad ingresada debe sser un valor numerico"