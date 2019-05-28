#-*-coding:utf-8-*-



'''escribir en panntalla el resultado de sumar los primeros 20 multiplos de 3'''



try:
	cont=0
	suma=0

	for a in range (1,63):
		if a%3==0:
			cont=1
			suma = suma+a

		if cont == 20:
			break

		

	print "la suma de los primeros 20 multiplos de 3 es: %d"%suma 




except ValueError:
	print " La cantidad ingresada deber ser un valor numerico "