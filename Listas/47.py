#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se
encuentran los números múltiplos de 10. No utilizar el número 10 en ninguna operación'''

try:
	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)
	
	aumento=0
	for b in range(len(lista)):
		if lista[b]%10==0 and lista[b]>10:
			lista2.append(b)
			aumento+=1

	if aumento>0:
		print("Los numeros multiplos de 10 estan en las posiciones: ",lista2)

	else:
		print("En la lista no hay numeros multiplos de 10")			


except ValueError:
	print("El valor digitado debe ser numerico")	