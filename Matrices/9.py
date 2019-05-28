#-*-coding:utf-8-*-



'''Leer una matriz 3x4 entera y determinar cuántos de los números almacenados son primos
y terminan en 3. '''


primo =[]
matrix = []
cont1= 0 
try:
	for a in range(3):
		lista = []
		for b in range(4):
			numero = int(raw_input("Ingrese un numero entero: "))
			lista.append(numero)

		matrix.append(lista)

	for c in range(len(matrix)):
		for d in range(len(matrix[c])):
			numero = matrix[c][d]
			cont = 0 
			for h in range(1,numero+1):
				if numero%h==0:
					cont+=1

			if cont ==2:
				primo.append(numero)

	for n in range(len(primo)):
		var = primo[n]
		if var%10==3:
			cont1+=1
	print matrix
	print primo
	print "%d"%cont1




except ValueError:
	print "la cantidad ingresada debe ser un valor numerico"