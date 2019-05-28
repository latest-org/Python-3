#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántas veces se repite
el promedio entero de los datos dentro de la lista'''

try:
	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	suma=0
	promedio=0	

	for b in range(len(lista)):
		suma+=lista[b]
		promedio=suma//10

	print("El promedio de la lista es: ",promedio)		
	
	aumento=0	
	for c in range(len(lista)):
		if lista[c]==promedio:
			aumento+=1


	if aumento>0:		
		print("Y se repite %d"%aumento + " veces en la lista")

	else:
		print("Y no se repite en la lista")	
	
except ValueError:
	print("El valor digitado debe ser numerico")				