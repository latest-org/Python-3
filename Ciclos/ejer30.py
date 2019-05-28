#-*-coding:utf-8-*-



''' Leer un número entero y mostrar todos sus componentes numéricos o sea aquellos para quienes él sea un múltiplo'''



try: 

	numero = int(raw_input("Ingrese un numero: "))
	print "Los componentes numericos del %d"%numero + " son "

	for a in range (1, numero+1):
		if numero% a ==0:
			print "%d"%a
			print "\n"


except ValueError:
	print "La cantiad ingresada debe ser un valor numerico"
