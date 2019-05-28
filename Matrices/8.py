#-*-coding:utf-8-*-



'''eer una matriz 4x4 entera y determinar cuántos enteros terminados en 0 hay
almacenados en ella'''


cont = 0
matrix = []
try:
	for a in range(4):
		lista =[]
		for b in range(4):
			numero = int(raw_input("Ingrese un numero; "))
			lista.append(numero)

		matrix.append(lista)

	for c in range(len(matrix)):
		
		for d in range(len(matrix)):
			numero = matrix[c][d]
			if numero%10==0:
				cont+=1

				
	print "%d"%cont
	print matrix
	

except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"