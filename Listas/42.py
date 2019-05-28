#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números con
cantidad par de dígitos pares hay almacenados en dicha lista'''

try:
	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		numero=lista[b]

		l1=1
		l2=10

		while numero>=l2:
			l1+=1
			l2=l2*10
		lista2.append(l1)	

	aumento=0	
	for c in range(len(lista2)):
		if lista2[c]%2==0:
			aumento+=1

	if aumento>0:		
		print("hay %d"%aumento + " numeros con cantidad par de digitos")					

except ValueError:
	print("El valor digitado debe ser numerico")	