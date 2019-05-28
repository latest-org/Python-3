#-*-coding:utf-8-*-




'''Leer una matriz 5x3 entera y determinar en qué fila está el mayor número primo.'''



matrix = []
mayor = 0 
primos=[]
pos = 0 
try:
	for a in range(5):
		lista =[]
		for b in range(3):
			numero = int(raw_input("Ingrese un numero entero; "))
			lista.append(numero)

		matrix.append(lista)

	for c in range(len(matrix)):
		for d in range(len(matrix[c])):
			numero = matrix [c][d]
			cont = 0 
			for h in range(1,numero+1):
				if numero%h==0:
					cont+=1

			if cont==2:
				primos.append(numero)

	for e in range(len(primos)):
		if primos [e]>mayor:
			mayor = primos [e]

	for g in range(len(matrix)):
		for f in range(len(matrix[g])):
			numero = matrix [g][f]
			if mayor == numero:
				pos = g
		

	print matrix 
	print primos 
	print "%d"%pos

except ValueError:
	print "la cantidad ingresada debe ser un valo numerico"