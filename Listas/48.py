#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición se
encuentra el número primo con mayor cantidad de dígitos pares'''

try:
	lista=[]
	lista2=[]
	lista3=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		primo=lista[b]
		contador=0

		for c in range(1,primo+1):
			if (primo%c)==0:
				contador+=1

		if contador==2:
			lista2.append(primo)


	for d in range(len(lista2)):
		primo2=lista[d]

		while primo2>0:
			digito=primo2%10
			if digito%2==0:
				lista3.append(primo2)
			primo2=primo2//10			


except ValueError:
	print("El valor digitado debe ser numerico")	