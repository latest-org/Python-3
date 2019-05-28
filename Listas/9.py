#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántas veces está repetido el mayor'''

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

	aumento=0		
	for c in range(len(lista)):
		if lista[c]==mayor:
			aumento+=1
			lista2.append(aumento)

	print("El numero mayor se repite:" + "%d"%aumento + " veces")


except ValueError:
	print("El valor digitado debe ser numerico")							