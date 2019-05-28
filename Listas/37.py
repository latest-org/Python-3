#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar a cuántos es igual el
cuadrado de cada uno de los números leídos'''

try:

	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	cuadrado=0	
	for b in range(len(lista)):
		cuadrado=lista[b]*lista[b]
		lista2.append(cuadrado)

	print("El cuadrado de cada elemento de la lista es: ",lista2)		

except ValueError:
	print("El valor digitado debe ser numerico")