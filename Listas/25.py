#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos de los números
leídos son números primos terminados en 3'''

try:

	lista=[]
	lista2=[]
	lista3=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		primo=lista[b]
		aumento=0

		for c in range(1,primo+1):
			if (primo%c)==0:
				aumento+=1

		if aumento==2:
			lista2.append(primo)

	aumento2=0
	for d in range(len(lista2)):
		if lista2[d]%10==3:
			aumento2+=1

	if aumento2>0:		
		print("Hay %d"%aumento2 + " numeros primos terminados en 3")						

	if aumento2==0:
		print("No hay numeros primos terminados en 3")

except ValueError:
	print("El valor digitado debe ser numerico")