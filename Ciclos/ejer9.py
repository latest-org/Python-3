#-*-coding:utf-8-*-

''' mostrar en pantalla todos los numeros terminados en 6 y comprendidos entre 25 y 205'''
try:



	for a in range (25,205+1):
		if a%10==6:
			print "%d"%a


except ValueError:
	print "a"
