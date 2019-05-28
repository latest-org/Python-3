#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos datos
almacenados son múltiplos de 3.'''

try:
	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	aumento=0	
	for b in range(len(lista)):
		if lista[b]%3==0:
			aumento+=1

	if aumento>0:
		print("Hay %d"%aumento + " numeros multiplos de 3")

	else:
		print("No hay numeros multiplos de 3")

except ValueError:
	print("El valor digitado debe ser numerico")					