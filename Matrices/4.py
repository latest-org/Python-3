#-*-coding:utf-8-*-



'''Leer una matriz 4x3 entera y determinar en qué posiciones exactas se encuentran los
números primos'''
posicion = 0 
matrix = []
posiciones = []
try:
	for a in range(4):
		fila = []
		for b in range(3):
			numero = int(raw_input("Ingrese un numero: "))
			fila.append(numero)

		matrix.append(fila)



	for c in range(len(matrix)):
		for d in range(len(matrix[c])):
			numero= matrix[c][d]
			cont= 0 
			for h in range (1,numero+1):
				if numero%h==0:
					cont+=1
			if cont==2:
				posicion = c,d
				posiciones.append(posicion)

	print matrix
	print posiciones





except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"