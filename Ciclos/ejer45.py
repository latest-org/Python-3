#-*-coding:utf-8-*-

'''Leer un número y calcularle el factorial a todos los enteros comprendidos entre 1 y el
número leído'''

try:
	numero=int(input("Digite un numero entero: "))

	var=1

	print("Los factoriales entre 1 y el numero leido son:")	

	for a in range (1, numero+1 ):
		var = var * a
		print "%d"%var		
	
except ValueError:
	print("El valor digitado debe ser numerico")		