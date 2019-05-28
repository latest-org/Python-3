#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuál es el número
menor'''

try:
	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	menor=lista[0]
		
	for b in range(len(lista)):
		if lista[b]<menor:
			menor=lista[b]

	print("El numero menor es: ",menor)	

except ValueError:
	print("El valor digitado debe ser numerico")