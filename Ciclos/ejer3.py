#-*-coding:utf-8-*-


'''leer un numero entero y mostrar todos los divisores exactos del numero comprendidos entre 1 y el numero leido'''


try:
	numero = int(raw_input("Ingrese un numero: "))



	for a in range (1,numero+1):
		


		if numero%a==0:
			print "%d"%a


		




except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"