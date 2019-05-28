#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuáles son los números
múltiplos de 5 y en qué posiciones están.'''

try:

	lista=[]
	lista2=[]
	lista3=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	aumento=0	
	for b in range(len(lista)):
		if lista[b]%5==0:
			aumento+=1
			lista2.append(b)
			lista3.append(lista[b])

	if aumento==1:
		print("El numero multiplo de 5 es: ",lista3)
		print("Y estan en la posicione: ",lista2)		

	if aumento>1:		
		print("Los numeros multiplos de 5 son: ",lista3)
		print("Y estan en las posiciones: ",lista2)
				
	if aumento==0:
		print("No hay numeros multiplos de 5 en la lista")		

except ValueError:
	print("El valor digitado debe ser numerico")