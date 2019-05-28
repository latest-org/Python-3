#-*-coding:utf-8-*-


'''leer una matriz 4x4 entera y determinar 
en que fila y en que columna se encuentra el numero mayor'''

poscicion = 0 
matrix= []
mayor = 0
try:

	for a in range (4):
		fila = []
		for b in range (4):
			numero = int(raw_input("Ingrese un numero entero: "))
			fila.append(numero)

		matrix.append(fila)

	for c in range(len(matrix)): 
		for d in range (len(matrix)):
			numero = matrix [c][d]
			if numero >mayor:
				mayor = numero
				posicion = (c,d)


	print "%d"%mayor

	print poscicion


except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"