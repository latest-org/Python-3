#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y mostrar en pantalla todos los
enteros comprendidos entre 1 y cada uno de los números almacenados en la lista'''

try:

	lista=[]
	lista2=[]

	for a in range(2):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):	
		numero=lista[b]

		for c in range(1,numero):
			lista2.append(c)

		print(lista2)		


except ValueError:
	print("El valor digitado debe ser numerico")