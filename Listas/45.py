#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista comienzan por 34'''

try:
	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		numero=lista[b]

		while numero>0:
			digito=numero%10
			if numero==32:
				lista2.append(numero)
			numero=numero//10
			
	aumento=0		
	for c in range(len(lista2)):
		aumento+=1				

	if aumento>0:
		print("Hay %d"%aumento + " numeros que empiezan por 32")

	else:
		print("No hay numeros que empiezen por 32")		

except ValueError:
	print("El valor digitado debe ser numerico")	