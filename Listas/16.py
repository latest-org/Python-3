#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuáles son los datos
almacenados múltiplos de 3'''

try:
	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	aumento=0	
	for b in range(len(lista)):
		if lista[b]%3==0:
			aumento+=1
			lista2.append(lista[b])

	if aumento>0:		
		print("Los numeros multiplos de 3 son: ",lista2)

	else:
		print("No hay numeros multiplos de 3")

except ValueError:
	print("El valor digitado debe ser numerico")						