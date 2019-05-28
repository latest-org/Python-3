#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar si el promedio entero
de dichos números es un número primo'''

try:

	lista=[]
	lista2=[]

	for a in range(3):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)


	promedio=0
	suma=0
	contador=0	
	for b in range(len(lista)):
		suma+=lista[b]
		contador+=1
		promedio=suma//contador

	print("Promedio de la lista: %d"%promedio)	

	contador2=0	
	for c in range(1,promedio+1):
		if (promedio%c)==0:
			contador2+=1

	if contador2==2:
		print("El promedio de la lista es un numero primo")

	else:
		print("El promedio de la lista no es un numero primo")			



except ValueError:
	print("El valor digitado debe ser numerico")