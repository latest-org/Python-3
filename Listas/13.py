#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar si el promedio entero de estos datos está almacenado en la lista'''

try:
	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	suma=0
	promedio=0	
	for b in range(len(lista)):
		suma+=lista[b]
		promedio=suma//10

	print("El promedio de la lista es:",promedio)		
	
	aumento=0	
	for c in range(len(lista)):
		if lista[c]==promedio:
			aumento+=1


	if aumento>0:
		print("Y ese promedio esta dentro de la lista")

	else:
		print("Y  ese promedio no esta dentro de la lista")

except ValueError:
	print("El valor digitado debe ser numerico")					