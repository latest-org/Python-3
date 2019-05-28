#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar si
este último entero se encuentra entre los 10 valores almacenados en la lista'''

try:

	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero que sera almacenado en lista: "))
		lista.append(numeros)

	print(" ")	
	leido=int(input("Digite un numero para compararlo con la lista: "))

	aumento=0	
	for b in range(len(lista)):
		if lista[b]==leido:
			aumento+=1	

	if aumento>0:
		print("El numero esta dentro de los elementos de la lista")

	else:
		print("El numero no esta dentro de los elementos de la lista")			

except ValueError:
	print("El valor digitado debe ser numerico")