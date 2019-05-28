#-*-coding:utf-8-*-



'''Leer una matriz 4x4 entera y determinar en qué posiciones están los enteros terminados
en 0.'''


posiciones =[]
matrix = []
posicion= 0 
try:
	for a in range(4):
		lista =[]
		for b in range(4):
			numero = int(raw_input("Ingrese un numero entero: "))
			lista.append(numero)

		matrix.append(lista)
	for c in range(len(matrix)):
		
		for d in range(len(matrix)):
			numero = matrix[c][d]
			if numero%10==0:
				posicion = (c,d)
				posiciones.append(posicion)
	print matrix
	print posiciones


except ValueError:
	"La cantidad ingresada debe ser un valor numerico"