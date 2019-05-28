#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números tienen, de los almacenados allí, menos de 3 dígitos'''

try:
	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	aumento=0	
	for b in range(len(lista)):
		if lista[b]<100:
			aumento+=1
			lista2.append(lista[b])

	print("Hay %d"%aumento + " numeros menores de 3 digitos")
	print("Y son los siguientes: ",lista2)		
except ValueError:
	print("El valor digitado debe ser numerico")				