#-*-coding:utf-8-*-

''' Leer un numero entero y mostrar todos los pares comprendidos entre el 1 y el numero leido'''


try:
	numero = int(raw_input("Ingrese un numero: "))



	for a in range (1,numero+1):
		if a%2==0:
			print "%d"%a




except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"