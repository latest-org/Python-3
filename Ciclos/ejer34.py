#-*-coding:utf-8-*-





'''Generar los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1'''


try:

	dif =9 

	for a in range (10,0,-1):
		operacion = a - dif
		print "%d"%operacion 
		dif +=-2


except ValueError:
	print "Error"