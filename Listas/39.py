#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar si la semisuma entre el
valor mayor y el valor menor es un número par'''

try:

	lista=[]
	lista2=[]
	suma=0

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	menor=lista[0]
	
	for b in range(len(lista)):
		if lista[b]<menor:
			menor=lista[b]

	mayor=lista[0]

	for c in range(len(lista)):
		if lista[c]>mayor:
			mayor=lista[c]
		
	suma=mayor+menor

	if suma%2==0:
		print("La suma del mayor y menor es un numero par")

	else:
		print("La suma del mayor y menor No es un numero par")	


except ValueError:
	print("El valor digitado debe ser numerico")