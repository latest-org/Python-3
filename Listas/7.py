#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentra el número mayor'''

try:

	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	
	mayor=lista[0]

	for b in range(len(lista)):
		if lista[b]>mayor:
			mayor=lista[b]

	for c in range(len(lista)):
		if lista[c]==mayor:
			lista2.append(c)

	print("El numero mayor se encuentra en las posiciones: ",lista2)
	
except ValueError:
	print("El valor digitado debe ser numerico")						