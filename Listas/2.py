#-*-coding:utf-8-*-

'''Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está el mayor número par leído'''

try:

	lista=[]
	lista2=[]
	lista3=[]

	for i in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)


	for l in range(len(lista)):
		if lista[l]%2==0:
			lista2.append(lista[l])

		
	mayor=lista2[0]

	for n in range(len(lista2)):
		if lista[n]>mayor:
			mayor=lista[n]
	
	aumento=1
	for a in range(len(lista)):
		if lista[a]==mayor:
			lista3.append(a-1)
			aumento+=1

	if aumento>1:		
		print("El numero par mayor esta en las posiciones: ",lista3)

	if aumento==1:
		print("El numero par mayor esta en la posicion: ",lista3)		

	



	
except ValueError:
	print("El valor digitado debe ser numerico")								