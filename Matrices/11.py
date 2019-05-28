#-*-coding:utf-8-*-


''' Leer una matriz 5x3 entera y determinar en qué 
columna está el menor número par.'''




matrix= []
primo = []
pos = []
pares = []
try:
	for a in range(5):
		lista =[]
		for b in range(3):
			numero = int(raw_input("Ingrese un numero; "))
			lista.append(numero)

		matrix.append(lista)
	menor = matrix [0]

	for c in range(len(matrix)):
		for d in range(len(matrix[c])):
			numero = matrix[c][d]
			if numero%2==0:
				pares.append(numero)

	for m in range(len(matrix)):
		if pares[m]< menor:
			menor=pares [m]

	for h in range(len(matrix)):
		for l in range(len(matrix[h])):
			numero = matrix[h][l]
			if menor == numero:
				pos.append(l)


	print matrix
	print pares 
	print menor 
	print pos


except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"
