#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el promedio entero de los datos de la lista'''

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

	print("El promedio entero de los elementos de la lista es:",promedio)
	
except ValueError:
	print("El valor digitado debe ser numerico")		

