#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se
encuentra el número con mayor cantidad de dígitos primos'''

try:
	lista=[]
	lista2=[]
	lista3=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		primo=lista[b]
		aumento=0

		while primo>0:
			digito=primo%10
			if digito==2 or digito==3 or digito==5 or digito==7:
				aumento+=1
			primo=primo//10
		lista2.append(aumento)

	mayor=lista2[0]

	aumento=0
	for c in range(len(lista2)):
		if lista[c]>mayor:
			mayor=lista[c]

	for d in range(len(lista)):
		if lista[d]==mayor:
			aumento+=1
			lista3.append(d)

	if aumento==1:
		print("El numero con mayor cantidad de digitos esta en la posicion: ",lista3)
		

	if	aumento>1:
		print("El numero con mayor cantidad de digitos esta en las posiciones: ",lista3)

	else:
		print("No hay digitos primos en la lista")		



except ValueError:
	print("El valor digitado debe ser numerico")	