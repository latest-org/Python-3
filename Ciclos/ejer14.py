#-*-coding:utf-8-*-


''' mostrar en pantalla los primeros 20 multiplos de 3'''


try: 

	for a in range (1,63):
		if a%3==0:
			print "%d"%a



except ValueError:
	print "La cantidad ingresada debe ser un valor numerico "