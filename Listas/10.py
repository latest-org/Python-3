#-*-coding:utf-8-*-


'''Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números con más de 3 dígitos'''

try:
	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		if lista[b]>=1000:
			lista2.append(b)

	print("Los numeros con mas de tres digitos estan ubicados en las posiciones: ",lista2)
	
except ValueError:
	print("El valor digitado debe ser numerico")			