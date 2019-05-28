#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición está el
número con más dígitos'''

try:

	lista=[]
	lista2=[]
	lista3=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		numero=lista[b]
		l1=1
		l2=10	

		while numero>=l2:
			l1+=1
			l2=l2*10

		lista2.append(l1)	


	mayor=lista2[0]

	for c in range(len(lista2)):
		if lista[c]>mayor:
			mayor=lista[c]

	for d in range(len(lista)):
		if lista[d]==mayor:
			lista3.append(d)				

	print("El numero con mas digitos esta en la posicion: ",lista3)		

except ValueError:
	print("El valor digitado debe ser numerico")