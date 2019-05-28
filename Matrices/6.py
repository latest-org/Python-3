#-*-coding:utf-8-*-


'''Leer una matriz 4x4 entera y calcular el promedio de los números mayores de cada fila.'''




matrix = []
suma = 0
promedio = 0 

try:
	for a in range(4):
		fila = []
		for b in range(4):
			numero = int(raw_input(	"ingrese un numero entero:"))
			fila.append(numero)

		matrix.append(fila)


	for c in range(len(matrix)):
		mayor = 0 
		for d in range(len(matrix)):
			numero=matrix[c][d]
			if numero > mayor:
				mayor = numero

		suma += mayor
		promedio = suma /4

		

	print promedio
	print matrix 
	print "%d"%suma



except ValueError:
	print "la cantidad ingresada debe ser un valor numerico"
