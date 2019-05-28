#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar si existe al menos un
número repetido'''

try:

	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		lista2.append(lista)

	aumento=0	
	for c in range(len(lista2)):
		if lista2[c]==lista2:
			aumento+=1
			print(lista[c])

	print(aumento)				

except ValueError:
	print("El valor digitado debe ser numerico")