#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición está el
número cuya suma de dígitos sea la mayor'''

try:

	lista=[]
	lista2=[]
	lista3=[]

	for a in range(3):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		numero=lista[b]
		contador=0
		suma=0

		while numero>0:
			digito=numero%10
			suma+=digito
			numero=numero//10
		lista2.append(suma)
		
		mayor=lista2[0]

		for c in range(len(lista2)):
			if lista[c]>mayor:
				mayor==lista[c]

		for d in range(len(lista)):
			if lista[d]==mayor:
				lista3.append(d)

	print(lista3)			




except ValueError:
	print("El valor digitado debe ser numerico")