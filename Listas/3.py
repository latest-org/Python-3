#-*-coding:utf-8-*-

'''Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está el mayor número primo leído'''

try:

	lista=[]
	lista2=[]
	lista3=[]

	for i in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		primo=lista[b]
		contador=0

		for c in range(1,primo+1):
			if (primo%c)==0:
				contador+=1

		if contador==2:
			lista2.append(primo)	


	mayor=lista2[0]

	for d in range(len(lista2)):
		if lista[d]>mayor:
			mayor=lista[d]

	aumento=0		
	for e in range(len(lista)):
		if lista[e]==mayor:
			lista3.append(e) 
			aumento+=1

	if aumento>1:
		print("El mayor numero primo esta en las posiciones: ",lista3)

	if aumento==1:
		print("El mayor numero primo esta en la posicion: ",lista3)					

	

except ValueError:
	print("El valor digitado debe ser numerico")				 	