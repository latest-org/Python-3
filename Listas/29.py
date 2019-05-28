#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y mostrar en pantalla todos los
enteros comprendidos entre 1 y cada uno de los dígitos de cada uno de los números
almacenados en la lista'''

try:

	lista=[]
	lista2=[]

	for a in range(1):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		numero=lista[b]
		suma=0

		while numero>0:
			digito=numero%10	
			numero=numero//10

			print(C)



except ValueError:
	print("El valor digitado debe ser numerico")