#-*-coding:utf-8-*-

''' leer un numero entero y mostrar los enteros comprendidos entre el 1 y el numero leido'''


try:
	numero = int(raw_input("Ingrese un numero: "))



	for a in range (1,numero+1):
		print "%d"%a


except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"