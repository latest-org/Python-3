#-*-coding:utf-8-*-


'''Leer una matriz 4x4 entera y determinar cuántas veces se repita en ella el número mayor.'''

cont =0
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
			
				
	for c in range(len(matrix)): 
		for d in range (len(matrix)):
			numero = matrix [c][d]
			if numero==mayor:
				cont +=1

	print "%d"%mayor

	print "%d"%cont


except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"