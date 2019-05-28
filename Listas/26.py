#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y calcularle el factorial a cada uno de
los números leídos almacenándolos en otra lista'''

try:

	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		numero=lista[b]
		factorial=1

		for c in range(1,numero+1):
			factorial=factorial*c

		lista2.append(factorial)
		
	print("Numeros ingresados: ",lista)	
	print("Factorial de los numeros: ",lista2)		


except ValueError:
	print("El valor digitado debe ser numerico")