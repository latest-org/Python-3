#-*-coding:utf-8-*-



'''Leer una matriz 4x3 entera, calcular la suma de los elementos de cada fila y determinar
cuál es la fila que tiene la mayor suma.'''



mayor = 0
pos = 0
matrix = []
try: 
	for a in range (4):
		fila = []
		for b in range(3):
			numero = int(raw_input("Ingrese un numero entero; "))
			fila.append(numero)


		matrix.append(fila)

	sumas = []
	for c in range(len(matrix)):
		suma = 0 
		for d in range(len(matrix[c])):
			numero = matrix[c][d]
			suma +=numero

		sumas.append(suma)

	for e in range(len(sumas)):
		if sumas[e]>mayor:
			mayor = sumas[e]
			pos = e
			
	print matrix
	print sumas
	print "%d"%pos

except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"