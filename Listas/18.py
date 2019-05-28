#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones están
los números positivos'''

try:
	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	aumento=0	
	for b in range(len(lista)):
		if lista[b]>0:
			aumento+=1
			lista2.append(b)

	if aumento>0:		
		print("Los numeros positivos estan en las posiciones: ",lista2)
	
	else:
		print("No hay numeros positivos en la lista")
except ValueError:
	print("El valor digitado debe ser numerico")				