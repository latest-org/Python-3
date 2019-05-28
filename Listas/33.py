#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual la
suma de los dígitos pares de cada uno de los números leídos'''

try:

	lista=[]
	lista2=[]

	for a in range(3):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		numero=lista[b]
		suma=0
		aumento=0

		while numero>0:
			digito=numero%10
			if digito%2==0:
				suma+=digito
				aumento+=1
				lista2.append(suma)
			numero=numero//10

		if aumento>0:		
			print(suma)		


except ValueError:
	print("El valor digitado debe ser numerico")