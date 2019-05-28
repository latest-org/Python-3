#-*-coding:utf-8-*-





'''Leer una matriz 5x5 entera y determinar en qué fila está el mayor número terminado en
6.'''

matrix = []
mayor = 0 
seis= []
pos = []
try:
	for a in range(5):
		lista = []
		for b in range(5):
			numero = int(raw_input("Ingrese un numero; "))
			lista.append(numero)
			
		matrix.append(lista)


	for c in range(len(matrix)):
		for d in range(len(matrix[c])):
			numero = matrix [c][d]
			if numero%10==6:
				seis.append(numero)


	for h in range(len(seis)):
		if seis[h]>mayor:
			mayor = seis[h]
	
	for k in range(len(matrix)):
		for l in range(len(matrix[k])):
			numero = matrix [k][l]
			if mayor == numero:
				pos.append(k)
				

	
	print matrix 
	print "\n"
	print seis
	print "%d"%mayor
	print pos





except ValueError:
	print "la cantidad ingresada debe ser un valor numerico"
