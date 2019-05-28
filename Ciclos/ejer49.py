#-*-coding:utf-8-*-

'''Generar los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1'''

try:

	cont = 0 
	for i in range(10,0,-1):
		cont += 1
		print cont

except ValueError:
	print("El valor digitado debe ser numerico")		