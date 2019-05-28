#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos de los números
almacenados en dicha lista pertenecen a los 100 primeros elementos de la serie de Fibonacci'''

try:

	lista=[]
	lista2=[]
	lista3=[]
	lista4=[]

	for l in range(10):
		leido=int(input("Digite un numero entero: "))
		lista.append(leido)	


	numero1=1
	numero2=1
	numero3=0


	for i in range(0,30):
		numero3=numero2
		numero2=numero1
		numero1=numero2+numero3
		lista2.append(numero1)	

	
	for n in range(len(lista)):
		comparacion=lista[n]

		for h in range(len(lista2)):
			if lista[n]==lista2[h]:
				lista3.append(lista2[h])
	aumento=0			
	for g in range(len(lista3)):
		aumento+=1
		lista4.append(lista3[g])

	print("Hay %d"%aumento + " numeros pertenecientes a la serie fibonacci")
	print("Y son: ",lista4)				


except ValueError:
	print("El valor digitado debe ser numerico")	