#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números
negativos hay.'''

try:
	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	aumento=0	
	for b in range(len(lista)):
		if lista[b]<0:
			aumento+=1

	if aumento>0:
		print("En la lista hay %d"%aumento + " numeros negativos")

	else:
		print("En la lista no hay numeros negativos")

except ValueError:
	print("El valor digitado debe ser numerico")						