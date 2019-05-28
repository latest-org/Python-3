#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántas veces en la lista
se encuentra el dígito 2. No se olvide que el dígito 2 puede estar varias veces en un mismo
número'''

try:

	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		numero=lista[b]
		aumento=0

		while numero>0:
			digito=numero%10
			if digito==2:
				lista2.append(digito)
			numero=numero//10
			
	for c in range(len(lista2)):
		aumento+=1

	if aumento>0:	
		print("Hay %d"%aumento + " digitos 2 en toda la lista")
	
	else:
		print("No hay digitos 2 en la lista")	



except ValueError:
	print("El valor digitado debe ser numerico")