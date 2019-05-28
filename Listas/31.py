#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar
cuántos divisores exactos tiene este último número entre los valores almacenados en la lista'''

try:

	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero que sera almacenado en la lista: "))
		lista.append(numeros)

	print(" ")	
	leido=int(input("Digite un numero que sera comparado con la lista: "))

	aumento=0	
	for b in range(len(lista)):
		if leido%lista[b]==0:
			aumento+=1	

	if aumento>0:
		print("El numero tiene %d"%aumento + " divisores")

	else:
		print("El numero no tiene divisores")			

except ValueError:
	print("El valor digitado debe ser numerico")