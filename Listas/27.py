#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el
promedio entero de los factoriales de cada uno de los números leídos'''

try:

	lista=[]
	lista2=[]
	lista3=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)


	for b in range(len(lista)):
		numero=lista[b]

		promedio=0
		suma=0
		aumento=0

		for c in range(1,numero+1):
			suma=suma+c
			aumento+=1
			promedio=suma//aumento
		lista2.append(promedio)

	print("El promedio de los factoriales de cada numero es: ",lista2)	




except ValueError:
	print("El valor digitado debe ser numerico")