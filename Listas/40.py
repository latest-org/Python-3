#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista terminan en 15'''

try:
	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	aumento=0	
	for b in range(len(lista)):
		if lista[b]%100==15:
			aumento+=1	

	if aumento>0:		
		print("Hay %d"%aumento + " numeros que terminan en 15")		

	else:
		print("No hay numeros que terminen en 15")	
	

except ValueError:
	print("El valor digitado debe ser numerico")	