#-*-coding:utf-8-*-

'''Leer una matriz 3x4 entera y determinar en qué posiciones exactas se encuentran los
números pares.'''

matrix = []
pos = 0 
matrix2 = []
try:
	for a in range (3):
		fila = []
		for b in range (4):
			numero = int(raw_input("Ingrese un numero entero: "))
			fila.append(numero)

		matrix.append(fila)
	posiciones = []
	for b in range (len(matrix)):
		for c in range(len(matrix[b])):
			numero = matrix[b][c]
			if numero%2==0:
				pos =b,c
				posiciones.append(pos)
				


	print matrix
	print posiciones

except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"