#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar si la semisuma entre el
valor mayor y el valor menor es un número primo'''

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


	contador=0
	for d in range(1,suma+1):
		if (suma%d)==0:
			contador+=1

	if contador==2:
		print("La suma del menor y el mayor es un numero primo")

	else:
		print("La suma del menor y el mayor NO es un numero primo")			



except ValueError:
	print("El valor digitado debe ser numerico")