#-*-coding:utf-8-*-


'''Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está el mayor número leído'''

try:

	lista=[]
	lista2=[]

	for i in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	mayor=0

	for j in range(len(lista)):
		if lista[j]>mayor:
			mayor=lista[j]


	aumento=0		
	for q in range(len(lista)):
		if mayor==lista[q]:
			lista2.append(q)
			aumento+=1

	if aumento>1:		
		print("El numero mayor esta en las posiciones: ",lista2)

	if aumento==1:
		print("El numero mayor esta en la posicion: ",lista2)	


except ValueError:
	print("El valor digitado debe ser numerico")				  		