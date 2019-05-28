#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar
cuántos números de los almacenados en la lista terminan en el mismo dígito que el último
valor leído'''

try:

	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero que sera almacenado en la lista: "))
		lista.append(numeros)

	print(" ")
	leido=int(input("Digite un numero que sera comparado con la lista: "))	


	aumento=0
	for b in range(len(lista)):
		if lista[b]%10==leido%10:
			aumento+=1
		
	if aumento>0:	
		print("Hay %d"%aumento + " numeros de la lista que terminan en el mismo digito que el numero")		

	else:
		print("No hay numeros de la lista que terminen en el mismo digito que el numero")	
		
except ValueError:
	print("El valor digitado debe ser numerico")