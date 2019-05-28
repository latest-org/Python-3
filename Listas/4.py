#-*-coding:utf-8-*-

'''Cargar una lista de 10 posiciones con los 10 primeros elementos de la serie de Fibonacci y mostrarlo en pantalla'''

try:

	lista=[]
	lista2=[0,1,1]

	numero1=1
	numero2=1
	numero3=0

	for i in range(0,7):
		print("%d"%i + "="+ "%d"%numero1)

		numero3=numero2
		numero2=numero1
		numero1=numero2+numero3

		lista.append(numero1)


	print(lista2+lista)	

except ValueError:
	print("El valor digitado debe ser numerico")		


