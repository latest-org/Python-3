#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números terminados en 4'''

try:

	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)	

	aumento=0	
	for b in range(len(lista)):
		if lista[b]%10==4:
			aumento+=1
			lista2.append(b)

	if aumento>0:		
		print("Los numeros terminados en 4 estan en las posiciones: ",lista2)

	else:
		print("No hay numeros terminados en 4")	
	
except ValueError:
	print("El valor digitado debe ser numerico")				
