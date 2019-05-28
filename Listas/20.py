#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición está el
menor número primo'''

try:

	lista=[]
	lista2=[]
	lista3=[]

	for a in range(10):
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

	menor=lista2[0]
			
	for d in range(len(lista2)):
		if lista[d]<menor:
			menor=lista2[d]

	aumento=0		
	for e in range(len(lista)):
		if lista[e]==menor:
			lista3.append(e)
			aumento+=1

	if aumento==1:
		print("El numero primo menor esta en la posicion: ",lista3)

	if aumento>1:
		print("El numero primo menor esta en las posiciones: ",lista3)
					
	


except ValueError:
	print("El valor digitado debe ser numerico")